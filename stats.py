def get_num_words(text_content):
        words = text_content.split()
        nums = len(words)
        return nums

def get_book_text(file_path):
        with open(file_path) as f:
                content = f.read()
                return content
file_path = "/home/tony/workspace/github.com/tony/bookbot/books/frankenstein.txt"
text_content = get_book_text(file_path)

def count_characters(text_content):
	char_count = {}
	text_lower = text_content.lower()
	for char in text_lower:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count

def sort_character_stats(char_dict):
	# Создаем список словарей
	char_list = []
	# Преобразуем словарь в список словарей
	for char, count in char_dict.items():
		if char.isalpha():
			char_list.append({"char": char, "num": count})
			# Сортируем список по ключу "num" от большего к меньшему
	char_list.sort(key=lambda x: x["num"], reverse=True)
	return char_list

