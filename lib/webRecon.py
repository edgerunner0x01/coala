from bs4 import BeautifulSoup , Comment
import requests 
import re
from typing import Union , List , Tuple , Dict
DEFAULT_HEADERS: Dict[str,str] ={
        "Accept": "xml,*/*" ,
         "Accept-Language":"en-US,en",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }

class Target:
    def __init__(self,url:str,headers: Dict[str,str]=DEFAULT_HEADERS) :
        self.url:str = rf'{url}'
        self.headers=headers
        self.HTTP_STATUS:None=None
        try:
            req=requests.get(self.url,headers=headers)
            self.HTTP_STATUS:int=req.status_code
            if self.HTTP_STATUS == 200:
                self.source=req.text
        except Exception as E:
            exit

    def Extract_Comments(self) -> Union[ Tuple[List,bool] , Tuple[str,bool] ]:
        try:
            soup=BeautifulSoup(self.source,'html.parser')
            extracted_comments = soup.find_all(string=lambda text: isinstance(text, Comment))
            comments=[]
            for comment in extracted_comments:
                comments.append(str(comment.extract()))
            return True,comments # RETURNS TRUE OR FLASE BASED OF THE HTTP STATUS CODE 
        except Exception as E:   # ALONG WITH THE COMMENTS IF THERE IS ANY OR THE ERROR MSG 
            return False,E
    
    def Extract_Emails(self) -> Union[ Tuple[List,bool] , Tuple[str,bool] ] :
        try:
            email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')
            email_matches = re.findall(email_pattern, self.source)
            return True,email_matches  # RETURNS TRUE OR FLASE BASED OF THE HTTP STATUS CODE 
        except Exception as E:         # ALONG WITH THE EMAILS IF THERE IS ANY OR THE ERROR MSG 
            return False,E

    def Extract_Robots(self)  -> Union[ Tuple[str,int,bool] , Tuple[str,bool ] ]: 
        def filter(url:str) -> str:
            if url[len(url)-1] == "/":
                return url[:len(url)-1]
            else:
                return url
        try:
            req=requests.get(f"{filter(self.url)}/robots.txt",headers=self.headers)
            status_code=req.status_code
            if int(status_code) == 200:
                return True,int(status_code),str(req.text) # RETURNS TRUE OR FLASE BASED OF THE HTTP STATUS CODE 
            else:                                           # ALONG WITH THE HTTP STATUS CODE 
                return False,int(status_code),""            # AND THE ROBOTS.TXT CONTENT IF THERE IS ANY
        except Exception as E:
            return False,str(E)

    def Extract_Sitemap(self)  -> Union[ Tuple[str,int,bool] , Tuple[str,bool ] ]: 
        def filter(url:str) -> str:
            if url[len(url)-1] == "/":
                return url[:len(url)-1]
            else:
                return url
        try:
            req=requests.get(f"{filter(self.url)}/sitemap.xml",headers=self.headers)
            status_code=req.status_code
            if int(status_code) == 200:
                return True,int(status_code),str(req.text)
            else:
                return False,int(status_code),""
        except Exception as E:
            return False,str(E)
        
# UPDATE THE HTTPS BUG 