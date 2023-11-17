import csv
import re

arr = [" "]*10000
i=0
prepositions = [
    "в", "на", "под", "за", "над", "через", "между", "перед", "после",
    "с", "из", "у", "о", "об", "при", "к", "от", "до", "для", "без",
    "около", "вокруг", "внутри", "среди", "вдоль", "впереди", "возле",
    "о", "из-за", "но", "нет", "при", "ваш", "и", "по"
]

#
#for num, word in enumerate(prepositions):
#    print(num)
#def comparison(i, x):
#
#    #print(f"{str(_x)} : {str(prepositions[i])}")
#    word_1 = str(_x.split())
#    word_2 = str(prepositions[i-1])
#
#    if word_1 != word_2:
#        if int(i) < 34:
#            return comparison(i+1, x)
#        else:
#            return _x
#    else:
#        return 0


with open("/home/log/med_ai_bot_1/med_ai_bot_1/database/med.csv", newline='', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                _space = row['Жалобы']
                _space = _space.strip().lower()
                _comma = re.sub(r",", " ,", _space).split(',')
                for x in _comma:
                    print(f'{x} ,')


               #_out = [i for i in _comma.split(",")]
           #for _v in _out:


                    #print("\n\ndone\n\n\n\n")

                #arr[i] = _v
                #i = i +1
                #print(i-1)

                #out = format(arr)
                #print(f'{out},')
                ##for _x in _v:
                ##    _j = f'{_x.strip()} '
                #print(',')
            print('\n')



            #print(row['Жалобы'], '|', row['ПеренесенныеЗаболевания'])
            #with open("finaly.csv", 'w', newline='', encoding="utf8") as csvfile:
            #    writer = csv.writer(csvfile, delimiter=";")
            #    writer.writerow(["row 1 el 1", "row 1 el 2", "row 1 el 3"])


    