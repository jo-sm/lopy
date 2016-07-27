import os
import pip
import subprocess
import warnings

def install(lopy_dir, config, *args):
  os.environ["PYTHONUSERBASE"] = lopy_dir

  if len(args) == 0:
    args = ("-r", "requirements.txt")

  pip.main(['install', '--user'] + list(args))

def do(lopy_dir, config, *args):
  # Look for the task given at args[0]
  task_name = args[0]

  try:
    task_command = config['tasks'][task_name]
    execute(lopy_dir, config, task_command)
  except KeyError:
    warnings.warn("Task {} not found".format(task_name))

def console(lopy_dir, config, *args):
  execute(lopy_dir, config, "python")

def run(lopy_dir, config, *args):
  execute(lopy_dir, config, *([ "python" ] + list(args)))

def execute(lopy_dir, config, *args):
  env = os.environ.copy()
  env["PYTHONUSERBASE"] = lopy_dir
  subprocess.Popen(list(args), env=env).communicate()
