from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings, start=1):
        x = file.tell()
        file.write(string + '\n')
        strings_positions[(i, x)] = string
    return strings_positions
    file.close()



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
