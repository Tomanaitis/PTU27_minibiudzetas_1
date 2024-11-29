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
"""
f06_sudetiniai_listai
darbuotojai = [
    ["Valdas", "programuotojas", 2000],
    ["Adomas", "direktorius", 3000],
    ["Aldona", "vadybininkas", 1800],
    ["Jogaila", "programuotojas", 2500],

"""

# Programą kuriam naujame Pycharm projekte, iniciavę git repositoriją ir kodą rašom etapais, darydami commit po
# kiekvieno etapo, pvz sukuriam vartotojo meniu, toliau vystom funkcionalumą kiekvienam meniu punktui.
# Reikėtų panaudoti bent vieną savo parašytą funkciją iškeltą į kitą failą ir importuojamą į pagrindinę programą.
#
# Padarę šį, pradinį variantą, prijungiam trynimo funkciją ir paieškos funkciją, loginimą. Trinti per indeksą,
# pradžioje išvedus turimus duomenis su indekso numeriu, tam galime panaudoti enumerate. Pabandykim
# bent dalį veiksmų kelti į funkcijas.
pajamos = [

]
islaidos = [

]

while True:
    print("1. Įvesti pajamas \n"
          "2. Įvesti išlaidas\n"
          "3. Atspausdinti pajamų eilutes\n"
          "4. Atspausdinti išlaidų eilutes\n"
          "5. Atspausdinti statistiką\n"
          "stop. baigti programą")
    pasirinkimas = input("pasirinkimas:   ")
    if pasirinkimas == "stop":
        print("Programa baigta")
        print(islaidos)
        print(pajamos)
        break
    if pasirinkimas == "1":
        data = input("įveskite datą yyyy-mm-dd: ")
        pavadinimas = input("įveskite pajamų pavadinimą: ")
        suma = input("įveskite pajamų sumą: ")
        print(f"data: {data}, pavadinimas: {pavadinimas}, suma: {suma}")
        pajamos.append([f"data: {data}, pavadinimas: {pavadinimas}, suma: {suma}"])
        print(pajamos)
        continue
    if pasirinkimas == "2":
        data = input("įveskite datą yyyy-mm-dd: ")
        pavadinimas = input("įveskite išlaidų pavadinimą: ")
        suma = input("įveskite išlaidų sumą: ")
        islaidos.append([f"data: {data}, pavadinimas: {pavadinimas}, suma: {suma}"])
        print(islaidos)
