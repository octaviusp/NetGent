from setuptools import setup, find_packages

setup(
    name="netgent",
    version="0.1.0",
    description="NetGent (Network Agent) is a functional API to design multi agent graph systems.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="NetGent Authors",
    author_email="",  # You might want to add an email here
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.2.14",
        "torch>=2.4.0",
    ],
    python_requires=">=3.12",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
)