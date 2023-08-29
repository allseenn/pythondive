# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.


# ВНИМАНИЕ! Задание сделано в виртуальной среде venv, установите зависимости:
# pip install -r requirements.txt
# и активируйте среду: 
# source venv/bin/activate

import requests
import re

url = "https://www.rfc-editor.org/rfc/rfc10.txt"
response = requests.get(url)

if response.status_code == 200:
    text = response.text
else:
    print(f"Не удалось скачать текст. Код состояния: {response.status_code}")

word_list = re.sub(r'\s+', ' ', text).replace(',', '').replace('.', '').replace(';', '') \
            .replace(':', '').replace('!', '').replace('?', '').lower().split()

word_dict = {}
for i in word_list:
    if i not in word_dict.keys():
        word_dict[i] = 1
    else:
        word_dict[i] += 1

sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))

for k, i in enumerate(list(sorted_dict)[:10], 1):
    print(f"{k:>2}. {i} встречается {sorted_dict[i]} раз")


