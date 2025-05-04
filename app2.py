#!/usr/bin/env python3
import sqlite3

# Establish a connection to the SQLite database
# The database file (data.db) will be created automatically

def get_connection():
    return sqlite3.connect("data.db")

# Create the items table if it doesn't already exist

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            qty   INTEGER NOT NULL
        );
    """
    )
    conn.commit()
    conn.close()

# Create: Add a new item to the database

def add_item(name: str, qty: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, qty) VALUES (?, ?);",
        (name, qty)
    )
    conn.commit()
    conn.close()

# Read: Retrieve all items from the database

def list_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, qty FROM items;")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update: Modify an existing item by ID

def update_item(item_id: int, new_name: str, new_qty: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE items
        SET name = ?, qty = ?
        WHERE id = ?;
        """,
        (new_name, new_qty, item_id)
    )
    conn.commit()
    conn.close()

# Delete: Remove an item by ID

def delete_item(item_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?;", (item_id,))
    conn.commit()
    conn.close()

# Simple text-based menu for user interaction

def menu():
    while True:
        print("""
=== ITEM INVENTORY ===
1. Add item
2. List items
3. Update item
4. Delete item
5. Exit
""")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ")
            qty  = int(input("Quantity: "))
            add_item(name, qty)
            print("✔️ Item added.")

        elif choice == "2":
            items = list_items()
            if not items:
                print("No items found.")
            else:
                for id, name, qty in items:
                    print(f"{id}: {name} (qty {qty})")

        elif choice == "3":
            item_id = int(input("Item ID to update: "))
            name    = input("New name: ")
            qty     = int(input("New quantity: "))
            update_item(item_id, name, qty)
            print("✔️ Item updated.")

        elif choice == "4":
            item_id = int(input("Item ID to delete: "))
            delete_item(item_id)
            print("✔️ Item deleted.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

# Entry point: initialize database and launch menu

if __name__ == "__main__":
    initialize_db()
    menu()