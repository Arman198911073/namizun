from setuptools import setup, find_packages

setup(name='namizun_core',
      version='1.3.8',
      description='namizun main functions',
      author='MalKeMit',
      author_email='khodemalkemit@gmail.com',
      url='https://github.com/malkemit/namizun',
      setup_requires=['wheel'],
      packages=find_packages(),
      install_requires=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6']
      )
