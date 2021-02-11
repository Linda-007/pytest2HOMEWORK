from setuptools import setup

setup(
    name='pytest_encode',
    url='https://github.com/Linda_007/hookcode',
    version='1.0',
    author="RoseLin",
    author_email='1094064246@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[  # 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=['hookcode'],
    keywords=[
        'pytest', 'py.test', 'hookcode',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'hookcode = hookcode',
        ]
    },
    zip_safe=False
)