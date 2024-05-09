import bill


class Flatmate:
    """Creates a flatmate person who lives in the flat and pays a share of bill"""

    def __init__(self, name: str, days_in_house: int) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: bill.Bill, number_of_flatmates: int, total_days: int,rest_of_the_days:int) -> float:
        """Calculates how much each flatmate pays"""
        weight = self.days_in_house / total_days
        bill = bill.amount * weight / number_of_flatmates
        final_bill = bill + rest_of_the_days * bill / 30
        
        return round(final_bill, ndigits=2)
