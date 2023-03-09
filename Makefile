PYTHON :=
ifeq ($(OS),Windows_NT)
	PYTHON=.venv/Scripts/python
else
	PYTHON=.venv/bin/python
endif

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"


install-requirements: check-venv
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m pip install -r requirements.txt

install-toml: check-venv
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m pip install .

## creates dist files and package release files based on pyproject.toml (depends on check-virtual-env)
build-toml: install-toml
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m build

# ---------------------------------------------------------
# Cleanup generated and installed files.

clean: 
	@find . -name '*.coverage *.pyc' -exec rm -f {} + 
	@find . -name '__pycache__' -exec rm -fr {} +
	rm -rf .coverage htmlcov 


clean-all: clean-build clean-pyc clean-test clean-doc clean-src clean-venv

clean-docs:
	rm -rf docs/build

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-src:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


run: check-venv
	@$(PYTHON) src/main.py

check-venv:
	@if [ -z "$$(which python | grep -o .venv)" ]; then \
		exit 1; \
	fi

pylint: check-venv
	@find src/ -name '*.py' -print0 | xargs -0 pylint -d C0103 -rn

test: check-venv
	$(PYTHON) -m unittest discover -p 'test_*.py' -v -b

flake8: check-venv
	@$(call MESSAGE,$@)
	@flake8 --exclude=.svn,CVS,.bzr,.hg,.git,__pycache__,.tox,.nox,.eggs,*.egg,.venv,venv,*.pyc

coverage: check-venv
	@$(call MESSAGE,$@)
	@coverage run -m unittest discover -p 'test_*.py' -v -b
	-coverage html
	-coverage report -m

# ---------------------------------------------------------
# Work with codestyle.
#
black:
	@$(call MESSAGE,$@)
	@$(PYTHON) -m black src/

codestyle: black


# ---------------------------------------------------------
# Work with generating documentation.
#
.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	$(PYTHON) -m pydoc -w src/*.py
	mv *.html doc/pydoc

# pdoc:
# 	@$(call MESSAGE,$@)
# 	pdoc --force --html --output-dir doc/pdoc src/*.py

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse src/*.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot

doc: pydoc pyreverse #pydoc sphinx



# ---------------------------------------------------------
# Calculate software metrics for your project.
#
radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average src

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show src

radon-raw:
	@$(call MESSAGE,$@)
	radon raw src

radon-hal:
	@$(call MESSAGE,$@)
	radon hal src

cohesion:
	@$(call MESSAGE,$@)
	cohesion --directory src

metrics: radon-cc radon-mi radon-raw radon-hal cohesion



# ---------------------------------------------------------
# Find security issues in your project.
#
bandit:
	@$(call MESSAGE,$@)
	bandit --recursive src

