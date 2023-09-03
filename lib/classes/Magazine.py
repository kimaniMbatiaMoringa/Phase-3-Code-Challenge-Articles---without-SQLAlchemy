import gc

class Magazine:
    def __init__(self,name,category):
        self.name = name
        self.category = category
        self.content=[]
        self.contributing_Authors = []

    def add_content(self, article):
        self.content.append(article)

    #def __str__(self) -> str:
    #    content ="\n".join(str(item)for item in self.content)
    #    return f"Magazine Name: {self.name}, Content:{content}"

    def name(self):
        return self.name
    
    def category(self):
        return self.category
    
    def show_content(self):
        for item in self.content:
            print(item.title)

    def contributors(self):
        for item in self.contributing_Authors:
            print(item)

    def find_by_name(name):
        pass

    #for ob in gc.get_objects():
    #   if isinstance(obj, Magazine):
            

    

