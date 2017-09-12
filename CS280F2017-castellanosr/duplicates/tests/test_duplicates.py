"""Test suite for the duplicates.py module"""

import pytest
import duplicates


def test_duplicates_removed():
    """Run the duplicate remove and see that the list gets smaller """
    list_one = [1, 2, 3, 4]
    list_two = [1, 2, 5, 6]
    duplicates.remove_duplicates(list_one, list_two)
    assert list_one != list_two
    assert list_one != list_two
    assert len(list_one) == 2
    assert (1 in list_one) is True
    assert (2 in list_one) is True
