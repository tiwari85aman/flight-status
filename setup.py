from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='flight-status',
    version='1.0.0',
    description='PIP package to get status of flight pnr status and other details [Indian Airlines]',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Aman Tiwari',
    author_email='tiwari.aman85@gmail.com',
    keywords=['Flight', 'PNR', 'Pnr status', 'India', 'Airlines'],
    url='https://github.com/tiwari85aman/flight-status.git',
    download_url='https://pypi.org/project/flight-status/'
)

install_requires = [
    'beautifulsoup4<=4.9.1',
    'selenium<=3.141.0',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
