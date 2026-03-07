import sys
from storage import load_list, save_list

def main():
    # Ielādējam esošos datus
    items = load_list()
    
    # Pārbaudām, vai ir ievadīta komanda
    if len(sys.argv) < 2:
        print("Lietošana: python shop.py [add/list/total/clear]")
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 4:
            print("Kļūda: Norādi nosaukumu un cenu! (piem. add Maize 1.20)")
            return
        
        name = sys.argv[2]
        try:
            price = float(sys.argv[3])
            new_item = {"name": name, "price": price}
            items.append(new_item)
            save_list(items)
            print(f"✓ Pievienots: {name} ({price:.2f} EUR)")
        except ValueError:
            print("Kļūda: Cenai jābūt skaitlim!")

    elif command == "list":
        if not items:
            print("Saraksts ir tukšs.")
        else:
            print("Iepirkumu saraksts:")
            for idx, item in enumerate(items, 1):
                print(f" {idx}. {item['name']} — {item['price']:.2f} EUR")

    elif command == "total":
        total_sum = sum(item['price'] for item in items)
        print(f"Kopā: {total_sum:.2f} EUR ({len(items)} produkti)")

    elif command == "clear":
        save_list([])
        print("✓ Saraksts notīrīts.")
    
    else:
        print(f"Nezināma komanda: {command}")

if __name__ == "__main__":
    main()