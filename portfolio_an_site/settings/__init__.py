# For backwards compatibility's sake. Load the local settings if none supplied.
import os
execfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'local.py'))
