from setuptools import setup

VERSION = "0.1.0"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="cli-ask",
    version=VERSION,
    description="Query user in cli for options to choose in a nice output",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="cli",
    url="https://github.com/danilocgsilva/cli-ask-python",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["cli_ask"],
    include_package_data=True
)

