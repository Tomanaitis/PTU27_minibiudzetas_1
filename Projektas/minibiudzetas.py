# MINIBIUDŽETAS_1 - atskira užduotis, daroma atskiram PyCharm projekte
# Parašyti programą minibiudžetas. Programa turi meniu punktus:
# 1. Įvesti pajamas
# 2. Įvesti išlaidas
# 3. Atspausdinti pajamų eilutes
# 4. Atspausdinti išlaidų eilutes
# 5. Atspausdinti statistiką
# q - Išeiti
# Vartotojui leidžiam įvesti tokius duomenis - data(datetime arba tiesiog stringas), pajamų ar išlaidų
# pavadinimas(pvz. pajamose - avansas, atlyginimas, stipendija ar pan, išlaidose - maistas, įvairūs pirkiniai,
# būsto išlaidos ir tt) ir suma.

# Duomenis saugom listuose.
# Turime 2 pagrindinius listus - pajamos, islaidos,
# juose saugom vidinius listus(kaip paskaitose pavyzdys su listu darbuotojai).

# Programą kuriam naujame Pycharm projekte, iniciavę git repositoriją ir kodą rašom etapais, darydami commit po
# kiekvieno etapo, pvz sukuriam vartotojo meniu, toliau vystom funkcionalumą kiekvienam meniu punktui.
# Reikėtų panaudoti bent vieną savo parašytą funkciją iškeltą į kitą failą ir importuojamą į pagrindinę programą.
#
# Padarę šį, pradinį variantą, prijungiam trynimo funkciją ir paieškos funkciją, loginimą. Trinti per indeksą,
# pradžioje išvedus turimus duomenis su indekso numeriu, tam galime panaudoti enumerate. Pabandykim
#  bent dalį veiksmų kelti į funkcijas.

while True:
    print("1. Įvesti pajamas \n"
          "2. Įvesti išlaidas\n"
          "3. Atspausdinti pajamų eilutes\n"
          "4. Atspausdinti išlaidų eilutes\n"
          "5. Atspausdinti statistiką")
    pasirinkimas = input("pasirinkimas:   ")
    #if pasirinkimas == "1":