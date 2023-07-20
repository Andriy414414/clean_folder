from setuptools import setup

setup(name='clean_folder',
      version='01',
      description='instrument for folder cleaning',
      url='https://github.com/Andriy414414/clean_folder.git',
      author='Andriy Kotenko',
      author_email='414andrey@gmail.com',
      packages=find_namespace_packages(),
      entry_points={"console_scripts": ['clean_folder=clean_folder.clean:main']}
