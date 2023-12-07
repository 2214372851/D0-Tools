import os
from distutils.core import setup
from Cython.Build import cythonize

# setup(name="hello", ext_modules=cythonize("MOZI_IMG.py"))
setup(name="hello", ext_modules=cythonize("test.py"))

# os.system('python setup.py build_ext --inplace')
