# Задача № 3
# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import csv
import json
from sys import argv

if len(argv) < 3:
    print(f"Example: python {argv[0]} input.json output.csv")
    exit(1)

def csv_gen(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as input_file, open(csv_file, 'w', newline='', encoding='utf-8') as output_file:
        json_data = json.load(input_file)
        
        # Flatten the nested dictionaries
        flattened_data = []
        for key, value in json_data.items():
            for sub_key, sub_value in value.items():
                flattened_data.append({"level": key, "id": sub_key, "name": sub_value})

        # Specify fieldnames directly in DictWriter constructor
        fieldnames = ["level", "id", "name"]
        
        # Initialize DictWriter with fieldnames and write data rows
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()  # Этот шаг автоматически записывает заголовок
        
        # Write data rows
        csv_writer.writerows(flattened_data)

    return "CSV file successfully created."


if __name__ == '__main__':
    csv_gen(argv[1], argv[2])
