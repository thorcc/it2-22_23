# https://www.uio.no/studier/emner/matnat/ifi/IN1000/h21/undervisningstilbud/alternativt-oblig-lop/week-4/partest-paradise-hotell.md

print("Velkommen til Paradise 2022!")

# importerer randint fra random-biblioteket
from random import randint


# Regler:
# Spillet foregår i 30 runder
# For hver runde øker premien med 10 000 kr
# I hver runde kan spillerne velge om de vil kaste kula eller holde kula

# --- Spillere ---

def optimistisk_spiller(belop):
    # Denne spilleren slipper aldri kula!
    return True # True betyr ikke slipp

def spiller_halvveis(belop):
    # Denne spilleren slipper kula når beløper er 150000 eller høyere
    if belop >= 150000:
        return False # slipper kula
    else:
        return True # hold kula

def usikker_spiller(belop):
    # Denne spilleren slipper kula 10% av gangene
    tilfeldig_tall = randint(1,100)
    if tilfeldig_tall <= 10:
        return False
    else:
        return True

def taktisk_spiller(belop):
    tilfeldig_tall = randint(1,100)
    if tilfeldig_tall <= 10 and belop < 150000:
        return False
    elif tilfeldig_tall <= 30 and belop >= 150000:
        return False
    return True

# --- Spill ---

def spill(funksjon_spiller1, funksjon_spiller2):
    # Denne funksjonen returnerer en liste bestående av to tall, gevinstene til de to spillerne
    belop = 0
    for i in range(30):
        belop += 10000
        # hvis en spiller kaster kula, skal alle pengene gå til hen
        spiller1 = funksjon_spiller1(belop) # true/false
        spiller2 = funksjon_spiller2(belop) # true/false
        if not spiller1:
            # da har spiller1 kastet kula!!
            return [belop, 0]
        if not spiller2:
            # da har spiller2 kastet kula!!
            return [0, belop]
    return [belop/2, belop/2]


# Spiller spill

spill1 = spill(optimistisk_spiller, spiller_halvveis)
print(f'Optimistisk vs. halvveis: {spill1}')

spill2 = spill(taktisk_spiller, spiller_halvveis)
print(f'Taktisk vs. halvveis: {spill2}')

spill3 = spill(usikker_spiller, spiller_halvveis)
print(f'Usikker vs. halvveis: {spill3}')
