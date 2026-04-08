# SoundScribe

Audio transcription CLI tool using faster-whisper with a progress bar.

I got tired of running `faster-whisper` and staring at a blank terminal with no idea whether it
was working, stuck, or halfway done. Long audio files could take minutes with zero feedback.
So I wrapped it in a proper CLI with a live progress bar and time estimates — because knowing
how long something will take is basic UX, even for a local dev tool.

## Features

- Fast transcription using faster-whisper
- Progress bar with time estimates
- Supports various audio formats (.m4a, .mp3, .wav, etc.)
- Automatic output to .txt file

## Installation

### Install with pip (editable)

```bash
cd soundscribe
pip install -e .
```

## Usage

Once installed, you can use the `soundscribe` command from anywhere:

```bash
soundscribe audio_file.m4a
```

This will:

1. Transcribe the audio file
2. Show a progress bar during transcription
3. Save the transcript as `audio_file.txt` in the same directory

## Example

```bash
$ soundscribe my_recording.m4a
✨ Transcribing... ████████████████████ 100% 0:00:45 0:00:00
✨ Transcript saved to: my_recording.txt
```

## Requirements

- Python >= 3.8
- faster-whisper
- rich
- rich-argparse

All dependencies are automatically installed during installation.

## Uninstall

```bash
pip uninstall soundscribe
```

<br>
