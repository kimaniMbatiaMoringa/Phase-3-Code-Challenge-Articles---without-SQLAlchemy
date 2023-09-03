from classes.Articles import Article
from classes.Magazine import Magazine

class Authour:
    def __init__(self,name):
        self.name = name
        self.works = []
        self.magazine_works=[]

    def name(self):
        return self.name
    
    def add_article(self,magazine,title):
        #magazine = Magazine(magazine,category)             #Creates a magazine for the article
        # order of creation: author ,magazine ,title
        article = Article(self.name,magazine,title)      #Creates a new Article Object
        self.works.append(article)                       #Adds the title of the Article created to a list called
        magazine.add_content(article)

        if magazine not in self.magazine_works:
            self.magazine_works.append(magazine)
        
    
        if self.name not in magazine.contributing_Authors:
            magazine.contributing_Authors.append(self.name)

        return article
    def articles(self):
        print("Articles written:")
        for items in self.works:
            print("\n" + items.title) 

    def magazines(self):
        print("Magazines contributed to")
        for item in self.magazine_works:
            print(item.name)



    def __str__(self) -> str:
        #articles_written = [print(article.title) for article in self.articles]
        articles_written ="\n".join(str(article)for article in self.works)
        return f"Name: {self.name}, Articles:{articles_written}"

