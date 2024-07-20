import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "BriefBot"
AUTHOR_USER_NAME = "pragati_paraagi"
SRC_REPO = "BriefBot"
AUTHOR_EMAIL = "202251097@iiitvadodara.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for NLP app",
    long_description=long_description,  # Corrected this line
    long_description_content_type="text/markdown",  # Corrected this line
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Corrected this line
    packages=setuptools.find_packages(where="src")
)
