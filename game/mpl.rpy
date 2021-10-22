init python:
    import matplotlib.pyplot as plt

    def chartgen(price, filename):
        people = floor(20 - price)

        peepnum = [0]
        prices = [0]
        for i in range(0, people):
            peepnum.append(i)
            prices.append(price * i)
        
        plt.plot(peepnum, prices)
        plt.ylabel("Income")
        plt.xlabel("Customers")

        plt.savefig(filename + ".png")

        return filename+".png"