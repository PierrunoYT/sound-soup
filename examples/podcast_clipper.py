"""
Podcast clip extraction example.
Extract all segments mentioning specific keywords from a podcast.
"""

from sound_soup import AudioSoup
import os


def extract_podcast_clips(source: str, keywords: list, output_dir: str = "clips"):
    """
    Extract clips from a podcast for each keyword.
    
    Args:
        source: YouTube URL or local audio file path
        keywords: List of keywords to search for
        output_dir: Directory to save clips
    """
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"🎙️  Processing podcast: {source}")
    print(f"🔑 Keywords: {', '.join(keywords)}")
    print(f"📁 Output directory: {output_dir}\n")
    
    with AudioSoup(source, model_size="base", verbose=True) as soup:
        # Get full transcript info
        print(f"\n📊 Transcript Statistics:")
        print(f"   Total segments: {len(soup.segments)}")
        print(f"   Total duration: {soup.segments[-1].end:.1f}s" if soup.segments else "N/A")
        
        # Process each keyword
        for keyword in keywords:
            print(f"\n🔍 Searching for '{keyword}'...")
            matches = soup.find_all(text=keyword, case_sensitive=False)
            
            if not matches:
                print(f"   ❌ No matches found")
                continue
            
            print(f"   ✅ Found {len(matches)} matches")
            
            # Export each match
            for i, match in enumerate(matches, 1):
                safe_keyword = keyword.replace(" ", "_").lower()
                filename = os.path.join(
                    output_dir,
                    f"{safe_keyword}_{i:03d}_{int(match.start)}s.mp3"
                )
                
                try:
                    match.export(filename)
                    print(f"      💾 Exported: {filename}")
                except Exception as e:
                    print(f"      ⚠️  Failed to export {filename}: {e}")
    
    print(f"\n✅ Done! Check '{output_dir}' for your clips.")


def main():
    # Example: Extract clips from a tech podcast
    # Replace with your actual YouTube URL or local file
    source = "https://www.youtube.com/watch?v=example"  # Replace!
    
    keywords = [
        "artificial intelligence",
        "machine learning",
        "neural network",
        "deep learning"
    ]
    
    extract_podcast_clips(source, keywords, output_dir="tech_clips")


if __name__ == "__main__":
    main()

