import csv
from collections import Counter
import os

column_name = ('Жалобы')
word_frequencies = Counter()
i = 1



with open("медицинские_протоколы.csv", newline='', encoding="utf8") as csvfile:
    with open("t.txt", 'w') as f:
        reader = csv.DictReader(csvfile, delimiter=";")
        print("wait pleas")
        for row in reader:
            i =+ 1
            if i > 100:
                print(f'/{"*"*i/100}')
                print(i)
                        #print(row[column_name], '\n')

            sentence = row[column_name]

            words = sentence.split()

            # Update the Counter with the words from the current sentence
            word_frequencies.update(words)


        # Print the most common words and their frequencies
        for x in prepositions:
            for word, frequency in word_frequencies.most_common():
                if frequency > 10 and word.split() != x:
                    #print(f"{word}: {frequency} times")

                        f.write(f'\n{word}: {frequency} times')
