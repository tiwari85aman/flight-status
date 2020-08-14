from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='flight-status',
    version='1.0.1',
    description='PIP package to get status of flight pnr status and other details [Indian Airlines]',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Aman Tiwari, Shibani Mahapatra',
    author_email='tiwari.aman85@gmail.com, shibani.mahapatra47@gmail.com',
    keywords=['Flight', 'PNR', 'Pnr status', 'India', 'Airlines'],
    url='https://github.com/tiwari85aman/flight-status.git',
    download_url='https://pypi.org/project/flight-status/',
    python_requires=">=2.7.0",
    install_requires=[
        'beautifulsoup4<=4.9.1',
        'selenium<=3.141.0',
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],

)
