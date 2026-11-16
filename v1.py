vet = int(input())

if vet < 20:
    print("Сильная засуха")
elif vet > 20 and vet < 40:
    print("Засуха")
elif vet > 40 and vet < 65:
    print("Нормальная влажность")
elif vet > 65 and vet < 80:
    print("Слабый дождь")
else:
    print("ливень или град")