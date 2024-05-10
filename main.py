import datetime
import calendar
from bill import Bill
from flatmate import Flatmate
from pdfReport import PdfReport


def get_num_days_in_month(period):
    period_parts = period.split()
    year = int(period_parts[1])
    month = datetime.datetime.strptime(period_parts[0], "%B").month
    return calendar.monthrange(year, month)[1]


def main():
    amount = int(input("The total amount of the bill: "))
    period = str(input("The period of the bill: i.e. December 2020: "))
    no_of_flatmates = int(input("The number of flatmates: "))
    flatmates = []
    total_days_staying = 0

    for i in range(1, no_of_flatmates + 1):
        name = input(f"Name of flatmate {i}: ")
        days_in_house = int(
            input(f"Days stayed by {name} (should be smaller than 30): ")
        )
        flatmate = Flatmate(name, days_in_house)
        flatmates.append(flatmate)
        total_days_staying += days_in_house

    bill = Bill(amount, period)

    for flatmate in flatmates:
        print(
            f"{flatmate.name} pays: {flatmate.pays(bill=bill, number_of_flatmates=no_of_flatmates, total_days=total_days_staying)}"
        )

    pdf_report = PdfReport(filename=f"{bill.period}.pdf")
    pdf_report.generate(flatmates, bill)


if __name__ == "__main__":
    main()
