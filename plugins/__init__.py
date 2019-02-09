from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
All_PLUGINS = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
