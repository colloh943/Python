# list uses squire brackets
employees = ['John','Smith','Andrew','Jane']
print(employees)
print(employees[2])
print(employees[1:3])
employees[3] = 'Reuben'
print(employees)
employees.append('stephen')
print(employees)
employees.extend(['Paul','Erick','Tom'])
print(employees)
# turple normal brackets
products = ('apple','banana','orange','strawberry')
print(products)
print(products[2])
print(products[2:4])
# product[0]='mango'
print(products)
# set
students = {'Peter','Esther','Ann','oduor'}
print(students)
students.add('Dennis')
print(students)
students.remove('Ann')
print(students)
students.update(['Kimani'])
print(students)
students.update(['Sammy','Goddo'])
print(students)
# dictionary
book ={'titl' :'Book Title',
       'author' : 'SUMMIDO',
       'publisher' : 'KLB',
       }
print(book)
book['year published'] = 1967
print(book)
print(book['author'])
print(book['publisher'])
# print(book['title'])
print(book['year published'])
if 'author' in book:
       print('author is in the book')
else:
       print('author is not present')

if 'title' in book:
              print('title is in the book')
else:
              print('title is not present')



book = {'title':'book title',
        'author':'kiptoo',
        'year':'2136',
        'pages':'21236',}
if 'title' in book:
       print('title is in the book')
else:
       print('title is not in the book')
