class LibraryItems:
       def __init__(self, title, year):
         self.id = None
         self.title = title
         self.year = year
       def bookDetails(self):
            return "The Book details are found"
class Book(LibraryItems):
    def __init__(self, title, year, author):
        self.author = author
        LibraryItems.__init__(self, title, year)

class Magazine(LibraryItems):
    def __init__(self, title, year, issue):
        self.issue = issue
        LibraryItems.__init__(self, title, year)
                 
#obj = Magazine(123, "sonaversity", 2000, 23)
obj = Magazine("Economics", 2000, 23)
obj.id = 7
print(obj.bookDetails())
print(obj.id)
