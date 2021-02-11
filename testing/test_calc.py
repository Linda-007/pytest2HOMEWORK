import allure
import pytest
import yaml
import sys
sys.path.append('..')


def get_datas(name,type='int'):
    with open("./datas/calc.yaml") as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return (datas,ids)



@pytest.fixture(params=get_datas('add','int')[0],ids=get_datas('add','int')[1])
def get_datas_with_fixture(request):
    return request.param

def test_param(get_datas_with_fixture):
    print(get_datas_with_fixture)

@pytest.fixture(params=get_datas('div', 'int')[0], ids=get_datas('div', 'int')[1])
def get_datas_div_fixture(request):
    return request.param

def test_div_param(get_datas_div_fixture):
        print(get_datas_div_fixture)


@allure.feature()
class TestCalculator:
    add_int_data = get_datas('add','int')
    div_int_data = get_datas('add','int')

    @allure.title(f"相加_{get_datas_with_fixture}")
    @allure.story("相加功能")
    def test_add(self,get_instance,get_datas_with_fixture):
        f = get_datas_with_fixture
        assert f[2] == get_instance.add(f[0],f[1])

    @pytest.mark.parametrize("a,b,result",[
        [0.1,0.2,0.3]
    ])
    def test_add_float(self,get_instance,a,b,result):
        assert result == round(get_instance.add(a,b),2)

    def test_add1(self,get_instance):
        datas = [[1,2,3],[-1,2,1],[100,200,300]]
        for data in datas:
            print(data)
            assert data[2] == get_instance.add(data[0],data[1])



    @allure.title(f"相除_{get_datas_div_fixture}")
    @allure.story("相除功能")
    def test_div(self,get_instance,get_datas_div_fixture):
        d1 = get_datas_div_fixture
        assert d1[2] == get_instance.div(d1[0],d1[1])

    def test_div1(self,get_instance):
        datas = [[2,1,2],[-8,2,-4],[0.4,0.2,2],[3,0,3]]
        for data in datas:

            if data[1] == 0:
                try:
                    get_instance.div(data[0],data[1])
                except ZeroDivisionError as e:
                            print("除数不能为0")
            else:
                assert  data[2] == get_instance.div(data[0],data[1])