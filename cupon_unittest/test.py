import unittest
import ddt  #第三方库

data=[[1,2],[3,4],[5,6]]

@ddt.ddt

class MyTestCase(unittest.TestCase):

    # 只有一个参数时
    @ddt.data(1,2,3)
    def test_01(self,a):
        print(a)

    @ddt.data(*data)#表示可变参数取值为data([1,2],[3,4],[5,6])，若传参是data,则后面的取值 data([[1,2],[3,4],[5,6]])
    @ddt.unpack
    def test_02(self,a,b):
        print(a,'----',b)

    @ddt.data(*data)  # 表示可变参数取值为data([1,2],[3,4],[5,6])，若传参是data,则后面的取值 data([[1,2],[3,4],[5,6]])
    # @ddt.unpack
    def test_02(self, a, b):
        print(a, '****', b)

    @ddt.data([1,2],[3,4])#和上面的相似，这里未使用变量
    @ddt.unpack
    def test_03(self,a,b):
        print(a, '----', b)