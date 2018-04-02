#import sys, os

#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q03_scrape_clean
from inspect import getfullargspec
import pandas
import pep8
# import subprocess
# subprocess.call('pep8 --max-line-length=150')

path = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
df = q03_scrape_clean(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q03_scrape_clean).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_return_shape(self):
        self.assertEqual(df.shape, (77, 15), "The Expected return shape does not match with the given return shape")


