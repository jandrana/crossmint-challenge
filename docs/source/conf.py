# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'crossmint-challenge'
copyright = '2024, Ana Alejandra Castillejo Muñoz'
author = 'Ana Alejandra Castillejo Muñoz'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_wagtail_theme'
]

templates_path = ['_templates']
exclude_patterns = []

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": True
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
