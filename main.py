from dataclasses import dataclass
from datetime import datetime
import math
from matplotlib import pyplot


@dataclass
class Transaction:
    trans_date: datetime
    post_date: datetime
    vendor: str
    amount: float
    sector: str  # These are decided by discover
    category: str  # These are decided by me

    def __init__(self, trans_date, post_date, vendor, amount, sector, category):
        self.trans_date = trans_date
        self.post_date = post_date
        self.vendor = vendor
        self.amount = amount
        self.sector = sector
        self.category = category


def main():
    print('aight')
    file = open('Discover-Last12Months-20231025.csv')

    transactions = []

    firstline = False
    for line in file:
        if not firstline:
            firstline = True
            continue

        print(line)
        fields = line.strip().split(',')

        # TODO do categories here
        print(fields[0])
        t = Transaction(datetime.strptime(fields[0], '%m/%d/%Y'), datetime.strptime(fields[1], '%m/%d/%Y'), fields[2][1:-1], float(fields[3]), fields[4][1:-1], None)
        print(t)
        if "Payment" in t.sector:
            continue
        transactions.append(t)

    sectors = dict()

    for t in transactions:
        if t.sector not in sectors:
            sectors[t.sector] = t.amount
        else:
            sectors[t.sector] += t.amount

    for s in sectors.keys():
        print(s + ": " + str(sectors.get(s)))
    print('')

    fig, ax = pyplot.subplots()
    ax.pie(sectors.values(), labels=sectors.keys())

    pyplot.show()




if __name__ == "__main__":
    main()