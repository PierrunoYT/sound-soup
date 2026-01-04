"""
Basic usage example for sound-soup.
"""

from sound_soup import AudioSoup


def main():
    # Example with YouTube URL
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your URL
    
    print("=" * 60)
    print("Basic sound-soup Usage")
    print("=" * 60)
    
    with AudioSoup(url, model_size="base", verbose=True) as soup:
        # Get full transcript
        print("\n📝 Full Transcript:")
        print("-" * 60)
        print(soup.get_text()[:500] + "...")
        
        # Search for specific text
        print("\n🔍 Searching for 'example'...")
        matches = soup.find_all(text="example")
        
        print(f"Found {len(matches)} matches:")
        for i, match in enumerate(matches[:5], 1):  # Show first 5
            print(f"  {i}. [{match.start:.1f}s - {match.end:.1f}s] {match.text[:60]}...")
        
        # Export first match if any found
        if matches:
            print(f"\n💾 Exporting first match...")
            filename = matches[0].export("example_clip.mp3")
            print(f"   Saved to: {filename}")


if __name__ == "__main__":
    main()

