from setuptools import setup

setup(
  name='flySkyiBus',
  version='1.0.0',    
  description='FlySky iBus python library for the raspberry pi.',
  url='https://github.com/GamerHegi64/FlySky-Ibus',
  author='GamerHegi64',
  author_email='gamerhegi64@gmail.de',
  packages=['flySkyiBus'],
  install_requires=[
    'pyserial>=3.4'                
  ]
)