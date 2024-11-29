# MINIBIUDŽETAS_1 - atskira užduotis, daroma atskiram PyCharm projekte
# Parašyti programą minibiudžetas. Programa turi meniu punktus:
# 1. Įvesti pajamas
# 2. Įvesti išlaidas
# 3. Atspausdinti pajamų eilutes
# 4. Atspausdinti išlaidų eilutes
# 5. Atspausdinti statistiką
# q - Išeiti

# Vartotojui leidžiam įvesti tokius duomenis - DATA(datetime arba tiesiog stringas), pajamų ar išlaidų
# PAVADINIMA(pvz. pajamose - avansas, atlyginimas, stipendija ar pan, išlaidose - maistas, įvairūs pirkiniai,
# būsto išlaidos ir tt) ir SUMA (SKAICIUS).
# Duomenis saugom listuose.
# Turime 2 pagrindinius listus - pajamos, islaidos,
# juose saugom vidinius listus(kaip paskaitose pavyzdys su listu darbuotojai).
# Programą kuriam naujame Pycharm projekte, iniciavę git repositoriją ir kodą rašom etapais, darydami commit po
# kiekvieno etapo, pvz sukuriam vartotojo meniu, toliau vystom funkcionalumą kiekvienam meniu punktui.


# Reikėtų panaudoti bent vieną savo parašytą funkciją iškeltą į kitą failą ir importuojamą į pagrindinę programą.
#
# Padarę šį, pradinį variantą, prijungiam trynimo funkciją ir paieškos funkciją, loginimą. Trinti per indeksą,
# pradžioje išvedus turimus duomenis su indekso numeriu, tam galime panaudoti ENUMERATE. Pabandykim
# bent dalį veiksmų kelti į funkcijas.
pajamos = []
islaidos = []
while True:
    print("1. Įvesti pajamas \n"
          "2. Įvesti išlaidas\n"
          "3. Atspausdinti pajamų eilutes\n"
          "4. Atspausdinti išlaidų eilutes\n"
          "5. Atspausdinti statistiką\n"
          "6. trynimo funkciją\n"
          "7. paieškos funkciją\n"
          "stop. baigti programą")
    pasirinkimas = input("pasirinkimas:   ")
    if pasirinkimas == "stop":
        print("Programa baigta")
        break
    if pasirinkimas == "1":
        data = input("įveskite datą yyyy-mm-dd: ")
        pavadinimas = input("įveskite pajamų pavadinimą: ")
        suma = float(input("įveskite pajamų sumą: "))
        pajamos.append([data, pavadinimas, suma])
        print("pridėtos pajamos", pajamos[-1])
    if pasirinkimas == "2":
        data = input("įveskite datą yyyy-mm-dd: ")
        pavadinimas = input("įveskite išlaidų pavadinimą: ")
        suma = float(input("įveskite išlaidų sumą: "))
        islaidos.append([data, pavadinimas, suma])
        print("pridėtos išlaidos", islaidos[-1])
    if pasirinkimas == "3":
        for elem in pajamos:
            print(f"data: {elem[0]}, pavadinimas: {elem[1]}, suma: {elem[2]} EUR")
    if pasirinkimas == "4":
        for elem in islaidos:
            print(f"data: {elem[0]}, pavadinimas: {elem[1]}, suma: {elem[2]} EUR")
    if pasirinkimas == "5":
        pajamu_suma = sum([elem[2] for elem in pajamos])
        islaidu_suma = sum(elem[2] for elem in islaidos)
        balancas = pajamu_suma - islaidu_suma
        print(f"Visos pajamos: {pajamu_suma} EUR")
        print(f"visos išlaidos: {islaidu_suma} EUR")
        print(f"balancas; {balancas} EUR")
    # if pasirinkimas == "6":

file = open("logginimas.txt", mode="w")
file.write(f"Visos įrasšytos pajamos: {pajamos}")
file.write(f"Visos įrašytos išlaidos: {islaidos}")
# file.write(f"Pajamų suma: {pajamu_suma} EUR")
# file.write(f"Išlaidų suma: {islaidu_suma} EUR")
# file.write(f"balancas: {balancas} EUR")
