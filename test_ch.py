import pytest
from test_ch1 import Test_ch1
class Test_ch:
    @pytest.mark.parametrize("a,b,expected",[(10,20,30),(40,50,90)])
    def test_sum(self,a,b,expected):
        assert Test_ch1.add(a,b)==expected
    
    @pytest.mark.parametrize("c,d,expected1",[(1,2,2),(3,3,9)])
    def test_mul(self,c,d,expected1):
        assert Test_ch1.mul(c,d)==expected1

    # @pytest.fixture
    # def test_d(Test_ch1.Wip):
    # print("arrive")