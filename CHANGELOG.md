# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - 2025-01-04

### Added
- Comprehensive test suite with 20 tests merged into single `test_sound_soup.py` file
- Manual test script (`manual_test.py`) for end-to-end package verification
- Test coverage for exceptions, AudioTag model, and AudioSoup core functionality

### Changed
- Consolidated all tests from separate files into one unified test file
- Improved test organization with clear sections for different components

### Removed
- Deprecated separate test files (`test_core.py`, `test_models.py`, `test_exceptions.py`)

## [0.1.2] - 2025-01-04

### Changed
- Enhanced installation documentation with platform-specific FFmpeg installation instructions
- Clarified that all Python dependencies are automatically installed with the package
- Verified dependency configuration ensures proper installation of openai-whisper, yt-dlp, and pydub

## [0.1.1] - 2025-01-04

### Added
- Development setup instructions in README
- Package building and publishing guidelines
- Project structure overview
- Code quality tools usage (Black, Ruff)
- TestPyPI publishing workflow documentation

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

[0.1.3]: https://github.com/PierrunoYT/sound-soup/releases/tag/v0.1.3
[0.1.2]: https://github.com/PierrunoYT/sound-soup/releases/tag/v0.1.2
[0.1.1]: https://github.com/PierrunoYT/sound-soup/releases/tag/v0.1.1
[0.1.0]: https://github.com/PierrunoYT/sound-soup/releases/tag/v0.1.0

