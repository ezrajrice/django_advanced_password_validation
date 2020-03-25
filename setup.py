from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    README = readme_file.read()

with open('HISTORY.md', encoding='utf-8') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='django-advanced_password_validation',
    version='1.0.4',
    description='Extends Django password validation options to include minimum uppercase, lowercase, numerical, and special characters.',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Ezra Rice',
    author_email='ezra.j.rice@gmail.com',
    keywords=['django', 'password', 'validator'],
    url='https://github.com/ezrajrice/django-advanced_password_validation.git',
    download_url='https://pypi.org/project/django-advanced_password_validation'
)

install_requires = [
    'Django>=1.11'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)