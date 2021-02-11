
import pytest



from pythoncode.Calc import Calc


@pytest.fixture(scope='session')
def get_instance():
    print("开始计算。。。")
    calc = Calc()
    yield  calc

    print("结束计算")