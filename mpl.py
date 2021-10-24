import matplotlib.pyplot as plt
import numpy as np
import math

def chartgen(price, filename):
    people = math.floor(20 - price)
    if people < 1:
        people = 1

    peepnum = [0]
    prices = [0]
    for i in range(0, people):
        peepnum.append(i)
        prices.append(price * i)
        
    plt.plot(peepnum, prices)
    plt.ylabel("Income")
    plt.xlabel("Customers")

    plt.figure().set_figwidth(20)
    plt.figure().set_figheight(20)
    print("People: " + str(people))
    print("prices: " + str(prices))

    plt.savefig(filename + ".png")
    plt.show()

for i in [0.25, 0.50, 0.75, 1, 1.50, 2, 300]:
    chartgen(i, "file" + str(i))
