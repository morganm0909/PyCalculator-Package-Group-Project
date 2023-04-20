# Change the content according to your package.
import setuptools
import re

# Extract the version from the init file.
VERSIONFILE = "pycomputation/__init__.py"
getversion = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSIONFILE, "rt").read(), re.M)
if getversion:
  new_version = getversion.group(1)
else:
  raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE, ))

# Configurations
with open("README.md", "r") as fh:
  long_description = fh.read()
setuptools.setup(
  install_requires=['os'],  # Dependencies
  python_requires='>=3',  # Minimum Python version
  name='pycomputation',  # Package name
  version=new_version,  # Version
  author="Group 4",  # Author name
  author_email="jennai.jackson@bison.howard.edu",  # Author mail
  description= "Python package for pycomputation.",  # Short package description
  long_description= "PyComputation is a Python package created to act as a calculator for users. This package will work to do all the functions that can be done by a scientific calculator. This way, they can easily solve equations using the package's functions rather than having to create their own.",  # Long package description
  long_description_content_type="text/markdown",
  url="https://github.com/morganm0909/PyCalculator-Package-Group-Project.git",  # Url to your Git Repo
  download_url='https://github.com/morganm0909/PyCalculator-Package-Group-Project.git/archive/' +
  new_version + '.tar.gz',
  packages=setuptools.find_packages(
  ),  # Searches throughout all dirs for files to include
  include_package_data=
  True,  # Must be true to include files depicted in MANIFEST.in
  license_files=["LICENSE"],  # License file
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
)
