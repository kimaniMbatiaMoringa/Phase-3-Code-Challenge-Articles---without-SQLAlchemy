from classes.Articles import Article
from classes.Author import Authour
from classes.Magazine import Magazine

import ipdb

author1 = Authour("Kimani")
magazine1 = Magazine("Mig Planes", "Aircraft")

author1.add_article("Mig-29 Foxhound", magazine1)
author1.add_article("Mig-23 Flogger", magazine1)

#ipdb.set_trace()

print(author1)
print(magazine1.name)
print(author1.articles_created)

