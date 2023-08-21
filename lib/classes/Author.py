import Articles
import Magazine

class Authour:
    def __init__(self,name):
        self.name=name
        self.article=[]

    def name(self):
        return self.name
    
    def add_article(self,magazine, title):
        self.article.append(magazine)

