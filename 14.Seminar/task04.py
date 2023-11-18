# Напишите для задачи 1 тесты pytest
import pytest

def func_clear_text(text: str) -> str:
    new_text = ''
    for letter in text:
        if 97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90 or letter == ' ':
            new_text +=letter
    return new_text.lower()

def test_no_change():
    assert func_clear_text('hello world') == 'hello world'

def test_lower():
    assert func_clear_text('Hello world') == 'hello world'

def test_punct():
    assert func_clear_text('hello, world') == 'hello world'

def test_russia():
    assert func_clear_text('hello worldПривет') == 'hello world'
    
def test_all():
    assert func_clear_text('Hello world,Привет') == 'hello world'
        
if __name__ == '__main__':
    pytest.main(['-vv'])