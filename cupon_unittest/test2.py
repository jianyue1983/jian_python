import unittest,os,time
import sys

discover= unittest.defaultTestLoader.discover(str('H:\\Code\\cupon_unittest\\testcase'),pattern='test*.py',top_level_dir=None)

if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(discover)
    print('aaa')