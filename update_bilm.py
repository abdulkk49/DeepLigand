import bilm
from os.path import join, dirname, abspath
from os import system

system(' '.join(['cp', join(dirname(abspath(__file__)), 'data.py'), join(bilm.__path__[0])]))
