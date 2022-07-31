import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="READER-RSS", # Replace with your username

    version="1.0.0",

    author="Everton Tomalok",

    author_email="evertontomalok123@gmail.com",

    description="Reader RSS",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/EvertonTomalok/reader_rss",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',
    
    entry_points = {
        'console_scripts': ['reader-rss=src.cmd.cli:cli'],
    },

)