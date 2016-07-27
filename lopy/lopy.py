import argparse
import configparser
import os
import warnings

from lopy.commands import install, do, run, execute, console

def find_up(path):
  # Look for the following in order:
  # .lopyconfig
  # .pip directory
  # requirements.txt
  # .git directory
  # If none are found, then lopy can't sensibly find directory to work on 
  lookups = [ ".lopyconfig", ".pip/", "requirements.txt", ".git/" ]
  abs_path = os.path.realpath(path)

  if abs_path == '/':
    return False
  for lookup in lookups:
    if os.path.exists(lookup):
      return abs_path
  return find_up(abs_path + '/..')

# Example
def main():
  arg_dict = {
    "install": install,
    "do": do,
    "exec": execute,
    "run": run,
    "console": console
  }

  # Add various parsers for commands
  parser = argparse.ArgumentParser(description='lopy -- Install local Python packages')
  parsers = parser.add_subparsers(title="Options", dest="command")

  install_parser = parsers.add_parser('install', help='Local pip install (by default installs requirements.txt). Usage: lopy install [dep_name]')
  install_parser.add_argument('args', nargs="*")

  do_parser = parsers.add_parser('do', help='Run a lopyconfig task. Usage: lopy do <task_name>')
  do_parser.add_argument('args', nargs=1, metavar="task_name", help="Name of the task in lopyconfig")

  run_parser = parsers.add_parser('run', help='Run a python script at <path> (alias for `exec python`). Usage: lopy run <script>')
  run_parser.add_argument('args', nargs="+", metavar="script_name", help="The script name, e.g. `server.py`")

  exec_parser = parsers.add_parser('exec', help='Execute a program within the local development environment. Usage: lopy exec <command>')
  exec_parser.add_argument('args', nargs="+", metavar="command", help="Command to execute")

  install_parser = parsers.add_parser('console', help='Spawn a console')
  install_parser.add_argument('args', nargs="*")

  # Create dict from argparse Namespace
  args = vars(parser.parse_args())

  if len(args) == 0 or not args["command"]:
    quit(parser.print_help())

  method = args["command"]
  method_arguments = args["args"]

  try:
    arg_dict[method]
  except KeyError:
    quit(parser.print_help())

  # Find the closest directory to run lopy in
  lopy_dir = find_up(os.getcwd())

  # Check if `module_dir` key is present in `.lopyconfig`
  config = configparser.ConfigParser()
  config.read(lopy_dir + '/.lopyconfig')
  module_dir = '.pip'

  if len(config):
    try:
      module_dir = config['config']['module_dir']
    except KeyError:
      pass

  # Quit with error if could not find lopy_dir
  if not lopy_dir:
    # We specifically allow installing a module directly
    if method == 'install' and len(method_arguments) > 0:
      warnings.warn('Could not locate suitable directory. Using current directory...')
      lopy_dir = os.getcwd()
    else:
      quit("Could not locate .lopyconfig, .pip directory, requirements.txt, or .git directory")

  lopy_dir = lopy_dir + '/' + module_dir

  arg_dict[method](lopy_dir, config, *method_arguments)
