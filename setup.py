from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='django-advanced_password_validation',
    version='0.1.1',
    description='Extends Django password validation options',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Ezra Rice',
    author_email='ezra.j.rice@gmail.com',
    keywords=['Django', 'password', 'validator'],
    url='',
    download_url=''
)

install_requires = [
    'Django>=1.11'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)