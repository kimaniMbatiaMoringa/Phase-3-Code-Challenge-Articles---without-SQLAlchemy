class Article:
    def __init__(self, author ,magazine ,title):
        self.title = title
        self.author = author
        self.magazine = magazine
    
    def __str__(self) -> str:       #Returns the string representation of that object
        return f"Article Name : {self.title}, Author: {self.author}"

    def author(self):
        return self.author
    
    def magazine(self):
        return self.magazine