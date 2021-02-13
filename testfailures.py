import unittest
import os
import platform

class Tests(unittest.TestCase):
    def test_0(self):
        self.assetTrue(True)
    @unittest.skip('skipped test')
    def test_1(self):
        self.fail('should have failed!')
    @unittest.skipIf(os.name=='posix','Not supported on Unix')
    def test_2(self):
        import winreg
    @unittest.skipUnless(platform.system()=='Darwin','Mac spesific test')
    def test_3(self):
        self.assetTrue(True)
    @unittest.expectedFailure
    def test_4(self):
        self.assetEqual(2+2,5)
    if __name__ == '__main__':
        unittest.main()