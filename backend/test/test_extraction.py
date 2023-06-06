import pytest

from ..model import Extraction


def setup(type_of_extraction):
    """
    Setup the extraction object.

    Args:
    - type_of_extraction (int): Type of extraction to perform.

    Returns:
    - Extraction: Extraction object.
    """
    return Extraction('Mohamed Ouédraogo',
                      'ouedraogomohamed008@gmail.com',
                      'https://example.com',
                      type_of_extraction,
                      2,
                      1,
                      1)


def test_source_code_extraction():
    """
    Test the source code extraction.
    """
    extraction = setup(1)
    content = extraction.source_code()

    assert content.startswith('<!doctype html>')
    assert '<title>' in str(content)
    assert '<body>' in str(content)


def test_content_extraction():
    """
    Test the content extraction.
    """
    extraction = setup(2)
    content = extraction.content_extraction()

    assert len(content) > 0
    assert '<p>' in str(content)


def test_save_file():
    """
    Test the saved file
    """
    extraction = setup(1)
    content = extraction.save_file()

    assert 'Extracted_Content_1.txt' in str(content)


if __name__ == '__main__':
    pytest.main()
