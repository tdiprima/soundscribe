# SoundScribe

Audio transcription CLI tool using faster-whisper with a progress bar.

I got tired of running `faster-whisper` and staring at a blank terminal with no idea whether it
was working, stuck, or halfway done. Long audio files could take minutes with zero feedback.
So I wrapped it in a proper CLI with a live progress bar and time estimates — because knowing
how long something will take is basic UX, even for a local dev tool.

Plus, I wanted something that does **not** reach out to the cloud to do the transcription.

## Features

- Fast transcription using faster-whisper
- Progress bar with time estimates
- Supports various audio formats (.m4a, .mp3, .wav, etc.)
- Automatic output to .txt file

## Supported Audio Formats

`soundscribe` relies on `faster-whisper`, which uses ffmpeg for audio decoding. Any format ffmpeg supports will work. Common formats include:

| Format | Extension |
|--------|-----------|
| MPEG Audio Layer 3 | `.mp3` |
| MPEG-4 Audio | `.m4a` |
| Waveform Audio | `.wav` |
| FLAC | `.flac` |
| Ogg Vorbis | `.ogg` |
| Opus | `.opus` |
| WebM | `.webm` |
| MP4 video (audio extracted) | `.mp4` |
| AAC | `.aac` |

> **Note:** ffmpeg must be installed and available on your `PATH` for formats other than WAV.

## Installation

### Install with pip (editable)

```bash
cd soundscribe
pip install -e .
```

## First Run

On first run, `faster-whisper` will download the model from Hugging Face and cache it locally. You'll see download progress and a warning like:

```
Warning: You are sending unauthenticated requests to the HF Hub...
```

This is normal. The model is only downloaded once — subsequent runs load it from the local cache (`~/.cache/huggingface/`) with no network activity. **Your audio is never sent anywhere.**

To suppress the warning and get faster downloads, set a (free) [Hugging Face token](https://huggingface.co/settings/tokens):

```bash
export HF_TOKEN=hf_your_token_here
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

<br>
