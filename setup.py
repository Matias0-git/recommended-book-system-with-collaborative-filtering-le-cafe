from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based Books Recommender System"
AUTHOR_USER_NAME = "Matias0-git"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []

# this setups for real time development this is or implementing the end to end project

setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Matias Mena Da Dalt",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matias0-git/recommended-book-system-with-collaborative-filtering-le-cafe",
    author_email="matias.mena@comunidad.ub.edu.ar",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
