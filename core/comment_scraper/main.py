from bs4 import BeautifulSoup
from bs4 import Comment
import requests
import sys
URL : str = sys.argv[1]
def main():
    try:
        source=requests.get(URL).text
        soup=BeautifulSoup(source,'html.parser')
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        print("====== "+f"COMMENTS for [{URL}]"+" ======")
        for c in comments:
            print("#",c)
            c.extract()
        print("\n")
    except:
        pass
if __name__=="__main__":
    main()
    