"""Setup script for Prompt-to-Song Generation using LLMs."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="prompt-to-song-llm",
    version="1.0.0",
    author="Contributors",
    description="Generate complete musical compositions from textual descriptions using LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GizzZmo/prompt-to-song-generation-using-large-language-models",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    keywords="music generation, llm, ai, deep learning, nlp, transformers",
)
