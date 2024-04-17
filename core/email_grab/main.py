import re 
from requests import get
import sys
URL:str=sys.argv[1]
def main():
    try:
        source=get(rf"{URL}").text
        email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')
        email_matches = re.findall(email_pattern, source)
        for email in email_matches:
            print(str(email))
    except Exception as E:
        print(E)
if __name__=="__main__":
    main()