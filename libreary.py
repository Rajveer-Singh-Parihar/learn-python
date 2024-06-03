class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

        def addbook(self ,book):
            self.books.append(book)
            self.nobooks = len(self.books)
            def showinfo(self):
                print(f"the library has{self.nobooks} books. the books are")
                for book in self.books:
                    print(book)

                l1 = library()
                l1.addbook("harry potter1")
                l1.addbook("twinkling star")
                l1.addbook("forest of glimpsip")
                l1.addbook("the software developer")
