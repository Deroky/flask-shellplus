from setuptools import setup, find_packages


def fread(fpath):
    with open(fpath, 'r') as f:
        return f.read()


setup(
    name='Flask-ShellPlus',
    version='0.0.3',
    url='http://github.com/kxxoling/flask-shellplus/',
    license='MIT',
    author='Kane Blueriver',
    author_email='kxxoling@gmail.com',
    description='Flask shell command based on Flask-Script to enhance its shell',
    long_description=fread('README.rst'),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.10.0',
        'Flask-Script>=2.0.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
