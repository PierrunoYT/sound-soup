"""
Manual test script to verify sound-soup package functionality.

This script tests the package with a real audio file or YouTube URL.
Run this after installing the package to verify everything works.

Usage:
    python manual_test.py
"""

import os
import sys
import tempfile
from pydub import AudioSegment
from sound_soup import AudioSoup


def create_test_audio_with_tone(duration_seconds: int = 10, frequency: int = 440):
    """
    Create a test audio file with a tone (instead of silence).
    This gives Whisper something to potentially transcribe.
    """
    print(f"🎵 Creating test audio file ({duration_seconds}s, {frequency}Hz tone)...")
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.close()
    
    # Create a simple tone
    from pydub.generators import Sine
    tone = Sine(frequency).to_audio_segment(duration=duration_seconds * 1000)
    
    # Make it quieter
    tone = tone - 20  # Reduce volume by 20dB
    
    tone.export(temp_file.name, format="mp3")
    print(f"✅ Created test file: {temp_file.name}")
    
    return temp_file.name


def test_local_file():
    """Test with a local audio file."""
    print("\n" + "="*60)
    print("TEST 1: Local Audio File")
    print("="*60)
    
    audio_path = None
    try:
        # Create test audio
        audio_path = create_test_audio_with_tone(duration_seconds=5)
        
        print(f"\n📂 Testing with local file: {audio_path}")
        print("🤖 Initializing AudioSoup (this may take a moment)...")
        
        # Test AudioSoup
        with AudioSoup(audio_path, model_size="tiny", verbose=True) as soup:
            print(f"\n📊 Results:")
            print(f"   - Audio path: {soup.audio_path}")
            print(f"   - Number of segments: {len(soup.segments)}")
            print(f"   - Full text length: {len(soup.get_text())} characters")
            
            if soup.get_text():
                print(f"\n📝 Transcription:")
                print(f"   {soup.get_text()[:200]}...")
            else:
                print(f"\n📝 Transcription: (empty - tone audio has no speech)")
            
            # Test find methods
            print(f"\n🔍 Testing search functionality...")
            matches = soup.find_all(text="test")
            print(f"   - Matches for 'test': {len(matches)}")
            
            # Test segment export if we have any
            if len(soup.segments) > 0:
                print(f"\n✂️  Testing audio export...")
                first_segment = soup.segments[0]
                output_file = "test_export.mp3"
                first_segment.export(output_file)
                
                if os.path.exists(output_file):
                    file_size = os.path.getsize(output_file)
                    print(f"   ✅ Exported segment to {output_file} ({file_size} bytes)")
                    os.unlink(output_file)
                else:
                    print(f"   ❌ Failed to export segment")
        
        print(f"\n✅ Local file test completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error during local file test: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if audio_path and os.path.exists(audio_path):
            os.unlink(audio_path)
            print(f"🧹 Cleaned up test file")
    
    return True


def test_youtube_url():
    """Test with a YouTube URL (optional - requires internet)."""
    print("\n" + "="*60)
    print("TEST 2: YouTube URL (Optional)")
    print("="*60)
    
    # Ask user if they want to test YouTube
    try:
        response = input("\n⚠️  YouTube test requires internet. Continue? (y/N): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\n⏭️  Skipping YouTube test (non-interactive mode)")
        return True
    
    if response != 'y':
        print("⏭️  Skipping YouTube test")
        return True
    
    # Use a short video for testing
    # This is a 10-second Creative Commons video
    try:
        url = input("\nEnter YouTube URL (or press Enter for default test): ").strip()
    except (EOFError, KeyboardInterrupt):
        url = ""
    
    if not url:
        url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"  # "Me at the zoo" - first YouTube video
    
    try:
        print(f"\n📺 Testing with YouTube URL: {url}")
        print("⬇️  Downloading and transcribing (this may take a while)...")
        
        with AudioSoup(url, model_size="tiny", verbose=True) as soup:
            print(f"\n📊 Results:")
            print(f"   - Audio path: {soup.audio_path}")
            print(f"   - Number of segments: {len(soup.segments)}")
            print(f"   - Full text length: {len(soup.get_text())} characters")
            
            if soup.get_text():
                print(f"\n📝 Transcription:")
                print(f"   {soup.get_text()[:500]}...")
            
            # Test search
            if soup.get_text():
                first_word = soup.get_text().split()[0] if soup.get_text().split() else "test"
                matches = soup.find_all(text=first_word)
                print(f"\n🔍 Search results for '{first_word}': {len(matches)} matches")
        
        print(f"\n✅ YouTube test completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n❌ Error during YouTube test: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_error_handling():
    """Test error handling."""
    print("\n" + "="*60)
    print("TEST 3: Error Handling")
    print("="*60)
    
    try:
        print("\n🧪 Testing invalid file path...")
        try:
            soup = AudioSoup("/nonexistent/file.mp3", verbose=False)
            print("   ❌ Should have raised DownloadError")
            return False
        except Exception as e:
            print(f"   ✅ Correctly raised {type(e).__name__}: {e}")
        
        print(f"\n✅ Error handling test completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n❌ Unexpected error during error handling test: {e}")
        return False


def main():
    """Run all tests."""
    # Set UTF-8 encoding for Windows console
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    
    print("🥣 sound-soup Package Manual Test")
    print("="*60)
    print("This script will test the core functionality of sound-soup")
    print("="*60)
    
    # Check dependencies
    print("\n📦 Checking dependencies...")
    try:
        import whisper
        import yt_dlp
        from pydub import AudioSegment
        print("   ✅ All dependencies installed")
    except ImportError as e:
        print(f"   ❌ Missing dependency: {e}")
        print("\n💡 Install with: pip install -e \".[dev]\"")
        return 1
    
    # Run tests
    results = []
    
    results.append(("Local File", test_local_file()))
    results.append(("YouTube URL", test_youtube_url()))
    results.append(("Error Handling", test_error_handling()))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name:20s} {status}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n🎉 All tests passed! sound-soup is working correctly.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Check the output above for details.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

