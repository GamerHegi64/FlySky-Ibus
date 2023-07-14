from setuptools import setup

# Function to read the long description from the README file
def read_long_description():
  with open("README.md", "r", encoding="utf-8") as file:
    return file.read()

setup(
  name='flySkyiBus',
  version='1.0.0',    
  description='FlySky iBus python library for the raspberry pi.',
  long_description=read_long_description(),
  long_description_content_type="text/markdown",
  url='https://github.com/GamerHegi64/FlySky-Ibus',
  author='GamerHegi64',
  author_email='gamerhegi64@gmail.de',
  packages=['flySkyiBus'],
  install_requires=[
    'pyserial>=3.4'                
  ]
)