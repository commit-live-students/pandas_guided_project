#import sys, os

#sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_append_row
from inspect import getfullargspec
import pandas
import pep8
# import subprocess
# subprocess.call('pep8 --max-line-length=150')

path = 'data/excel-comp-data.xlsx'
df = q02_append_row(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q02_append_row).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_return_shape(self):
        self.assertEqual(df.shape, (16, 10), "The Expected return shape does not match with the given return shape")


