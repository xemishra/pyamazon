from pathlib import Path
from setuptools import setup, find_packages

# Function to read dependencies from requirements.txt!
def get_dependencies(path="requirements.txt"):
    req_file = Path(path)
    return req_file.read_text(encoding="utf-8").splitlines() if req_file.exists() else []

# Function to read README.md for long_description!
def get_long_description(path="README.md"):
    readme = Path(path)
    return readme.read_text(encoding="utf-8") if readme.exists() else ""

setup(
    name="pyamazon",
    version="0.0.3",
    author="Shivanand Mishra",
    description="Python module to fetch product data from Amazon",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=">=3.6",
    packages=find_packages(),  # This auto-detects pyamazon package!
    install_requires=get_dependencies(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Source": "https://github.com/xemishra/pyamazon",
        "Issues": "https://github.com/xemishra/pyamazon/issues"
    },
    include_package_data=True,
    zip_safe=False,
)
