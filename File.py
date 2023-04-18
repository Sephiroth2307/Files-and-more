class File:

    def __init__(self, archivo):
        self.archivo = archivo
        self.content = ""

    def ReadFile(self):
        with open(self.archivo, "r") as file:
            self.content = file.read()
        return self.content

    def CountCharactersFile(self):
        file_characters = len(self.content)
        return file_characters

    def CountWordsFile(self):
        words = self.content.split()
        file_words = len(words)
        return file_words
