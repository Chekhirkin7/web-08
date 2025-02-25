from mongoengine import connect
from models import Quote, Author

connect(db='homework_08',
        host='mongodb+srv://user_hw_08:567234@cluster0.p4i2j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


def search_by_name(name):
    author = Author.objects(fullname__iregex=name).first()
    result = []
    if not author:
        print(f'Author with name {name} not exist.')
    quotes = Quote.objects(author=author)
    if quotes:
        result = [q.quote for q in quotes]
    else:
        print(f'No quotes found for author {name}.')
    return result


def search_by_tag(tag):
    quotes = Quote.objects(tags__iregex=tag)
    result = []
    if quotes:
        result = [q.quote for q in quotes]
    else:
        print(f'No quotes found with tag {tag}.')
    return result


def search_by_tags(tags):
    tag_list = [tag.strip() for tag in tags.split(',')]
    quotes = Quote.objects(tags__in=tag_list)
    result = []
    if quotes:
        result = [q.quote for q in quotes]
    else:
        print(f'No quotes found with tag {tag_list}.')
    return result


def main():
    while True:
        command = input('Enter command (name: name | tag: tag | tags: tags | exit): ').strip()

        if command.lower() == 'exit':
            return "Exit the program"
        elif command.startswith('name:'):
            name = command[5:].strip()
            print(search_by_name(name))
        elif command.startswith('tag:'):
            tag = command[4:].strip()
            print(search_by_tag(tag))
        elif command.startswith('tags:'):
            tags = command[5:].strip()
            print(search_by_tags(tags))
        else:
            print('Invalid command. Please try again.')


if __name__ == '__main__':
    main()
