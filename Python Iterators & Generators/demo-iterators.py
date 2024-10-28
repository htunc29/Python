import math
sayilar=[12,45,67,98]


def my_for(iterable,fnc):
    iterator=iter(iterable)
    while True:
        try:
            sayi=next(iterator)
            fnc(sayi)
        except StopIteration:
            break


my_for(sayilar,print)