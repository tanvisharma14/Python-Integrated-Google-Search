from googlesearch import search as s

keyword = input("Enter your query: ")
result = s(keyword, 10)
for i in result:
    print(i)
