import pytest

class TestA():
    def setup_class(self):
        print('setup')


    def teardown_class(self):
        print('teardown')

    @pytest.mark.run(order=-1)
    def test01(self):
        print('11111')
        assert 1


    def test02(self):
        print('22222')
        assert 1

    @pytest.mark.run(order=0)
    def test03(self):
        print('33333')
        assert 1

    @pytest.mark.run(order=1)
    def test04(self):
        print('44444')
        assert 1



