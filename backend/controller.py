import time

from .model import APP_NAME,\
    APP_VERSION,\
    APP_AUTHOR,\
    APP_DESCRIPTION,\
    Eligibility,\
    Extraction,\
    USER_NOTE,\
    INTRO_EXTRACTION_CHOICE,\
    EXTRACTION_OPTION,\
    SAVING_FORMAT_OPTION,\
    ENDING_CHOICE
from .view import Home, UserData, DataProcess, EndOfProcess, show_input_error
from .exceptions import InvalidInputError, InvalidChoiceError


def user_choice_validation(usable_option_length):
    """
    Decorator to validate user choice.

    Args:
    - usable_option_length (list): List of usable option length.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    input_to_validate = func(*args, **kwargs)
                    input_starting_value = 1
                    input_ending_value = len(usable_option_length)
                    if input_to_validate == '':
                        raise InvalidChoiceError('\n> Empty value is not allowed.')
                    elif not input_to_validate.isnumeric():
                        raise InvalidChoiceError('\n> Please enter a number.')
                    elif not input_starting_value <= int(input_to_validate) <= input_ending_value:
                        raise InvalidChoiceError(f'\n> Please enter a number between'
                                                 f' {input_starting_value} and {input_ending_value}.')
                    return int(input_to_validate)
                except InvalidChoiceError as e:
                    show_input_error(e)
                    continue

        return wrapper

    return decorator


def user_input_validation(input_type=None):
    """
    Decorator to validate user input.

    Args:
    - input_type (str): Type of input to validate.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    input_to_validate = func(*args, **kwargs)
                    if input_to_validate == '':
                        raise InvalidInputError('\n> Empty value is not allowed.')
                    elif input_type == 'email':
                        if '@' not in input_to_validate:
                            raise InvalidInputError('\n> Please enter a valid email address.')
                    elif input_type == 'url':
                        if 'http' not in input_to_validate:
                            raise InvalidInputError('\n> Please enter a valid URL.')
                    return input_to_validate
                except InvalidInputError as e:
                    show_input_error(e)
                    continue

        return wrapper

    return decorator


class Control:
    """
    Base class for the controller.
    """
    def __init__(self):
        """
        Initialize the controller.

        Attributes:
        - user_name (str): Name of the user.
        - user_email (str): Email of the user.
        - type_of_extraction (str): Type of extraction to perform.
        - content_to_extract (str): Content to extract.
        - url (str): URL of the web page to extract data from.
        - saving_format (str): Format to save the extracted data.
        - extracted_data (str): Extracted data.
        - number_of_attempt (int): Number of attempt to extract data.
        - view_home (Home): Home view.
        - view_data (UserData): UserData view.
        - view_process (DataProcess): DataProcess view.
        - view_end (EndOfProcess): EndOfProcess view.
        """
        self.user_name = None
        self.user_email = None
        self.type_of_extraction = None
        self.content_to_extract = 1
        self.url = None
        self.saving_format = None
        self.extracted_data = None
        self.number_of_attempt = 1
        self.view_home = Home(USER_NOTE, INTRO_EXTRACTION_CHOICE, EXTRACTION_OPTION)
        self.view_data = UserData(SAVING_FORMAT_OPTION)
        self.view_process = DataProcess()
        self.view_end = EndOfProcess(self.number_of_attempt, ENDING_CHOICE)

    def intro(self):
        """
        Display the intro message.
        """
        self.view_home.intro(APP_NAME, APP_VERSION, APP_AUTHOR, APP_DESCRIPTION)

        @user_input_validation()
        def get_user_name():
            return self.view_data.user_name()

        self.user_name = get_user_name()

        @user_input_validation('email')
        def get_user_email():
            return self.view_data.user_email()

        self.user_email = get_user_email()

    def get_url(self):
        # Get URL
        @user_input_validation('url')
        def get_url():
            return self.view_data.url()

        self.url = get_url()
        return self.url

    def get_type_of_extraction(self):
        # Get type of extraction
        @user_choice_validation(INTRO_EXTRACTION_CHOICE)
        def get_type_of_extraction():
            return self.view_home.choose_type_of_extraction()

        self.type_of_extraction = get_type_of_extraction()
        return self.type_of_extraction

    def get_content_to_extract(self):
        @user_choice_validation(EXTRACTION_OPTION)
        def get_content_to_extract():
            return self.view_home.extraction_options()

        self.content_to_extract = get_content_to_extract()
        return self.content_to_extract

    def get_source_code(self):
        """
        Perform source code extraction based on the given type of extraction.

        Return:
        - str: Extracted source code.
        """
        content_extracted = self.extraction()
        self.extracted_data = content_extracted.source_code()
        return self.extracted_data

    def get_web_content(self):
        """
        Perform web content extraction based on the given type of extraction.

        Return:
        - str: Extracted web content.
        """
        content_extracted = self.extraction()
        self.extracted_data = content_extracted.content_extraction()
        return self.extracted_data

    def get_saving_format(self):
        @user_choice_validation(SAVING_FORMAT_OPTION)
        def get_saving_format():
            return self.view_data.save_method()

        self.saving_format = get_saving_format()
        return self.saving_format

    def extraction(self):
        """
        Perform extraction based on the data given by the user.

        Return:
        - Extraction: Extraction object.
        """
        return Extraction(self.user_name,
                          self.user_email,
                          self.url,
                          self.type_of_extraction,
                          self.content_to_extract,
                          self.number_of_attempt,
                          self.saving_format)

    def extraction_process(self):
        """
        Perform the overall extraction process.
        """
        # Get extraction data
        self.view_data.prompt_to_enter_extraction_data()
        self.get_url()
        self.get_type_of_extraction()
        # Check eligibility
        eligible = Eligibility.check_for_eligibility()
        if not eligible:
            self.view_process.not_eligible()
        elif eligible:
            self.view_process.eligible()
            # Get saving format and process the extraction
            if self.type_of_extraction == 1:
                self.get_saving_format()
                self.extracted_data = self.get_source_code()
            elif self.type_of_extraction == 2:
                self.get_content_to_extract()
                self.get_saving_format()
                self.extracted_data = self.get_web_content()
            # Output the extraction content
            self.view_process.extraction_is_processing()
            time.sleep(1.5)
            self.view_process.extraction_output(self.extracted_data)
            self.view_end.number_of_attempt(self.number_of_attempt)
            # Save file
            self.extraction().save_file()
        # Retry extraction process
        self.retry_or_quit()

    def retry_or_quit(self):
        """
        Ask the user if they want to retry the extraction process or quit the program.
        """

        @user_choice_validation(ENDING_CHOICE)
        def get_user_choice():
            return self.view_end.retry_or_quit()

        user_choice = get_user_choice()

        if user_choice == 1:
            self.number_of_attempt += 1
            self.extraction_process()
        elif user_choice == 2:
            self.view_end.quit()

    def run(self):
        """
        Run the program.
        """
        self.intro()
        self.extraction_process()
