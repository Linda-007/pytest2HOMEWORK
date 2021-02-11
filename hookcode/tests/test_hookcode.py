
import  pytest

@pytest.mark.parametrize('name',['南希','小明'])
@pytest.mark.parametrize('job',['设计师','测试员'])
def test_hookcode(name,job):
    print(name,job)

