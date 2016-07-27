import os
import pip
import subprocess

def install(lopy_dir, *args):
  os.environ["PYTHONUSERBASE"] = lopy_dir

  if len(args) == 0:
    args = ("-r", "requirements.txt")

  pip.main(['install', '--user'] + list(args))

def do(lopy_dir, *args):
  pass

def run(lopy_dir, *args):
  execute(lopy_dir, *([ "python" ] + list(args)))

def execute(lopy_dir, *args):
  env = os.environ.copy()
  env["PYTHONUSERBASE"] = lopy_dir
  subprocess.Popen(list(args), env=env).communicate()
