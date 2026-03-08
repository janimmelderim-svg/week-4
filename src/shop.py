import sys
from storage import load_list, save_list
from utils import calc_line_total, calc_grand_total, count_units

def main():
    args = sys.argv[1:]
    if not args:
        print("Komandas: add <nosaukums> <daudzums> <cena>, list, total, clear")
        return

    command = args[0].lower()
    shopping_list = load_list()

    if command == "add":
        # Pārbaude: vai ir pietiekami daudz argumentu?
        if len(args) < 4:
            print("Kļūda: Jānorāda nosaukums, daudzums un cena (piem., add Maize 3 1.20)")
            return
        
        name = args[1]
        try:
            qty = int(args[2])
            price = float(args[3].replace(',', '.'))
            
            if qty <= 0 or price < 0:
                print("Kļūda: Daudzumam un cenai jābūt pozitīviem skaitļiem!")
                return

            new_item = {"name": name, "qty": qty, "price": price}
            shopping_list.append(new_item)
            save_list(shopping_list)
            
            line_total = calc_line_total(new_item)
            print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.)")
            print(f"= {line_total:.2f} EUR")
            
        except ValueError:
            print("Kļūda: Daudzumam jābūt veselam skaitlim, cenai – skaitlim!")

    elif command == "list":
        if not shopping_list:
            print("Saraksts ir tukšs.")
        else:
            print("Iepirkumu saraksts:")
            for i, item in enumerate(shopping_list, 1):
                line_total = calc_line_total(item)
                print(f" {i}. {item['name']} × {item['qty']} — {item['price']:.2f} EUR/gab. — {line_total:.2f} EUR")

    elif command == "total":
        total_price = calc_grand_total(shopping_list)
        total_units = count_units(shopping_list)
        print(f"Kopā: {total_price:.2f} EUR ({total_units} vienības, {len(shopping_list)} produkti)")

    elif command == "clear":
        save_list([])
        print("✓ Saraksts ir notīrīts.")

if __name__ == "__main__":
    main()