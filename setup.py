import setuptools

setuptools.setup(
    name='hdptest',
    version='0.4',
    scripts=[],
    author="Ismael Figueroa",
    author_email="ifigueroap@gmail.com",
    description="Mecanismo simple para tests en Jupyter Notebooks",
    url="https://github.com/ifigueroap/hdptest",
    packages=setuptools.find_packages(),
    install_requires=['pytest', 'ipytest', 'IPython',]
)