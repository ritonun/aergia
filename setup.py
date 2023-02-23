from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="aergia",
    version="0.1.0",
    description="Game Engine Framework based on pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/ritonun/aergia",
    author="ritonun",
    # author_email=
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Games/Entertainment"
    ],
    keywords="pygame, engine, framework",
    package_dir={"": "engine"},
    packages=find_packages(where="engine"),
    python_requires=">=3.8, <4",
    install_requires=[
        "pygame >= 2.0.0"
    ],
    # data_files=[("fonts", ["res/fonts/m5x7.ttf"])],
    # project_urls={"source": "https://github.com/ritonun/pypygui"}
)
