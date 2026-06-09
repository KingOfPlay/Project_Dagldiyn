# Из предложенного текстового файла (text18-13.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно вставив после строки N (N – задается пользователем)
# произвольную фразу.

with open('text18-13.txt', encoding='utf-16') as file:
    text = file.read()

print(f'Содержимое:\n{text}\n')
print(f'Количество символов в тексте: {len(text)}\n')

try:
    N = int(input('Введите номер строки: '))
except ValueError:
    print('Введите число.')
    exit()

split = text.split('\n')
split.insert(N, 'произвольную фразу')

with open('file.txt', 'w', encoding='utf-16') as file:
    file.write('\n'.join(split))