
from classes.Articles import Article
from classes.Magazine import Magazine

class Authour:
    def __init__(self,name):
        self.name = name
        self.articles = []

    def name(self):
        return self.name
    
    def add_article(self,title,magazine):
        #magazine = Magazine(magazine,category)           #Creates a magazine for the article
        article = Article(title,self,magazine)
        self.articles.append(article.title)
        magazine
        return article

    def __str__(self) -> str:
        #articles_written = [print(article) for article in self.articles]
        articles_written ="\n".join(str(book)for book in self.articles)
        return f"Name: {self.name}, Articles:{articles_written}"
