import csv
import difflib
import re
from collections import Counter
from difflib import SequenceMatcher

def load_csv(file_path):
    data = []
    with open(file_path, newline='', encoding="utf8") as file:
    
        reader = csv.DictReader(file, delimiter=";")


        for row in reader:
            data.append(row['Жалобы'])
    return data

def write_file_four(file_path_w, text): #запись топ-10 жалоб
    with open(file_path_w, 'w', encoding="utf8") as file:

        for text_out, count in text:
            file.write(f"{text_out}: {count} раз(а)\n")

    return text


def write_complaints(file_path_w, complaints):
    with open(file_path_w, 'w', encoding="utf8") as file:

        file.write("совпадения\n")
        for c in complaints:
            file.write(f'{c}')


def write_file_three(file_path_w, text): #запись 3
    with open(file_path_w, 'w', encoding="utf8") as file:

        file.write(f"Жалобы;\n")
        for text_out, count in text:
            file.write(f"{text_out};\n")


def sort_complaints_by_frequency(complaints):
    # Используем Counter для подсчета частотности каждой жалобы
    complaints_counter = Counter(complaints)
    
    # Сортируем жалобы по частотности встречаемости (от наиболее частых к менее частым)
    sorted_complaints = sorted(complaints_counter.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_complaints


def compare_complaints(data, top_complaints):
    data.append(['Совпадение'])
    for i in range(1, len(data)):
        data[i].append('0')

    # Проходим по каждой жалобе и сравниваем с топ-10
    for i in range(1, len(data)):
        complaint = data[i][0].lower()  # Приводим к нижнему регистру для сравнения
        for top_complaint in top_complaints:
            ratio = SequenceMatcher(None, complaint, top_complaint).ratio()
            # Если коэффициент сходства выше определенного порога (например, 0.8), считаем, что есть совпадение
            if ratio > 0.8:
                data[i][-1] = '1'
                break

    return data


def process_sentences(path, file_path_w):    
    with open(path, newline='', encoding="utf8") as csvfile:
        with open(file_path_w, 'w', encoding="utf8") as file:
            file.write(f"Жалобы;\n")
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                sentences_space = row['Жалобы']
                sentences_space = sentences_space.strip().lower()
                sentences_comma = re.sub(",", " ,", sentences_space).split(',')

                
                
                for text_out in sentences_comma:
                    text_out = text_out.strip()
                    text_out = f'{text_out}'.replace('  ', '').replace('   ','')
                    file.write(f'{text_out}, \n')
                
            

def filter_sentences(sentences):
    filtered_sentences = [sentence for sentence in sentences if 'нет' not in sentence.lower() and 'не предьявляет' not in sentence.lower() and 'не имеет' not in sentence.lower() and 'не предъявляет' not in sentence.lower()and 'медосмотр' not in sentence.lower()] 
    
    return filtered_sentences

def lemmatize_text(text):
    #лемматизация или другой обработки текста
    # В данном примере, используется простая лемматизация, убирающая пробелы и приводящая к нижнему регистру
    return text.lower()

def find_duplicates(data):
    lemmatized_data = [lemmatize_text(text) for text in data]
    duplicates = Counter(lemmatized_data)

    # Выбор топ-10 повторяющихся жалоб
    top_10_duplicates = duplicates.most_common(10)

    return top_10_duplicates

def simple_parsing(file_path):
    file_path_write = '/home/log/med_ai_bot_1/med_ai_bot_1/Задание второго этапа Сириус.ИИ/2.Жалобы.csv'

    process_sentences(file_path, file_path_write)

    return process_sentences


def list_complaint(file_path):
    file_path_write = '/home/log/med_ai_bot_1/med_ai_bot_1/Задание второго этапа Сириус.ИИ/3.Жалобы.csv'

    data = load_csv(file_path)

    sorted_complaints = sort_complaints_by_frequency(data)

    write_file_three(file_path_write, sorted_complaints)

    return sorted_complaints


def top_ten(file_path): #функция находит топ 10 самых частых жалоб
    file_path_write = '/home/log/med_ai_bot_1/med_ai_bot_1/Задание второго этапа Сириус.ИИ/4.Топ_10_Жалоб.txt'

    data = load_csv(file_path)

    filter_data = filter_sentences(data)

    top_duplicates = find_duplicates(filter_data)

    top_duplicates = write_file_four(file_path_write, top_duplicates)

    return top_duplicates


def complaints(path, td):  
    path_w = '/home/log/med_ai_bot_1/med_ai_bot_1/Задание второго этапа Сириус.ИИ/6.Жалобы.csv'

    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    
    complaints = compare_complaints(data, td)
    
    write_complaints(path_w, complaints) 
    
    return complaints
    


if __name__ == "__main__":
    file_path_dataset = '/home/log/med_ai_bot_1/med_ai_bot_1/database/med.csv'
    
    top_duplicates = top_ten(file_path_dataset)

    list_complaint(file_path_dataset)

    simple_parsing(file_path_dataset)
    
    complaints(file_path_dataset, top_duplicates)

    print("Топ-10 повторяющихся жалоб:")

    for text_out, count in top_duplicates:
        print(f"{text_out}: {count} раз(а)")
    
    print('\n\n-----------------------------------------------------------\n\n')


    
    