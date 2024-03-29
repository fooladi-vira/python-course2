import unittest
class test56(unittest.TestCase):
    def testcase(self,text):
        t1='Python'
        self.assertEqual(text,t1)
    if __name__=='__main__':
        unittest.main()