class WordsFinder:

    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                text_file = file.read()
                new_file = text_file.lower()
                del_punctuation = [',', '.', '=', '!', '?', ';', ':',
                                   ' - ']
                for k in range(len(del_punctuation)):
                    new_file = new_file.replace(del_punctuation[k], "")
                all_words[i] = new_file.split()
        return all_words

    def find(self, word):
        word = word.lower()  
        found_position = {}
        for file, words in self.get_all_words().items():
            position = 0
            for i in words:
                position += 1
                if i == word:
                    found_position[file] = position
                    break
        return found_position

    def count(self, word):
        word = word.lower()
        number_of_words = {}
        for file, words in self.get_all_words().items():
            count = 0
            for i in words:
                if i == word:
                    count += 1
            number_of_words[file] = count
        return number_of_words


# Проверка кода
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего