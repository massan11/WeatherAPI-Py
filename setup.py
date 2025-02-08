import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "weatherapi_py",
    version = "0.0.1",
    author = "Mhammad H Kazemi",
    author_email = "mhassan.zoho@gmail.com",
    description = "WeatherAPI-Py is a Python package for retrieving real-time air temperature using Open-Meteo and OpenWeather APIs. It supports multiple data sources, easy integration, and temperature conversion",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/massan11/WeatherAPI-Py",
    project_urls = {
        "Author": "https://github.com/massan11",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        "requests"
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)