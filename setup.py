import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flask-No-Cache",
    version="1.0",
    author="VolkerWessels Telecom",
    author_email="opensource@vwt.digital",
    description="Cache control for Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vwt-digital/flask-no-cache",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
