import os
import httplib2

def path(*a):
  ROOT = os.path.dirname(os.path.abspath(__file__))
  return os.path.join(ROOT, *a)

def download_url(url, dest=None):
  h = httplib2.Http()
  resp, content = h.request(url, "GET")

  if dest == None:
    dest = os.path.basename(url)

  local = open(dest, 'wb')
  local.write(content)
  local.close()
  return dest
