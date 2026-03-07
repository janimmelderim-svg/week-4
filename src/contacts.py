import json
import os
import sys

# Definējam faila nosaukumu kā konstanti
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Ielādē kontaktus no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_contacts(contacts):
    """Saglabā kontaktu sarakstu JSON failā."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

def add_contact(name, phone):
    """Pievieno jaunu kontaktu un saglabā failā."""
    contacts = load_contacts()
    new_contact = {"name": name, "phone": phone}
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"✅ Kontakts '{name}' pievienots!")

def list_contacts():
    """Izvada visus saglabātos kontaktus."""
    contacts = load_contacts()
    if not contacts:
        print("📭 Kontaktu saraksts ir tukšs.")
        return

    print(f"\n--- Kontaktu saraksts ({len(contacts)}) ---")
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c['name']}: {c['phone']}")

def search_contacts(query):
    """Meklē kontaktus pēc vārda daļas (case-insensitive)."""
    contacts = load_contacts()
    results = [c for c in contacts if query.lower() in c['name'].lower()]

    if not results:
        print(f"🔍 Nekas netika atrasts pēc pieprasījuma: '{query}'")
    else:
        print(f"\n--- Meklēšanas rezultāti ({len(results)}) ---")
        for c in results:
            print(f"👤 {c['name']}: {c['phone']}")

def main():
    """Galvenā loģika komandrindas argumentu apstrādei."""
    if len(sys.argv) < 2:
        print("Lietošana: python contacts.py [add|list|search] [parametri]")
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) == 4:
        name = sys.argv[2]
        phone = sys.argv[3]
        add_contact(name, phone)
    
    elif command == "list":
        list_contacts()
    
    elif command == "search" and len(sys.argv) == 3:
        query = sys.argv[2]
        search_contacts(query)
    
    else:
        print("Nepareiza komanda vai argumentu skaits.")

if __name__ == "__main__":
    main()