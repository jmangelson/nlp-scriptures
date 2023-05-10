import numpy as np
import pandas as pd

scrips = pd.read_csv("lds-scriptures.csv")
book_names = scrips.book_title.unique()

books = {}
for book_name in book_names:
    book_verses = scrips.loc[scrips['book_title'] == book_name]
    full_book_text = ''.join(book_verses.scripture_text)
    books[book_name] = full_book_text

full_standard_works = ''.join(books.values())
