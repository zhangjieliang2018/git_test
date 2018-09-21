import pytest


class TestDemo():
    def setup(self):
        print("我先执行")

    def teardown(self):
        print("我来结尾")
    @pytest.mark.run(order=2)
    def test_a(self):
        print("aaaaa")
    @pytest.mark.run(order=0)
    def test_b(self):
        print("bbbbbb")
