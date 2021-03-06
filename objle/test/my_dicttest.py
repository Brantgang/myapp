import unittest
from objle.test.dict import Dict
#继承unittest.TestCase方法
class TestDict(unittest.TestCase):


    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    def test_key(self):
         d=Dict()
         d['key']='value'
         self.assertEqual(d.key,'value')
    def test_attr(self):
         d=Dict()
         d.key = 'value'
         self.assertTrue('key' in d)
         self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
    def seetup(self):
        print('setup.....')
    def tearDown(self):
        print('teardown ...')



if __name__=='__main__':
        unittest.main()

















