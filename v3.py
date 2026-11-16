vet = int((input("Введите влажность воздуха: ")))
temperature = int((input("Введите температуру воздуха: ")))

if vet < 40 and temperature < -10:
    print("Сухой трескучий мороз")

elif vet > 40 and vet < 70 and temperature < -10:
    print("Обычная зимняя погода")

elif vet > 75 and temperature < -10:
    print("Сырой обжигающий холод / Изморозь")

elif vet < 40 and temperature > -10 and temperature < 10:
    print("Сухая прохлада")

elif vet > 40 and vet < 70 and temperature > -10 and temperature < 10:
    print("Свежая комфортная погода")

elif vet > 75 and temperature > -10 and temperature < 10:
    print("Промозглая сырость / Дождь / Мокрый снег / Туман")

elif vet < 40 and temperature > 10 and temperature <24:
    print("Сухое тепло")

elif vet > 40 and vet < 70 and temperature > 10 and temperature < 24:
    print("Идеальный комфорт")

elif vet > 70 and temperature > 10 and temperature < 24:
    print("Дождливая погода / После дождя")

elif vet < 40 and temperature > 25:
    print("Засуха / Суховей")

elif vet < 70 and vet > 40 and temperature > 25:
    print("Летний зной")

elif vet > 70 and vet < 100 and temperature > 25 and temperature < 100:
    print("Тропическая духота / Перед грозой или градом.")
else:
    print("Такого нету")
