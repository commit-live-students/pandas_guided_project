import sys, os

# sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q10_total
from inspect import getfullargspec
import pandas

path1 = 'data/excel-comp-data.xlsx'
path2 = 'data/scraped.csv'
df = q10_total(path1, path2)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q10_total).args
        self.assertEqual(len(arg), 2, "Expected argument(s) %d, Given %d" % (1, len(arg)))




