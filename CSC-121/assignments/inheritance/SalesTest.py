# Filename: SalesTest.py
# Author: Joel Hubbard
# Date: 17.11.2021

from Sale import *

book = Sale('eragon', 15)
game = Sale('Skyrim', 40)
print(book)
print(game)
Sale.setName(book, 'eldest')
Sale.setPrice(game, 20)
print(book)
print(game)
print(book.getName())
print(book.getPrice())
print(game.getName())
print(game.getPrice())

