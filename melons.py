"""Classes for melon orders."""

import random
import datetime

class TooManyMelonsError(ValueError):
    pass

class AbstractMelonOrder:
    """ Parent class for domestic and internaional melon orders """

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

        if self.qty > 100:
            raise TooManyMelonsError("You can not order more than 100 melons")

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        total = (1 + self.tax) * self.qty * base_price

        if self.species == "Christmas":
            return total * 1.5

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        # random integer between 5-9 as the base price
        # can be modified in the future to be more complex, perhaps to depend on the weather, the day of the week
        # add an extra $4 charge to each melon ordered during morning rush hour (from 8-11am, Monday-Friday)
        # base_price = int(uniform(5, 9))
        base_price = random.randint(5, 9)

        current_hour = datetime.datetime.now().hour
        if current_hour >= 8 and current_hour <= 11:
            base_price += 4

        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08
    
    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    #     super().__init__(species, qty)
    #     self.order_type = "domestic"
    #     self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
    
    order_type = "international"
    tax = 0.17

    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes."""
    #     super().__init__(species, qty)
    #     self.country_code = country_code
    #     self.order_type = "international"
    #     self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):        
        
        if self.qty < 10:
            return super().get_total() + 3
        
        return super().get_total()


class GovernmentMelonOrder(AbstractMelonOrder):
    """A GovernmentMelonOrder melon order within the USA."""

    # def __init__(self, species, qty):
    #     """Initialize GovernmentMelonOrder melon order attributes."""

    #     super().__init__(species, qty)
    #     self.order_type = "domestic"
    #     self.passed_inspection = False
    #     self.tax = 0.0

    # def mark_inspection(self, passed):
    #     if passed == True:
    #         self.passed_inspection = True
    
    order_type = "domestic"
    tax = 0.0
    passed_inspection = False
    
    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True    

    

#  ========== driver code ============

#order0 = InternationalMelonOrder("watermelon", 6, "AUS")
#print(" new total: ", order0.get_total())

#print ("order: ", order0.country_code, order0.tax, order0.order_type)

