# import sys, os

# sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q04_mapping
from inspect import getfullargspec
import pandas

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
df = q04_mapping(path1, path2)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q04_mapping).args
        self.assertEqual(len(arg), 2, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_return_value_Mississipi(self):
        self.assertEqual(str(df.iloc[6, 6]), 'nan', "The Expected return does not match with the given return")

    def test_return_value_tenessee(self):
        self.assertEqual(str(df.iloc[10, 6]), 'nan', "The Expected return does not match with the given return")
