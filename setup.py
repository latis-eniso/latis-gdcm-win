from setuptools import setup, find_packages
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()


setup_args = dict(
    name="latis-gdcm-win",  # Replace with your own username
    version="0.0.1",
    author="Mohamed Amine",
    author_email="hiddentn@outlook.com",
    description="LATIS image processing utilities for python",
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    url="http://www.latis-eniso.org/",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"],

    python_requires='>=3.0',
    packages=[],
    data_files=[
        ('lib/site-packages/gdcmlib', glob("gdcm/gdcmlib/*")),
        ('lib/site-packages/gdcmlib/XML', glob("gdcm/XML/*")),
        ('lib/site-packages', ["gdcm/gdcm.py"])
    ],
)

install_requires = []

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires,
          include_package_data=True)
