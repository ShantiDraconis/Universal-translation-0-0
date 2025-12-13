"""
setup.py for Universal Translation Engine 0/0

This file is maintained for compatibility with older installation methods.
For modern installations, pyproject.toml is the primary configuration.
"""

from setuptools import setup, find_packages

setup(
    name="universal-translation-0-0",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "universal_translation.mappings": ["*.json"],
        "universal_translation.datasets": ["**/*.csv", "**/*.json", "**/*.md"],
        "universal_translation.evaluation": ["*.md", "*.yaml"],
    },
    python_requires=">=3.9",
    install_requires=[],
    extras_require={
        "api": [
            "fastapi>=0.100.0",
            "uvicorn>=0.23.0",
            "pydantic>=2.0.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "universal-translate=universal_translation.api.cli:main",
        ],
    },
    author="Draconis",
    author_email="draconis@example.com",
    description="A modular framework for universal translation",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ShantiDraconis/Universal-translation-0-0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
