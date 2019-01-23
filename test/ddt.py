from ddt import ddt,data,unpack
import unittest
from selenium import webdriver
@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        print("this is the setUp")
    @data([1,2,3])
    def test_1(self,value):
        print(value)
    @data([3,2,1], [5,3,2], [10,4,6])
    @unpack
    def test_2(self,a,b,expected):
        actual = int(a) - int(b)
        expected = int(expected)
        self.assertEqual(actual, expected)



    def test_3(self):
        bowser = webdriver.Chrome()
        bowser.refresh()