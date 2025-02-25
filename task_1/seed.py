import json
from mongoengine.errors import NotUniqueError
from models import Author, Quote

if __name__ == '__main__':
    with open('authors.json', 'r') as f:
        data = json.load(f)
        for el in data:
            try:
                author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'),
                                born_location=el.get('born_location'), description=el.get('description'))
                author.save()
            except NotUniqueError:
                print(f'Author with fullname {el.get("fullname")} already exists in the database.')

    with open('quotes.json', 'r') as f:
        data = json.load(f)
        for el in data:
            author, *_ = Author.objects(fullname=el.get('author'))
            quote = Quote(tags=el.get('tags'), author=author, quote=el.get('quote'))
            quote.save()