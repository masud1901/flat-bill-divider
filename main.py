from bill import Bill
from flatmate import Flatmate
from pdfReport import PdfReport

amount = int(input("The total amount of the bill: "))
period = str(input("The period of the bill: i.e. December 2020: "))

bill = Bill(amount, period)

no_of_flatmates = int(input("The number of flatmates: "))
flatmates = []
total_days_staying = 0

for i in range(1, no_of_flatmates + 1):
    name = input(f"Name of flatmate {i}: ")
    days_in_house = int(input(f"Days stayed by {name} (should be smaller than 30): "))
    flatmate = Flatmate(name, days_in_house)
    flatmates.append(flatmate)
    total_days_staying += days_in_house


rest_of_the_days = 30 - days_in_house
if rest_of_the_days < 0:
    rest_of_the_days = 0

for flatmate in flatmates:
    bill = flatmate.pays(bill, no_of_flatmates, total_days_staying, rest_of_the_days)
    total
    print(f"{flatmate.name} pays: {bill}")
