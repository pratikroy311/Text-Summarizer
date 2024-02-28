import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
    
__version__ = "0.0.0"
REPONAME = "Text-Summarizer"
AUTHOR_USER_NAME = "pratik311"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "pratikroy311@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=f"A small python package for text-summarizing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues",
    },
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where='src'),
    
)