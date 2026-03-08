def calc_line_total(item):
    """Aprēķina summu vienai rindiņai (daudzums * cena)."""
    return item['qty'] * item['price']

def calc_grand_total(items):
    """Aprēķina kopējo summu visam sarakstam."""
    return sum(calc_line_total(item) for item in items)

def count_units(items):
    """Saskaita kopējo vienību (preču gabalu) skaitu."""
    return sum(item['qty'] for item in items)