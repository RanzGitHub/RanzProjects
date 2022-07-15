import wikipedia
import wikipedia as RanzWiki
while True:
    RanzWikiSearch = input("Search Your Thing")
    print("Type your search")
    RanzWikiResponse = input(RanzWiki.search(RanzWikiSearch))
    print(RanzWiki.summary(RanzWikiResponse))