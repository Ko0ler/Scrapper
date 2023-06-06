from abc import ABC
import requests as rqt
from bs4 import BeautifulSoup as Bs
from datetime import datetime

APP_NAME = 'Scrapper'
APP_VERSION = '1.0'
APP_AUTHOR = 'Mohamed Ouédraogo'
APP_DESCRIPTION = 'Extract content from a web page the easiest way !!!'
# User notes to be displayed
USER_NOTE = ['Run the executable in the folder where you want the output to be downloaded',
             'Be connected to the internet',
             'Try not to make too many requests (e.g. over 15),'
             ' as this would be unethical and may result in'
             ' server-side performance issue or even being banned',
             'Be aware that this script is still in development (kinda beta),'
             ' so you may encounter some bugs or unexpected errors',
             'Mail me at ouedraogomohamed008@gmail.com for any suggestions :)']

# Choices for extraction option
INTRO_EXTRACTION_CHOICE = ['Download source code', 'Choose a specific option']
EXTRACTION_OPTION = ['Title', 'Text', 'Link', 'Image']
HTML_TAG_VALUE = {
    'Title': 'title',
    'Text': 'p',
    'Link': 'a',
    'Image': 'img'
}

# Choices for saving format option
SAVING_FORMAT_OPTION = ['txt', 'html', 'xml']
SAVING_STYLE = 'w'  # 'w' for overwriting content in file
SAVING_FILE_NAME = 'Extracted_Content'

# Choices for ending options
ENDING_CHOICE = ['Retry', 'Quit']


class Model(ABC):
    """
    Base class for the model.
    """
    def __init__(self,
                 user_name,
                 user_email,
                 url,
                 type_of_extraction,
                 content_to_extract,
                 number_of_attempt,
                 saving_format=1):
        """
        Initialize the model.

        Args:
        - user_name (str): Name of the user.
        - user_email (str): Email of the user.
        - url (str): URL of the web page to extract data from.
        - type_of_extraction (str): Type of extraction to perform.
        - content_to_extract (str): Content to extract.
        - number_of_attempt (int): Number of attempt to extract data.
        - saving_format (str): Format to save the extracted data.
        """
        self.user_name = user_name
        self.user_email = user_email
        self.url = url
        self.type_of_extraction = type_of_extraction
        self.content_to_extract = content_to_extract
        self.saving_format = saving_format
        self.page = rqt.get(self.url)
        self.html = self.page.text
        self.soup = Bs(self.html, 'html.parser')
        self.saving_file_number = number_of_attempt
        self.extracted_data = None
        self.type_of_content_extracted = None


class Eligibility:
    def __init__(self):
        pass

    @staticmethod
    def check_for_eligibility():
        """
        Check if the user is eligible for extraction.
        This function can be customized based on eligibility criteria.
        """
        return True


class Extraction(Model):
    """
    Class responsible for extraction process.
    """
    def source_code(self):
        """
        Extract the source code from the web page.

        Returns:
        - str: Extracted source code.
        """
        self.extracted_data = self.html
        return self.extracted_data

    def content_extraction(self):
        """
        Extract the content from the web page.

        Returns:
        - str: Extracted content.
        """
        html_tag = EXTRACTION_OPTION[self.content_to_extract - 1]
        self.type_of_content_extracted = html_tag
        self.extracted_data = self.soup.find_all(f'{HTML_TAG_VALUE[html_tag]}')
        for element in self.extracted_data:
            return element

    def save_file(self):
        """
        Save the extracted content to a file.
        The file is named based on user details, extraction time, and saving format.

        Returns:
        - str: File saving confirmation message.
        """

        time_of_extraction = datetime.now()
        file_format = SAVING_FORMAT_OPTION[self.saving_format - 1]
        type_of_content_extracted, extracted_data = None, None
        if self.type_of_extraction == 1:
            type_of_content_extracted = 'Source code'
            extracted_data = self.source_code()
        elif self.type_of_extraction == 2:
            self.content_extraction()
            type_of_content_extracted = self.type_of_content_extracted
            extracted_data = self.content_extraction()
        with open(f'{SAVING_FILE_NAME}_{self.saving_file_number}.{file_format}', SAVING_STYLE) as file:
            file.write(f'Name : {self.user_name}\n'
                       f'Email : {self.user_email}\n'
                       f'Time of extraction : {time_of_extraction}\n'
                       f'URL : {self.url}\n\n\n'
                       f'Content ({type_of_content_extracted}) :\n\n\n'
                       f'{extracted_data}')
            return file
