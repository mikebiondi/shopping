#!python3

# Shopping list
#from tinydb import TinyDB, Query
from pdb import set_trace
from pathlib import Path
from collections import defaultdict

import sqlite3

debug = True

def initdb (conn):
	conn = sqlite3.connect('example.db')

	c = conn.cursor()
	
	c.execute (
		'''CREATE TABLE items
			(date text, 
			description text,
			qty real)
		''')
	conn.commit()


def add_an_item(conn):
  category = input("Food category: ").capitalize()
  food_item = input("Food name: ").capitalize()
  amount = int(input("Amount: "))

  conn.
  db.upsert({
    'category': category,
    'food_name': food_item,
    'amount': amount
  }, query.food_name == food_item)


def print_database(db):

  shopping = db.all()
  s_list = defaultdict(dict)

  for item in shopping:
    s_list[item['category']][item['food_name']] = item['amount']

  rows = 0
  print()

  for category in sorted(s_list):
    for item in sorted(s_list[category]):
      print(u'\u2610', "{cat:20s} :: {food:20s} -- {it:d}".format(
        cat=category, food=item, it=s_list[category][item]))
      rows = rows + 1
    print()

  if rows == 0:
    print("\n\tNothing in the database\n")


def remove_an_item(db):
  # Remove a whole category?  Or just an item?

  query = Query()

  ans = input("Remove category or item: [C, I] ")
  ans = ans.lower()

  set_trace()
  if ans[0] == 'c':
    print("Remove category:")
    print("I know these categories:")

    c_list = defaultdict(dict)

    shopping = db.all()
    for item in shopping:
      c_list[item['category']] = c_list[item['category']] + 1

    for item in c_list:
      print("\t{item:s}".format(item))

    cat_to_remove = input("Remove which category: ")

    res = db.search(query.category == category)
    set_trace()
    res = db.remove(query.category == category)

  elif ans[0] == 'i':
    item = input("Enter item to remove: ")
    res = db.remove(query.item == item)

    if res:
      print(res)


def main():
  database = './shopping.db'
  
  
  my_database = Path(database)

  if not my_database.is_file():
    db = TinyDB(database)
    db.purge()

  else:
    db = TinyDB(database)

  while True:
    menu = input("print, add, delete, exit: ")
    menu = menu.lower()

    if menu[0] == "p":
      #Print
      print_database(db)

    elif menu[0] == "a":
      # Add item
      add_an_item(db)

    elif menu[0] == "d":
      # Delete item
      remove_an_item(db)

    elif menu[0] == "e":
      sys.exit()
    else:
      print("I don't know that option\n")


main()

