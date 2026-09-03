import argparse
import logging
import os
from pathlib import Path

from faster_whisper import WhisperModel
from rich.progress import (BarColumn, Progress, TimeElapsedColumn,
                           TimeRemainingColumn)
from rich_argparse import RichHelpFormatter

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe an audio file using faster-whisper",
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("audio_file", help="Path to the .m4a (or other) audio file.")
    args = parser.parse_args()

    audio_path = Path(args.audio_file)
    if not audio_path.exists():
        raise FileNotFoundError(f"Bruh... can't find: {audio_path}")

    model_size = os.getenv("WHISPER_MODEL", "medium")
    device = os.getenv("WHISPER_DEVICE", "cpu")
    compute_type = os.getenv("WHISPER_COMPUTE_TYPE", "int8")
    model = WhisperModel(model_size, device=device, compute_type=compute_type)

    # First pass: get metadata including duration
    # (fast, doesn't decode audio fully)
    _, info = model.transcribe(str(audio_path), beam_size=5, without_timestamps=True)

    total_duration = info.duration  # seconds of audio

    full_segments = []
    processed_time = 0.0

    # Pretty lil' progress bar setup
    with Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.1f}%",
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        transient=True,
        speed_estimate_period=5,
    ) as progress:

        task_id = progress.add_task("✨ Transcribing...", total=total_duration)

        # Real transcription
        segments, _ = model.transcribe(str(audio_path), beam_size=5)

        for seg in segments:
            full_segments.append(seg.text)
            processed_time = seg.end
            progress.update(task_id, completed=processed_time)

    # Stitch transcript
    full_transcript = " ".join(full_segments)

    out_path = audio_path.with_suffix(".txt")
    out_path.write_text(full_transcript)

    logger.info("Transcript saved to: %s", out_path)


if __name__ == "__main__":
    main()
