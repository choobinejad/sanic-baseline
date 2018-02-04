import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.join(os.path.dirname(__name__), '..'))


# -- General configuration ------------------------------------------------

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = 'sanic-baseline'
copyright = '2018, choobinehad'
author = 'choobinehad'
version = '0.1'
release = '0.1-BETA'
language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'typekit_id': '',
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    # 'includehidden': True,
    # 'titles_only': False
}

html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

htmlhelp_basename = 'sanic-baselinedoc'


# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'sanic-baseline', 'sanic-baseline Documentation', [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'sanic-baseline', 'sanic-baseline Documentation',
     author, 'sanic-baseline', 'One line description of project.',
     'Miscellaneous'),
]



