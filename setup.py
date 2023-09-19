from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education', 
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='myregr',
  version='0.0.1',
  description='a regression tool',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Venkat B S',
  author_email='venkatbs2003@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='regression', 
  packages=find_packages(),
  install_requires=['numpy','scikit-learn'] 
) 