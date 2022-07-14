set -e
set -x
#python3 t.py
#exit 0
#python3 -m tom --directory . --log-level info --interactive
if [ -z "$1" ]; then
  python3 -m coverage run -m pytest | tee log
  python3 -m coverage html
else
  # for debugging, getting all output, and running a single test method:
  python3 -m pytest -k "$1" --show-capture=all -vv
fi
