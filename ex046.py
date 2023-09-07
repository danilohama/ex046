""" Faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles!
"""
from time import sleep

for count in range(10, -1, -1):
    sleep(1)
    print(count)
sleep(1)
print('buuuum 🎆! buUUUM🎆! POOOOOW🎆!')
