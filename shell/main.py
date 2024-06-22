import validators

class Shell:
    Commands=[str(i) for i in range(0,9)]
    Commands.append("S")
    Commands.append("M")
    Commands.append("99")
    def __init__(self,no:int=0):
        self.help_message="""
Options:
  [1] Extract HTML Comments
      Extracts all HTML comments from the target web page. 
      HTML comments are enclosed within <!-- and -->.

  [2] Extract Meta Tags
      Extracts metadata from the target web page.
      This includes tags like <meta name="description" content="...">.

  [3] Extract URLs (Links, Images, Scripts)
      Extracts all URLs from the target web page, including:
      - Hyperlinks (<a href="...">)
      - Image sources (<img src="...">)
      - Script sources (<script src="...">)

  [4] Extract Email Addresses
      Extracts email addresses from the target web page. 
      It searches for patterns that resemble email addresses (e.g., user@example.com).

  [5] Extract Robots.txt Content
      Retrieves and displays the content of the robots.txt file from the target website.
      This file often contains rules for web crawlers about which parts of the site to avoid.

  [6] Extract URLs from Sitemap.xml
      Extracts all URLs listed in the sitemap.xml file from the target website.
      Sitemaps typically help search engines to better index a site.

  [7] Extract URLs from XML (Sitemap Schema)
      Parses any XML content conforming to the sitemap schema to extract URLs.
      Useful for custom sitemap formats or other structured XML data.

  [8] Extract WordPress Login Form Params
      Extracts the form parameters required to log in to a WordPress site.
      This includes fields like username and password input names.

  [S] Set target (URL)
      Sets the target URL for subsequent extraction operations.
      Example: "S" followed by "https://example.com".

  [M] Menu
      Displays the main menu with options to choose from.

  [0] Help
      Displays this help text, providing details about each option and how to use them.

  [99] Exit
      Exits the program.
"""
        self.menu="""
Select an option:

[1] Extract HTML Comments
[2] Extract Meta Tags
[3] Extract URLs (Links, Images, Scripts)
[4] Extract Email Addresses
[5] Extract Robots.txt Content
[6] Extract URLs from Sitemap.xml
[7] Extract URLs from XML (Sitemap Schema)
[8] Extract WordPress Login Form Params

[S] Set target (Url)
[M] Menu
[0] Help
[99] Exit

"""
        self.no=no
        self.target:str=None
        self.prompt="> "
        
    def Run(self):
        while 1:
            execute=str(input(self.prompt)).strip()
            if(execute in Shell.Commands):
                if execute == "1":
                    pass
                
                elif execute == "2":
                    pass
                
                elif execute == "3":
                    pass
                
                elif execute == "4":
                    pass
                
                elif execute == "5":
                    pass
                
                elif execute == "6":
                    pass
                
                elif execute == "7":
                    pass
                
                elif execute == "8":
                    pass
                
                elif execute == "S":
                    self.Set_Target()
                
                elif execute == "M":
                    self.Menu()
                
                elif execute == "0":
                    self.Help()
                
                elif execute == "99":
                    break
                    exit
            else:
                print("Invalid option !")

    def Set_Target(self):
        try:
            self.target:str=str(input("[*] Set Target : "))
            if validators.url(self.target):
                print(f"[+] Target is set to '{self.target}' Successfully ")
            else:
                print("[!] Target should be a URL ")
        except Exception as E:
            print(E)
    
    def Menu(self):
        print(self.menu)
    
    def Help(self):
        print(self.help_message)

if __name__=="__main__":
    Shell().Menu()
    Shell().Run()
