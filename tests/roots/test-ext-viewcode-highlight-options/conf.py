import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd().resolve()))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
highlight_language = 'python'
highlight_options = {'python': {'tabsize': 3}}
