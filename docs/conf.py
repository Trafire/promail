"""Sphinx configuration."""
import os
import sys

project = "Promailer: The Python Email Automation Framework"
author = "Antoine Wood"
copyright = f"2022, {author}"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
sys.path.insert(0, os.path.abspath(".."))
