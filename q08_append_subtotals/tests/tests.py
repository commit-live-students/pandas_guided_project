import sys, os

# sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q08_append_subtotals
from inspect import getfullargspec
import pandas

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
df = q08_append_subtotals(path1, path2)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q08_append_subtotals).args
        self.assertEqual(len(arg), 2, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_return_shape(self):
        self.assertEqual(df.shape, (14,4), "The Expected return shape does not match with the given return shape")

    def test_return_value_Jan(self):
        self.assertEqual(df.iloc[-1]['Jan'],'$1,462,000',"The Return value does not match expected value")

    def test_return_value_Feb(self):
        self.assertEqual(df.iloc[-1]['Feb'],'$1,507,000',"The Return value does not match expected value")

    def test_return_value_March(self):
        self.assertEqual(df.iloc[-1]['Mar'], '$717,000', "The Return value does not match expected value")




