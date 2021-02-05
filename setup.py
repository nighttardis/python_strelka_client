import setuptools

setuptools.setup(
    name='python_strelka_client',
    author='nighttardis',
    description='Python Client library for Strelka',
    license='Apache 2.0',
    packages=setuptools.find_packages(),
    scripts=['bin/strelka-backend']
)