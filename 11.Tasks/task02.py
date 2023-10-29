
class Archive:
    def __new__(cls):
        _instance.archive_text = list()
        _instance.archive_number = list()


    def __init__(self, text, number):
        self.archive_text.append(text)
        self.archive_number.append(number)

    def __str__(self):
        return f"Text is {self.archive_text[-1]} and number is {self.archive_number[-1]}. Also {[i for i in self.archive_text]} and {[i for i in self.archive_number]}"
    
    def __repr__(self):
        return f"Archive({[i for i in self.archive_text]}, {[i for i in self.archive_number]})"


ss = Archive("Hello", 42)
ww = Archive("World", 42)
print(repr(ss))

zz = Archive(['Hello', 'World'], [42, 42])
print(zz)