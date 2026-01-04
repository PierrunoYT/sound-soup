# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-XX

### Added
- Initial release of sound-soup
- `AudioSoup` class for parsing audio like HTML with BeautifulSoup-style API
- `AudioTag` model representing transcribed audio segments
- Support for YouTube URL downloads via yt-dlp
- Support for local audio files (MP3, WAV, M4A, FLAC, etc.)
- AI-powered transcription using OpenAI Whisper
- `find_all()` and `find()` methods for searching transcripts
- `export()` method on AudioTag for extracting audio clips
- Lazy loading of audio segments to prevent RAM overload
- Context manager support (`with` statement) for automatic cleanup
- Progress callbacks via `verbose` parameter
- Custom exception hierarchy (`SoundSoupError`, `DownloadError`, `TranscriptionError`, `ExportError`)
- Support for multiple Whisper model sizes (tiny, base, small, medium, large)
- Case-sensitive and case-insensitive search options
- Comprehensive README with examples and FAQ
- Example scripts for basic usage and podcast clip extraction
- Test suite structure with pytest

### Technical Details
- Memory-efficient design: audio segments are lazy-loaded only when exporting
- Automatic temporary file cleanup via context manager
- Built on well-maintained libraries: OpenAI Whisper, yt-dlp, pydub
- Requires FFmpeg for audio processing
- Python 3.9+ support

[0.1.0]: https://github.com/yourusername/sound-soup/releases/tag/v0.1.0

