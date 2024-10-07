import os
from mutagen import File

def extract_tags(file_path):
    """Extract the artist and track title tags from an audio file."""
    try:
        audio = File(file_path, easy=True)
        artist = audio.get('artist', ['Unknown Artist'])[0]
        title = audio.get('title', ['Unknown Title'])[0]
        return artist, title
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None

def scan_directory(directory):
    """Scan through a directory and its subdirectories for audio files and extract artist and track title tags."""
    tags_list = []
    
    # Supported audio file extensions
    supported_extensions = ('.mp3', '.flac', '.ogg', '.wav', '.m4a', '.aac')

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(supported_extensions):
                file_path = os.path.join(root, file)
                artist, title = extract_tags(file_path)
                if artist and title:
                    tags_list.append((file_path, artist, title))
    
    return tags_list

def write_tags_to_file(tags_list, output_file):
    """Write the extracted artist and track title tags to a text file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for file_path, artist, title in tags_list:
            f.write(f"File: {file_path}\n")
            f.write(f"  Artist: {artist}\n")
            f.write(f"  Title: {title}\n\n")

def main():
    input_directory = input("Enter the directory to scan for audio files: ")
    output_file = input("Enter the output text file name: ")
    
    tags_list = scan_directory(input_directory)
    write_tags_to_file(tags_list, output_file)

    print(f"Artist and track title tags extracted and saved to {output_file}")

if __name__ == "__main__":
    main()
