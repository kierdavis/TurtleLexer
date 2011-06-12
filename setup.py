from setuptools import setup
setup(
  name = "TurtleLexer",
  version = "0.1",
  
  py_modules = ["turtlelexer"],
  
  author = "Kier Davis",
  author_email = "kierdavis@gmail.com",
  description = "A Turtle lexer for Pygments",
  keywords = "pygments lexer turtle rdf",
  classifiers = ["Programming Language :: Python", "Operating System :: OS Independant", "Topic :: Software Development :: Libraries :: Python Modules"],
  
  install_requires = ["Pygments"],
  entry_points = {"pygments.lexers": "turtlelexer = turtlelexer:TurtleLexer"},
)
