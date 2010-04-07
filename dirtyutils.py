import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def path(*a):
  return os.path.join(ROOT, *a)
