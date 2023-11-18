# Напишите для задачи 1 тесты unittest.
def func_clear_text(text: str) -> str:
    new_text = ''
    for letter in text:
        if 97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90 or letter == ' ':
            new_text +=letter
    return new_text.lower()

class TestString(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual('hello world', func_clear_text('hello world'), msg = 'All is NOT Ok')

    def test_lower(self):
        self.assertEqual('hello world', func_clear_text('Hello world'), msg = 'All is NOT Ok')

    def test_punct(self):
        self.assertEqual('hello world', func_clear_text('hello, world'), msg = 'All is NOT Ok')

    def test_russia(self):
        self.assertEqual('hello world', func_clear_text('hello worldваыа'), msg = 'All is NOT Ok')
    
    def test_all(self):
        self.assertEqual('hello world', func_clear_text('Hello world,Привет'), msg = 'All is NOT Ok')
        
if __name__ == '__main__':
    unittest.main(verbosity=2)