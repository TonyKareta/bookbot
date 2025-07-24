import sys
def get_book_text(file_path):
	with open(file_path) as f:
		content = f.read()
		return content
from stats import get_num_words
from stats import count_characters
from stats import sort_character_stats 
def main():
	if len(sys.argv) != 2:
        	print("Usage: python3 main.py <path_to_book>")
        	sys.exit(1)
	file_path = sys.argv[1]
	text_content = get_book_text(file_path)
	words = get_num_words(text_content)
	characters = count_characters(text_content)
	sort_list = sort_character_stats(characters)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found {file_path}...")
	print("----------- Word Count ----------")
	print(f"Found {words} total words")
	print("--------- Character Count -------")
	for item in sort_list:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

if __name__ == "__main__":
    main()
