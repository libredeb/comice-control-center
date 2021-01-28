VIRTUAL_ENV ?= venv
PIP=$(VIRTUAL_ENV)/bin/pip
PYTHON=$(VIRTUAL_ENV)/bin/python
PYTHON_MAJOR_VERSION=3
PYTHON_MINOR_VERSION=6
SYSTEM_DEPENDENCIES= \
    git \
    libpython$(PYTHON_VERSION)-dev \
    python$(PYTHON_VERSION) \
    python$(PYTHON_VERSION)-dev \
    python3-aptdaemon \
    python3-aptdaemon.gtk3widgets \
    python3-gi \
    virtualenv
PYTHON_VERSION=$(PYTHON_MAJOR_VERSION).$(PYTHON_MINOR_VERSION)
PYTHON_MAJOR_MINOR=$(PYTHON_MAJOR_VERSION)$(PYTHON_MINOR_VERSION)
PYTHON_WITH_VERSION=python$(PYTHON_VERSION)

all: virtualenv

system_dependencies:
	apt install --yes --no-install-recommends $(SYSTEM_DEPENDENCIES)

$(VIRTUAL_ENV):
	virtualenv --python=$(PYTHON_WITH_VERSION) --system-site-packages $(VIRTUAL_ENV)
	$(PIP) install -r requirements.txt

virtualenv: $(VIRTUAL_ENV)

deb:	
    $(PYTHON) setup.py --command-packages=stdeb.command sdist_dsc bdist_deb

clean:
	@rm -rf deb_dist dist comice_control_center.egg-info
	@rm -f comice-control-center*.tar.gz

run: virtualenv
	$(PYTHON) comice-control-center

