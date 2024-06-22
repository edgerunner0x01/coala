import validators
import logging
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module_to_import')))
from zProbe.Lib.zProbe import *

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

    Commands = [str(i) for i in range(9)] + ["S", "M", "99",""]

    def __init__(self):
        """Initializes the Shell with default values and messages."""
        self.help_message = """
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
        self.menu = """
Select an option:

[1] Extract HTML Comments
[2] Extract Meta Tags
[3] Extract URLs (Links, Images, Scripts)
[4] Extract Email Addresses
[5] Extract Robots.txt Content
[6] Extract URLs from Sitemap.xml
[7] Extract URLs from XML (Sitemap Schema)
[8] Extract WordPress Login Form Params

[S] Set target (URL)
[M] Menu
[0] Help
[99] Exit

"""
        self.target = None
        self.prompt = "> "

    def Run(self):
        """Runs the shell, handling user input and directing to appropriate functions."""
        logging.info("Starting the shell.")
        while True:
            try:
                execute = input(self.prompt).strip().upper()
                if execute in Shell.Commands:
                    self.execute_command(execute)
                else:
                    print("Invalid option! Please try again.")
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                print(f"An unexpected error occurred: {e}")

    def execute_command(self, command):
        """Executes the command based on user input."""
        if command == "1":
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
        elif command == "M":
            self.Menu()
        elif command == "0":
            self.Help()
        elif command == "99":
            self.exit_shell()

    def set_target(self):
        """Sets the target URL for extraction."""
        try:
            target = input("[*] Set Target (URL): ").strip()
            if validators.url(target):
                self.target = target
                print(f"[+] Target is set to '{self.target}' successfully.")
                logging.info(f"Target set to: {self.target}")
            else:
                print("[!] Invalid URL. Please try again.")
        except Exception as e:
            logging.error(f"Failed to set target: {e}")
            print(f"An error occurred while setting the target: {e}")

    def Menu(self):
        """Displays the menu options."""
        print(self.menu)

    def Help(self):
        """Displays the help message."""
        print(self.help_message)

    def exit_shell(self):
        self.logger.info("Exiting the shell.")
        print("Exiting the program.")
        exit()

    # Methods to integrate with Target class methods

    def ensure_target_set(self):
        if not self.target:
            print("Target URL is not set. Use 'S' command to set the target.")
            self.logger.warning("Target URL is not set.")
            return False
        return True

    def extract_html_comments(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                comments, success = target.Extract_Comments()
                if success:
                    self.logger.info("Extracted HTML comments successfully.")
                    print(comments)
                else:
                    self.logger.error(f"Failed to extract HTML comments: {comments}")
            except Exception as e:
                self.logger.error(f"Exception occurred while extracting HTML comments: {e}")

    def extract_meta_tags(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                metadata, success = target.Extract_MetaData()
                if success:
                    self.logger.info("Extracted meta tags successfully.")
                    print(metadata)
                else:
                    self.logger.error(f"Failed to extract meta tags: {metadata}")
            except Exception as e:
                self.logger.error(f"Exception occurred while extracting meta tags: {e}")

    def extract_urls(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                urls, success = target.Extract_URLS()
                if success:
                    self.logger.info("Extracted URLs successfully.")
                    print(urls)
                else:
                    self.logger.error(f"Failed to extract URLs: {urls}")
            except Exception as e:
                self.logger.error(f"Exception occurred while extracting URLs: {e}")

    def extract_email_addresses(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                emails, success = target.Extract_Emails()
                if success:
                    self.logger.info("Extracted email addresses successfully.")
                    print(emails)
                else:
                    self.logger.error(f"Failed to extract email addresses: {emails}")
            except Exception as e:
                self.logger.error(f"Exception occurred while extracting email addresses: {e}")

    def extract_robots_txt(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                content, status_code, success = target.Extract_Robots()
                if success:
                    self.logger.info("Extracted robots.txt content successfully.")
                    print(content)
                else:
                    self.logger.error(f"Failed to extract robots.txt: {content}")
            except Exception as e:
                self.logger.error(f"Exception occurred while extracting robots.txt: {e}")

    def extract_urls_from_sitemap(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                urls, status_code, success = target.Extract_Sitemap()
                if success:
                    self.logger.info("Extracted URLs from sitemap.xml successfully.")
                    print(urls)
                else:
                    self.logger.error(f"Failed to extract URLs from sitemap.xml: {urls}")
            except Exception as e:
                self.logger.error(f"Exception occurred while extracting URLs from sitemap.xml: {e}")

    def extract_urls_from_xml(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                urls, status_code, success = target.Extract_XML_URLS()
                if success:
                    self.logger.info("Extracted URLs from XML content successfully.")
                    print(urls)
                else:
                    self.logger.error(f"Failed to extract URLs from XML content: {urls}")
            except Exception as e:
                self.logger.error(f"Exception occurred while extracting URLs from XML content: {e}")

    def extract_wp_login_form_params(self):
        if self.ensure_target_set():
            try:
                target = Target(self.target)
                form_params, status_code, success = target.Extract_WPLOGIN()
                if success:
                    self.logger.info("Extracted WordPress login form parameters successfully.")
                    print(form_params)
                else:
                    self.logger.error(f"Failed to extract WordPress login form parameters: {form_params}")
            except Exception as e:
                self.logger.error(f"Exception occurred while extracting WordPress login form parameters: {e}")

if __name__ == "__main__":
    shell = Shell()
    shell.Menu()
    shell.Run()
