import unittest

import mymod

class RandomTesting(unittest.TestCase):
    #setup function run before each test
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_random(self):
        rand_num = mymod.my_num()
        
        self.assertTrue(0 <= rand_num < 1)

    #test to fail on purpose
    def test_fail(self):
        rand_num = mymod.my_num()
        test_num = int(rand_num)
        self.assertTrue(rand_num == test_num)

    def test_int(self):
        rand_num = mymod.my_int()
        test_num = int(rand_num)
        self.assertEquals(rand_num,test_num)

if __name__ == "__main__":
    unittest.main()