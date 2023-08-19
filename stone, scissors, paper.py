from random import randrange

end = ["Вы победили", "Боевая ничья", "Вы проиграли"]
transl = {0: "камень", 1: "ножницы", 2: "бумага"}
motion_of_program = randrange(0, 3)
motion_of_user = input(f"Выберите и напишите: камень, ножницы или бумага: \n").lower()
print(f"Ваш выбор: {motion_of_user}")
print(f"Выбор оппонентa: {transl[motion_of_program]}")

if motion_of_user == "камень":
    if motion_of_program == 0:
        print(end[1])
    elif motion_of_program == 1:
        print(end[0])
    else:
        print(end[2])

elif motion_of_user == "ножницы":
    if motion_of_program == 1:
        print(end[1])
    elif motion_of_program == 2:
        print(end[0])
    else:
        print(end[2])

else:
    if motion_of_program == 2:
        print(end[1])
    elif motion_of_program == 0:
        print(end[0])
    else:
        print(end[2])
