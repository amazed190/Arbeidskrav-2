#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: amaliezedell

Arbeidskrav 2


"""

#Oppgave 1 

alder = int(input("Hvilket år er du født?"))

print("Du er", 2024-alder, "år i 2024")



#Oppgave 2

import numpy as np

antall_elever = int(input("Skriv inn antall elever:"))

antall_pizzaer = int(np.ceil(antall_elever/4))

print("Det må kjøpes", antall_pizzaer, "stk pizza")



#Oppgave 3 

import numpy as np 

v_grad = float(input("Skriv inn gradtallet"))

v_rad = v_grad*np.pi/180

print(v_grad, "grader blir", v_rad, "radianer")



#Oppgave 4

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

land = str(input("Skriv inn et land"))
print(data[land][0], "er hovedstaden i", land,"og det er", data[land][1],"mill.innbyggere i", data[land][0])


nytt_land = str(input("Skriv inn et nytt land"))
hovedstad = str(input("Skriv inn hovedstaden i landet"))
innbyggere = float(input("Skriv inn antall milloner innbyggere"))

data[nytt_land]=[hovedstad, innbyggere]

print(data)


#Oppgave 5

import numpy as np

def areal_og_omkrets(a,b):

    r=a/2
    
    areal_sirkel = (np.pi*r**2)/2
    omkrets_sirkel = np.pi*r

    areal_trekant = (b*a)/2
    omkrets_trekant = np.sqrt(a**2 + b**2) + b   #omkrets av lengste katet + hypotenus

    totalt_areal = areal_sirkel + areal_trekant
    total_omkrets = omkrets_sirkel + omkrets_trekant

    return totalt_areal, total_omkrets

areal, omkrets = areal_og_omkrets(3,8)

print("Totalt areal av figuren er ", round(areal,2), " og total omkrets er ", round(omkrets,2))



#Oppgave 6

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)

f = - x**2 - 5

plt.plot(x, f)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Grafen f(x) = -x**2 - 5")
plt.grid ()
plt.show()
