# Console interaction for now ...
# Gonna think about creating GUI

def show_input_error(error):
    """
    Display an input error message.

    Args:
    - error (str): Error message to be displayed.
    """
    print(f'\nInput error: {error}')


def print_options_list(methods):
    """
    Print a numbered list of options.

    Args:
    - methods (list): List of options to be displayed.
    """
    for index, method in enumerate(methods):
        print(f'{index + 1}. {method}')


class Home:
    def __init__(self, requirement, intro_options_list, extraction_options_list):
        """
        Initialize the Home view with requirements and options lists.

        Args:
        - requirement (list): List of requirements to be displayed.
        - intro_options_list (list): List of options for the introductory step.
        - extraction_options_list (list): List of extraction options.
        """
        self.requirement = requirement
        self.intro_options_list = intro_options_list
        self.extraction_options_list = extraction_options_list

    def intro(self, app_name, app_version, app_author, app_description):
        """
        Display the introduction screen.
        """
        print(f'\n\nWelcome to {app_name} {app_version}\n'
              f'Created by {app_author}\n'
              f'\n{app_description}\n')
        print('\nMake sure to:')
        print_options_list(self.requirement)
        print('\nPlease provide necessary information about yourself before proceeding with the extraction')

    def choose_type_of_extraction(self):
        """
        Prompt the user to choose the type of extraction process.

        Returns:
        - str: Selected extraction option index.
        """
        print('\nWhich process do you prefer?\n')
        print_options_list(self.intro_options_list)
        return input('\nChoose an option: ')

    def extraction_options(self):
        """
        Display the extraction options to the user.

        Returns:
        - str: Selected extraction option index.
        """
        print('\nHere is a list of options for extracting websites:\n')
        print_options_list(self.extraction_options_list)
        return input('\nChoose an option: ')


class UserData:
    def __init__(self, options_list):
        """
        Initialize the UserData view with options list.

        Args:
        - options_list (list): List of options for user input.
        """
        self.options_list = options_list

    def prompt_to_enter_extraction_data(self):
        """
        Display the message to enter extraction data.
        """
        print('\nEnter the necessary data for extraction')

    def user_name(self):
        """
        Prompt the user to enter their name.

        Returns:
        - str: User name.
        """
        return input('\nYour name: ')

    def user_email(self):
        """
        Prompt the user to enter their email address.

        Returns:
        - str: User email.
        """
        return input('\nYour email address: ')

    def url(self):
        """
        Prompt the user to enter the target URL.

        Returns:
        - str: Target URL.
        """
        return input('\nTarget URL (Provide the absolute value)'
                     '\nFor example: https://example.com\n> ')

    def save_method(self):
        """
        Prompt the user to choose the saving method.

        Returns:
        - str: Selected saving method index.
        """
        print('\nSaving method:\n')
        print_options_list(self.options_list)
        return input(f'\nChoose one: ')


class DataProcess:
    def eligibility_check(self):
        """
        Display the eligibility check message.
        """
        print('\n\nChecking for eligibility...\n\n')

    def eligible(self):
        """
        Display the message indicating the user is eligible to proceed.
        """
        print('\nGreat, you are authorized to process the extraction!'
              '\nExtraction will be proceed.')

    def not_eligible(self):
        """
        Display the message indicating the user is not eligible to proceed.
        """
        print('\nSorry, not authorized to proceed!'
              'Check your URL and extraction method, then retry')

    def extraction_is_processing(self):
        print('\nExtraction is processing ...')

    def extraction_output(self, content):
        """
        Display the extracted data.

        Args:
        - content (str): Extracted data to be displayed.
        """
        print(f'\nHere is your extracted data:\n'
              f'\n----------------------------'
              f'\n{content}'
              '\n----------------------------')


class EndOfProcess:
    def __init__(self, attempt_number, options_list):
        """
        Initialize the EndOfProcess view with attempt number and options list.

        Args:
        - attempt_number (int): Number of attempts made.
        - options_list (list): List of options for the end of the process.
        """
        self.attempt_number = attempt_number
        self.options_list = options_list

    def number_of_attempt(self, number):
        """
        Display the number of attempts made.

        Args:
        - number (int): Number of attempts made.
        """
        print(f'\nNumber of attempt: {number}')

    def retry_or_quit(self):
        """
        Prompt the user to choose the next action.

        Returns:
        - str: Selected action index.
        """
        print('\nWhat to do next?\n')
        print_options_list(self.options_list)
        return input(f'\nChoose one: ')

    def quit(self):
        """
        Display the quitting message.
        """
        input('\nGreat, have a nice day :)\n'
              'Press Enter to quit ...\n')
