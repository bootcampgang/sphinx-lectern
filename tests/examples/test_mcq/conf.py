"""Master configuration file for Sphinx.

Configuration for all subdirectories import this file and use it as a
base. For information about what any of these configuration options mean,
see:
"""
import sys
import os

sys.path.append(os.path.abspath("./../../.."))

master_doc = "index"
extensions = ["sphinxlectern", "sphinxlectern.mcq"]

html_theme = handouts_theme = "handouts"
pygments_style = "sphinx"
mcq_build_answerkey = True
mcq_build_scantron = True