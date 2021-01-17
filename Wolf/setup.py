from setuptools import setup, find_packages

setup(
    name='chase',
    version='1.1',
    description='Python Wolf Chasing Sheeps Simulation',
    author='Arkadiusz Remplewicz',
    author_email='224413@edu.p.lodz.pl',
    url="https://github.com/rempek99/python_tutorial",
    py_modules=['__main__', 'Parser'],
    data_files=[('config', ['config'])],
    packages=find_packages(),
)
