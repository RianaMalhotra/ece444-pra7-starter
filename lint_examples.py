import os  # F401: unused import


def example():
    unused = 10  # F841: unused variable


def add_item(item, items=[]):  # B006: mutable default argument
    items.append(item)
    return items
