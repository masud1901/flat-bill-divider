import bill


class Flatmate:
    """Creates a flatmate person who lives in the
    flat and pays a share of bill"""

    def __init__(self, name: str, days_in_house: int) -> None:
        self.name = name
        self.days_in_house = days_in_house
        self.payment = 0

    def pays(self, bill: bill.Bill, number_of_flatmates: int, total_days: int) -> float:
        """Calculates how much each flatmate pays"""
        weight = self.days_in_house / total_days
        payment = bill.amount * weight
        individual_share = payment / number_of_flatmates
        self.payment = individual_share
        return round(individual_share, ndigits=2)
