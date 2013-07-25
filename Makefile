LOCALISED_SCRIPTS = ipython ipdb flake8 pylint nose
PROJECT = $(shell basename $(shell pwd))

PYTHON_VERSION = 2.7
NIX_PATH = .
NIX_PROFILE = ./nixprofile${PYTHON_VERSION}
NIX_SITE = ${NIX_PROFILE}/lib/python${PYTHON_VERSION}/site-packages
VENV_CMD = ${NIX_PROFILE}/bin/virtualenv
VENV = .
VENV_SITE = ${VENV}/lib/python${PYTHON_VERSION}/site-packages
NOSETESTS = ${VENV}/bin/nosetests


export KEEP_FAILED := 1

all: print-python-version test-import check

nixpkgs:
	test -d nixpkgs || git clone -b work git://github.com/chaoflow/nixpkgs

bootstrap: nixpkgs
	nix-env -p ${NIX_PROFILE} -i dev-env -f dev${PYTHON_VERSION}.nix
	${VENV_CMD} --distribute --clear .
	realpath --no-symlinks --relative-to ${VENV_SITE} ${NIX_SITE} > ${VENV_SITE}/nixprofile.pth
	${VENV}/bin/pip install --src src-pip -r requirements.txt --no-index -f ""
	for script in ${LOCALISED_SCRIPTS}; do ${VENV}/bin/easy_install -H "" $$script; done

print-syspath:
	${VENV}/bin/python -c 'import sys,pprint;pprint.pprint(sys.path)'

print-python-version:
	${VENV}/bin/python -c 'import sys; print sys.version'

test-import:
	${VENV}/bin/python -c "import ${PROJECT}; print ${PROJECT}"

var:
	test -L var -a ! -e var && rm var || true
	ln -s $(shell mktemp --tmpdir -d ${PROJECT}-var-XXXXXXXXXX) var

var-clean:
	rm -fR var/*

check: var var-clean
	${NOSETESTS} -v -w . --logging-level=INFO ${ARGS}

check-debug: var var-clean
	DEBUG=1 ${NOSETESTS} --logging-level=DEBUG -v -w . ${ARGS}

check-ipdb: var var-clean
	${NOSETESTS} -v -w . --logging-level=INFO --ipdb --ipdb-failures ${ARGS}

check-ipdb-debug: var var-clean
	DEBUG=1 ${NOSETESTS} -v -w . --logging-level=DEBUG --ipdb --ipdb-failures ${ARGS}

coverage: var var-clean
	rm -f .coverage
	${NOSETESTS} -v -w . --with-cov --cover-branches --cover-package=${PROJECT} ${ARGS}


pyoc-clean:
	find . -name '*.py[oc]' -print0 |xargs -0 rm


deps-status:
	for x in $(shell cat requirements.txt | cut -d' ' -f2); do (cd $$x && echo $$x && git status); done

deps-push:
	for x in $(shell cat requirements.txt | cut -d' ' -f2); do (cd $$x && echo $$x && git push); done

deps-pull:
	for x in $(shell cat requirements.txt | cut -d' ' -f2); do (cd $$x && echo $$x && git pull --rebase); done

deps-describe:
	for x in $(shell cat requirements.txt | cut -d' ' -f2); do (cd $$x && echo $$x && git describe --tags); done

profile: var var-clean
	${NOSETESTS} -v -w . --with-cprofile ${ARGS}

.PHONY: all bootstrap check coverage print-syspath pyoc-clean test-nose var var-clean
