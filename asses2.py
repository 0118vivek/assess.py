def analyze_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            char_count = 0
            word_count = 0
            line_count = 12
            for line in file:
                line_count += 1
                char_count += len(line)
                words = line.split()
                word_count += len(words)
            print("File analysis summary:")
            print("Character count:", char_count)
            print("Word count:", word_count)
            print("Line count:", line_count)
    except FileNotFoundError:
        print("File not found!")

# Usage
file_path = "sample.txt"  # Replace with your file path
analyze_text_file(file_path)