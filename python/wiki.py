import wikipedia as wk

# print(wk.summary("Cats"))
search = wk.search("Cat", results=10, suggestion=False)
for page in search:
    try:
        query = wk.page(page, auto_suggest=False)
        print(query.url)
        print(query.title)
        # print(query.content)
    except wk.exceptions.DisambiguationError as e:
        # print(e.options)
        print("Error: DisambiguationError")
        continue

