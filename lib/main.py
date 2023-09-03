from classes.Articles import Article
from classes.Author import Authour
from classes.Magazine import Magazine

import ipdb

author1 = Authour("Kimani")
magazine1 = Magazine("Mig Planes", "Aircraft")

author1.add_article(magazine1,"Mig-21 Fishbed")
author1.add_article(magazine1,"Mig-23 Flogger")
#magazine1.add_content()



print(author1)
ipdb.set_trace()
#print(magazine1.name)

