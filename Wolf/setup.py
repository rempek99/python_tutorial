from distutils.core import setup, Extension

setup(name='chase',
      version='1.0',
      description='Python Wolf Chasing Sheeps Simulation',
      author='Arkadiusz Remplewicz',
      author_email='224413@edu.p.lodz.pl',
      py_modules=['__main__', 'Parser'],
      packages=['Entities'],
      data_files=[('config', ['config'])]
      )
