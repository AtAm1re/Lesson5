def custom_write(file_name, strings):
    file_ = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    number = 0
    for i in strings:
        number += 1
        strings_positions[(number, file_.tell())] = i
        file_.write(f'{i}\n')
    file_.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
    