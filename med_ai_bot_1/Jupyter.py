import csv
import difflib
from collections import Counter

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

def write_file_two(file_path_w, text): #запись топ-10 жалоб
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

def list_complaint(file_path):
    file_path_write = '/home/log/med_ai_bot_1/med_ai_bot_1/Задание второго этапа Сириус.ИИ/2.Жалобы.csv'

    data = load_csv(file_path)

    sorted_complaints = sort_complaints_by_frequency(data)

    write_file_two(file_path_write, sorted_complaints)

    return sorted_complaints


def top_ten(file_path): #функция находит топ 10 самых частых жалоб
    file_path_write = '/home/log/med_ai_bot_1/med_ai_bot_1/Задание второго этапа Сириус.ИИ/4.Топ_10_Жалоб.txt'

    data = load_csv(file_path)

    filter_data = filter_sentences(data)

    top_duplicates = find_duplicates(filter_data)

    top_duplicates = write_file_four(file_path_write, top_duplicates)

    return top_duplicates


if __name__ == "__main__":
    file_path_dataset = '/home/log/med_ai_bot_1/med_ai_bot_1/database/med.csv'
    
    top_duplicates = top_ten(file_path_dataset)

    sorted_complaints = list_complaint(file_path_dataset)

    print("Топ-10 повторяющихся жалоб:")

    for text_out, count in top_duplicates:
        print(f"{text_out}: {count} раз(а)")
    
    print('\n\n-----------------------------------------------------------\n\n')

    

    
    