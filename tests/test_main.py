# This testing script showcases some unit testing patterns
# There are lots of other tricks to learn in unit testing,
# but hopefully this is instructive.
import io
import itertools
import re
import sys
import unittest
from unittest.mock import patch

from parameterized import parameterized

from swl_sample_project_repository.main import Greeting
from swl_sample_project_repository.main import sayhello


class TestGreeting(unittest.TestCase):
    """
    We usually create a test class per module.

    Test cases inherit from unittest.TestCase.

    In this case we have two methods to test the two main functions
      in main.py: the tostring() method of the Greeting class and the
      function sayhello()

    To test Greeting.tostring() we test four cases by passing all
      combinations of two sets of two arguments {"Joe", "Jantine"}
      and {"good", "great"}. This creates 4 tests and is called a
      test matrix:

            |  Jantine |   Joe   |
      --------------------------
      good  |  test 1  |  test 2 |
      --------------------------
      great |  test 3  |  test 4 |

    We do this with the @parameterized.expand decorator, which
      can be passed an explicit list of tuples to run the test with
      or can be used powerfully in combination with itertools.product
      as shown below.

    To test sayhello() we use two useful patterns:

      * We change stdout to be a file-like object so that we can read
          anything our code prints
      * We "mock" the Greeting object using the patch.object decorator,
          which allows us to force Greeting.tostring() to return a
          certain value. It does this by creating a unittest.mock.MagicMock
          object
          (https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock)
          which keeps track of the number of times it was called and what
          arguments were used each time.

    """

    def test_greeting(self):
        greeting = Greeting("name", "adjective")
        assert greeting.name == "name"
        assert greeting.adjective == "adjective"

    @parameterized.expand(
        itertools.product(
            # Could add more lines here for a higher-dimensional test matrix
            ["Joe", "Jantine"],
            ["good", "great"],
        )
    )
    def test_tostring(self, name, adjective):
        greeting = Greeting(name, adjective)
        intended_pattern = r"Hi, (.+). It's (.+) to see you."
        vars = re.search(intended_pattern, greeting.tostring()).groups()
        assert vars == (name, adjective)

    @patch.object(Greeting, "tostring")
    def test_sayhello(
        self, mock_greeting  # this argument references the mocked method
    ):
        mock_return_value = "Hi there"
        mock_greeting.return_value = mock_return_value
        out = io.StringIO()
        sys.stdout = out  # redirect stdout to something we can read()
        sayhello()
        sys.stdout = sys.__stdout__  # put stdout back to normal
        out.seek(0)
        assert out.read().strip() == mock_return_value
        assert mock_greeting.call_count == 1
