from distutils.core import setup



setup(
    name='DSD',
    version='1.0',
    packages=['dsd',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy >= 1.14.4",
        "pandas >= 0.24.2",
        "urllib3 >= 1.13.1",
    ],
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.csv',],
    },
    include_package_data=True,
)
