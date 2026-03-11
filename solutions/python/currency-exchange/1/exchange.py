"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """

    :param budget: float(127.5)
    :param exchange_rate: float (1.2)
    :return: budget / echange_rate
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float(127.5)
    :param exchanging_value: float(120.0)
    :return: budget - exchange_value
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int(5)
    :param number_of_bills: int(128)
    :return:denomination * number_of_bills
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """

    :param amount: float(127.5)
    :param denomination: int(5)
    :return: amount // denomination
    """

    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float(127.5)
    :param denomination: int(20)
    :return: amount % denomination
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float(127.25)
    :param exchange_rate: float(1.20)
    :param spread: int(10)
    :param denomination: int(20)
    :return: int
    """
    actual_rate = exchange_rate * (1 + spread / 100)
    exchanged = budget / actual_rate
    return int(get_number_of_bills(exchanged, denomination) * denomination)
