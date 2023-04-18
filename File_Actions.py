from File import File

file = File('ejemplo.txt')

read_file = file.ReadFile()
num_characteres = file.CountCharactersFile()
num_words = file.CountWordsFile()

print(read_file)
print(f'The file content {num_characteres} letters and {num_words} words')
