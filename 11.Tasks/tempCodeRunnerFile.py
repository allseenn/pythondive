class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # print(cls._instance)
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text, number):
        self._instance.text = text
        self._instance.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {[i for i in self._instance.archive_text]} and {[i for i in self._instance.archive_number]}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


archive1 = Archive("Запись 1", 42)
print(archive1)
archive2 = Archive("Запись 2", 3.14)
print(archive2)