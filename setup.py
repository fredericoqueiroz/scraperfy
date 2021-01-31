import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scraperfy",
    version="0.0.1",
    author="Frederico Queiroz",
    author_email="rqfrederico@gmail.com",
    description="A Financial Data Web Scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fredericoqueiroz/scraperfy",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)