def print_book_info(title, author=None, year=None):
    if author is None and year is None:
        print(f'"{title}"')
    elif author is None:
        print(f'"{title}" was written in {year}')
    elif year is None:
        print(f'"{title}" was written by {author}')
    else:
        print(f'"{title}" was written by {author} in {year}')
