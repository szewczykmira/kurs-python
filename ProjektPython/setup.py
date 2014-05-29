__author__ = 'Mira'
from distutils.core import setup

setup(name='NewDebter',
      version='1.0',
      description='Program do zarzadzania swoimi zasobami pienieznymi',
      author='Miroslawa Szewczyk',
      author_email='szewczyk.mira@gmail.com',
      py_modules=['main'],
      data_files=[('dat',['kwota.txt','newdb.db'])],
      )
