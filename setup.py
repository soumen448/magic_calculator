import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='magic_calculator',                           # should match the package folder
    packages=['magic_calculator'],                     # should match the package folder
    version='0.5',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='performs magic calculation',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Soumen Mondal',
    author_email='mondalsoumen00@gmail.com',
    url='https://github.com/soumen448/magic_calculator',
    install_requires=['requests'],                  # list all packages that your package uses
    keywords=["pypi", "magic_calculator", "tutorial"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/soumen448/magic_calculator/archive/refs/tags/0.5.tar.gz",
)