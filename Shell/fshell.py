from bs4 import BeautifulSoup
import validators
import logging
import sys
import os
from random import randint
from colorama import init, Fore, Back, Style
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module_to_import')))
from zProbe.Lib.zProbe import *

# Initialize colorama
init(autoreset=True)

# Configure logging
class Log:
    LOG_LEVELS = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    def __init__(self, log_method: str = "DEBUG", logger_name: str = "Shell"):
        self.logger = logging.getLogger(logger_name)
        self.configure_logging(log_method)

    def configure_logging(self, log_method: str):
        try:
            log_level = self.LOG_LEVELS.get(log_method, logging.DEBUG)
            logging.basicConfig(level=log_level,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                handlers=[
                                    logging.FileHandler("Log/Log.log"),
                                    logging.StreamHandler()
                                ])
        except Exception as e:
            self.logger.error("Error setting up logging: %s", e)

class Shell:
    """A command-line interface shell for performing various extraction tasks on a target URL."""

    Commands = [str(i) for i in range(9)] + ["S", "M", "C", "99", "" , "X"]

    def __init__(self):
        """Initializes the Shell with default values and messages."""
        self.banners = [f"""{Fore.MAGENTA}
 _______                    __
|     __|.-----.-----.----.|  |_.----.-----.
|__     ||  _  |  -__|  __||   _|   _|  -__|
|_______||   __|_____|____||____|__| |_____|
         |__|                                   
                    - https://github.com/edgerunner0x01 -{Style.RESET_ALL}"""]

        self.help_message = f"""{Fore.MAGENTA}
Options:
  {Fore.LIGHTMAGENTA_EX}[1] Extract HTML Comments{Fore.RESET}
      Extracts all HTML comments from the target web page. 
      HTML comments are enclosed within <!-- and -->.

  {Fore.LIGHTMAGENTA_EX}[2] Extract Meta Tags{Fore.RESET}
      Extracts metadata from the target web page.
      This includes tags like <meta name="description" content="...">.

  {Fore.LIGHTMAGENTA_EX}[3] Extract URLs (Links, Images, Scripts){Fore.RESET}
      Extracts all URLs from the target web page, including:
      - Hyperlinks (<a href="...">)
      - Image sources (<img src="...">)
      - Script sources (<script src="...">)

  {Fore.LIGHTMAGENTA_EX}[4] Extract Email Addresses{Fore.RESET}
      Extracts email addresses from the target web page. 
      It searches for patterns that resemble email addresses (e.g., user@example.com).

  {Fore.LIGHTMAGENTA_EX}[5] Extract Robots.txt Content{Fore.RESET}
      Retrieves and displays the content of the robots.txt file from the target website.
      This file often contains rules for web crawlers about which parts of the site to avoid.

  {Fore.LIGHTMAGENTA_EX}[6] Extract URLs from Sitemap.xml{Fore.RESET}
      Extracts all URLs listed in the sitemap.xml file from the target website.
      Sitemaps typically help search engines to better index a site.

  {Fore.LIGHTMAGENTA_EX}[7] Extract URLs from XML (Sitemap Schema){Fore.RESET}
      Parses any XML content conforming to the sitemap schema to extract URLs.
      Useful for custom sitemap formats or other structured XML data.

  {Fore.LIGHTMAGENTA_EX}[8] Extract WordPress Login Form Params{Fore.RESET}
      Extracts the form parameters required to log in to a WordPress site.
      This includes fields like username and password input names.

  {Fore.LIGHTMAGENTA_EX}[S] Set target (URL){Fore.RESET}
      Sets the target URL for subsequent extraction operations.
      Example: "S" followed by "https://example.com".

  {Fore.LIGHTMAGENTA_EX}[M] Menu{Fore.RESET}
      Displays the main menu with options to choose from.

  {Fore.LIGHTMAGENTA_EX}[0] Help{Fore.RESET}
      Displays this help text, providing details about each option and how to use them.

  {Fore.LIGHTMAGENTA_EX}[99] Exit{Fore.RESET}
      Exits the program.
{Style.RESET_ALL}
        
"""     
        self.target = None
        self.menu = f"""{Fore.MAGENTA}
# Select an option:

{Fore.LIGHTMAGENTA_EX}[1] Extract HTML Comments{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[2] Extract Meta Tags{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[3] Extract URLs (Links, Images, Scripts){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[4] Extract Email Addresses{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[5] Extract Robots.txt Content{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[6] Extract URLs from Sitemap.xml{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[7] Extract URLs from XML (Sitemap Schema){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[8] Extract WordPress Login Form Params{Fore.RESET}

{Fore.CYAN}[S] Set target (URL) [{self.target}]{Fore.RESET}
{Fore.CYAN}[X] Print target HTML Source{Fore.RESET}
{Fore.CYAN}[M] Menu{Fore.RESET}
{Fore.CYAN}[C] Clear{Fore.RESET}
{Fore.CYAN}[0] Help{Fore.RESET}
{Fore.CYAN}[99] Exit{Fore.RESET}

{Style.RESET_ALL}
"""
        self.prompt = f"{Fore.LIGHTMAGENTA_EX}> {Style.RESET_ALL}"

    def Run(self):
        """Runs the shell, handling user input and directing to appropriate functions."""
        logging.info("Starting the shell.")
        while True:
            try:
                execute = input(self.prompt).strip().upper()
                if execute in Shell.Commands:
                    self.execute_command(execute)
                else:
                    print(f"{Fore.RED}Invalid option! Please try again.{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")

    def execute_command(self, command):
        """Executes the command based on user input."""
        if command == "X":
            self.extract_source()
        elif command == "1":
            self.extract_html_comments()
        elif command == "2":
            self.extract_meta_tags()
        elif command == "3":
            self.extract_urls()
        elif command == "4":
            self.extract_email_addresses()
        elif command == "5":
            self.extract_robots_txt()
        elif command == "6":
            self.extract_urls_from_sitemap()
        elif command == "7":
            self.extract_urls_from_xml()
        elif command == "8":
            self.extract_wp_login_form_params()
        elif command == "S":
            self.set_target()
        elif command == "C":
            self.Clear()
        elif command == "M":
            self.Menu()
        elif command == "0":
            self.Help()
        elif command == "99":
            self.exit_shell()

    def set_target(self):
        """Sets the target URL for extraction."""
        try:
            target = input(f"{Fore.CYAN}[*] Set Target (URL): {Style.RESET_ALL}").strip()
            if validators.url(target):
                self.target = target
                print(f"{Fore.GREEN}[+] Target is set to '{self.target}' successfully.{Style.RESET_ALL}")
                self.menu = f"""{Fore.MAGENTA}
# Select an option:

{Fore.LIGHTMAGENTA_EX}[1] Extract HTML Comments{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[2] Extract Meta Tags{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[3] Extract URLs (Links, Images, Scripts){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[4] Extract Email Addresses{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[5] Extract Robots.txt Content{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[6] Extract URLs from Sitemap.xml{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[7] Extract URLs from XML (Sitemap Schema){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[8] Extract WordPress Login Form Params{Fore.RESET}

{Fore.CYAN}[S] Set target (URL) [{self.target}]{Fore.RESET}
{Fore.CYAN}[X] Print target HTML Source{Fore.RESET}
{Fore.CYAN}[M] Menu{Fore.RESET}
{Fore.CYAN}[C] Clear{Fore.RESET}
{Fore.CYAN}[0] Help{Fore.RESET}
{Fore.CYAN}[99] Exit{Fore.RESET}

{Style.RESET_ALL}
"""
                logging.info(f"Target set to: {self.target}")
            else:
                print(f"{Fore.RED}[!] Invalid URL. Please try again.{Style.RESET_ALL}")
        except Exception as e:
            logging.error(f"Failed to set target: {e}")
            print(f"{Fore.RED}An error occurred while setting the target: {e}{Style.RESET_ALL}")

    def Menu(self):
        """Displays the menu options."""
        print(self.menu)

    def Help(self):
        """Displays the help message."""
        print(self.help_message)

    def Banner(self):
        print(self.banners[randint(0, len(self.banners) - 1)])

    def exit_shell(self):
        logging.info("Exiting the shell.")
        print(f"{Fore.GREEN}Exiting the program.{Style.RESET_ALL}")
        exit()

    def Clear(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            logging.error(f"Exception occurred while clearing the screen: {e}")

    # Methods to integrate with Target class methods

    def ensure_target_set(self):
        if not self.target:
            print(f"{Fore.RED}Target URL is not set. Use 'S' command to set the target.{Style.RESET_ALL}")
            logging.warning("Target URL is not set.")
            return False
        return True

    def extract_html_comments(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                comments, success = target.Extract_Comments()
                if success:
                    logging.info("Extracted HTML comments successfully.")
                    print(f"{Fore.GREEN}{comments}{Style.RESET_ALL}")
                else:
                    logging.error(f"Failed to extract HTML comments: {comments}")
                    print(f"{Fore.RED}Error extracting HTML comments: {comments}{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"Exception occurred while extracting HTML comments: {e}")
                print(f"{Fore.RED}Exception occurred: {e}{Style.RESET_ALL}")

    def extract_meta_tags(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                metadata, success = target.Extract_MetaData()
                if success:
                    logging.info("Extracted meta tags successfully.")
                    print(f"{Fore.GREEN}{metadata}{Style.RESET_ALL}")
                else:
                    logging.error(f"Failed to extract meta tags: {metadata}")
                    print(f"{Fore.RED}Error extracting meta tags: {metadata}{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"Exception occurred while extracting meta tags: {e}")
                print(f"{Fore.RED}Exception occurred: {e}{Style.RESET_ALL}")

    def extract_source(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                if target.HTTP_STATUS == 200:
                    source=BeautifulSoup(target.source, 'html.parser').prettify()
                    logging.info("Extracted HTML Source successfully.")
                    print(f"{Fore.GREEN}{source}{Style.RESET_ALL}")
                else:
                    logging.error(f"Failed to extract HTML Source: {source}")
                    print(f"{Fore.RED}Error extracting HTML Source: {source}{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"Exception occurred while extracting HTML Source: {e}")
                print(f"{Fore.RED}Exception occurred: {e}{Style.RESET_ALL}")

    def extract_urls(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                urls, success = target.Extract_URLS()
                if success:
                    logging.info("Extracted URLs successfully.")
                    print(f"{Fore.GREEN}{urls}{Style.RESET_ALL}")
                else:
                    logging.error(f"Failed to extract URLs: {urls}")
                    print(f"{Fore.RED}Error extracting URLs: {urls}{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"Exception occurred while extracting URLs: {e}")
                print(f"{Fore.RED}Exception occurred: {e}{Style.RESET_ALL}")

    def extract_email_addresses(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                emails, success = target.Extract_Emails()
                if success:
                    logging.info("Extracted email addresses successfully.")
                    print(f"{Fore.GREEN}{emails}{Style.RESET_ALL}")
                else:
                    logging.error(f"Failed to extract email addresses: {emails}")
                    print(f"{Fore.RED}Error extracting email addresses: {emails}{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"Exception occurred while extracting email addresses: {e}")
                print(f"{Fore.RED}Exception occurred: {e}{Style.RESET_ALL}")

    def extract_robots_txt(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                content, status_code, success = target.Extract_Robots()
                if success:
                    logging.info("Extracted robots.txt content successfully.")
                    print(f"{Fore.GREEN}{content}{Style.RESET_ALL}")
                else:
                    logging.error(f"Failed to extract robots.txt: {content}")
                    print(f"{Fore.RED}Error extracting robots.txt: {content}{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"Exception occurred while extracting robots.txt: {e}")
                print(f"{Fore.RED}Exception occurred: {e}{Style.RESET_ALL}")

    def extract_urls_from_sitemap(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                urls, status_code, success = target.Extract_Sitemap()
                if success:
                    logging.info("Extracted URLs from sitemap.xml successfully.")
                    print(f"{Fore.GREEN}{urls}{Style.RESET_ALL}")
                else:
                    logging.error(f"Failed to extract URLs from sitemap.xml: {urls}")
                    print(f"{Fore.RED}Error extracting URLs from sitemap.xml: {urls}{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"Exception occurred while extracting URLs from sitemap.xml: {e}")
                print(f"{Fore.RED}Exception occurred: {e}{Style.RESET_ALL}")

    def extract_urls_from_xml(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                urls, status_code, success = target.Extract_XML_URLS()
                if success:
                    logging.info("Extracted URLs from XML content successfully.")
                    print(f"{Fore.GREEN}{urls}{Style.RESET_ALL}")
                else:
                    logging.error(f"Failed to extract URLs from XML content: {urls}")
                    print(f"{Fore.RED}Error extracting URLs from XML content: {urls}{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"Exception occurred while extracting URLs from XML content: {e}")
                print(f"{Fore.RED}Exception occurred: {e}{Style.RESET_ALL}")

    def extract_wp_login_form_params(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                form_params, status_code, success = target.Extract_WPLOGIN()
                if success:
                    logging.info("Extracted WordPress login form parameters successfully.")
                    print(f"{Fore.GREEN}{form_params}{Style.RESET_ALL}")
                else:
                    logging.error(f"Failed to extract WordPress login form parameters: {form_params}")
                    print(f"{Fore.RED}Error extracting WordPress login form parameters: {form_params}{Style.RESET_ALL}")
            except Exception as e:
                logging.error(f"Exception occurred while extracting WordPress login form parameters: {e}")
                print(f"{Fore.RED}Exception occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    shell = Shell()
    shell.Menu()
    shell.Run()
