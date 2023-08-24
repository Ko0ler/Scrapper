class ViewInputError(Exception):
    """
    Base exception class for view input errors.
    """
    pass


class InvalidInputError(ViewInputError):
    """
    Exception class for invalid input errors.
    Inherits from ViewInputError.
    """
    pass


class InvalidChoiceError(ViewInputError):
    """
    Exception class for invalid choice errors.
    Inherits from ViewInputError.
    """
    pass
