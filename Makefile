
PYTHON ?= python
PYTESTS ?= pytest
CODESPELL_SKIPS ?= "doc/auto_*,*.fif,*.eve,*.gz,*.tgz,*.zip,*.mat,*.stc,*.label,*.w,*.bz2,*.annot,*.sulc,*.log,*.local-copy,*.orig_avg,*.inflated_avg,*.gii,*.pyc,*.doctree,*.pickle,*.inv,*.png,*.edf,*.touch,*.thickness,*.nofix,*.volume,*.defect_borders,*.mgh,lh.*,rh.*,COR-*,FreeSurferColorLUT.txt,*.examples,.xdebug_mris_calc,bad.segments,BadChannels,*.hist,empty_file,*.orig,*.js,*.map,*.ipynb,searchindex.dat,install_mne_c.rst,plot_*.rst,*.rst.txt,c_EULA.rst*,*.html,gdf_encodes.txt,*.svg"
CODESPELL_DIRS ?= eztrack/ doc/ tutorials/ examples/ tests/

MARCCDIR=ali39@jhu.edu@gateway2.marcc.jhu.edu:/home-1/ali39@jhu.edu/data/epilepsy_bids/

LOCAL_RESULTSDIR=/home/adam2392/hdd/derivatives/
EXTERNAL_RESULTSDIR=/media/adam2392/SEAGATE_HDD/derivatives/

LOCALDIR=/home/adam2392/hdd2/data/
EXTERNALDIR=/media/adam2392/SEAGATE_HDD/data/

LOCALDIR=/Users/adam2392/Downloads/tngpipeline/sourcedata/
#LOCALDIR=/Users/adam2392/Dropbox/phd_research/data/epilepsy_bids_data/
EXTERNALDIR=/Volumes/SEAGATE_HDD/sourcedata/

MARCC_USER=ali39@jhu.edu
ssh 							:= ssh $(port)
remote	          				:= $(MARCC_USER)@gateway2.marcc.jhu.edu

all: clean inplace test

clean-pyc:
	find . -name "*.pyc" | xargs rm -f
	find . -name "*.DS_Store" | xargs rm -f

clean-so:
	find . -name "*.so" | xargs rm -f
	find . -name "*.pyd" | xargs rm -f

clean-build:
	rm -rf _build
	rm -rf eztrack.egg-info
	rm -rf CLI_EZT.egg-info

clean-ctags:
	rm -f tags

clean-cache:
	find . -name "__pychache__" | xargs rm -rf
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm .coverage.*

clean-logs:
	rm ./eztrack/logs/*.log*

clean: clean-build clean-pyc clean-so clean-ctags clean-logs clean-cache

codespell:  # running manually
	@codespell -w -i 3 -q 3 -S $(CODESPELL_SKIPS) --ignore-words=ignore_words.txt $(CODESPELL_DIRS)

codespell-error:  # running on travis
	@echo "Running code-spell check"
	@codespell -i 0 -q 7 -S $(CODESPELL_SKIPS) --ignore-words=ignore_words.txt $(CODESPELL_DIRS)

cli:
	pip install click
	python ./eztrack/cli/setup.py develop

inplace:
	$(PYTHON) setup.py install
	pip install black pytest pytest-cov coverage codespell pydocstyle coverage-badge anybadge sphinx sphinx-gallery sphinx_bootstrap_theme numpydoc

test: inplace check-manifest
	rm -f .coverage
	$(PYTESTS) ./

test-doc:
	$(PYTESTS) --doctest-modules --doctest-ignore-import-errors

test-coverage:
	rm -rf coverage .coverage
	$(PYTESTS) --cov=./ --cov-report html:coverage

trailing-spaces:
	find . -name "*.py" | xargs perl -pi -e 's/[ \t]*$$//'

build-doc:
	cd doc; make clean
	cd doc; make html

pydocstyle:
	@echo "Running pydocstyle"
	@pydocstyle

pycodestyle:
	@echo "Running pycodestyle"
	@pycodestyle

push-marcc:
	rsync -aP $(LOCALDIR) $(MARCCDIR);

push-external:
#	rsync -aP $(LOCALDIR) $(EXTERNALDIR) --exclude='*/tempdir/';
	rsync -aP $(LOCAL_RESULTSDIR) $(EXTERNAL_RESULTSDIR);

pull-marcc:
	rsync -aP $(MARCCDIR) $(LOCALDIR);

pull-external:
	rsync -aP $(EXTERNALDIR) $(LOCALDIR) --exclude='*/tempdir/';

check-manifest:
	check-manifest --ignore .circleci*,doc,benchmarks,notebooks,data,tests

upload-pipy:
	python setup.py sdist bdist_egg register upload

black:
	@if command -v black > /dev/null; then \
		echo "Running black"; \
		black --check eztrack; \
	else \
		echo "black not found, please install it!"; \
		exit 1; \
	fi;
	@echo "black passed"

check:
	@$(MAKE) -k black pydocstyle codespell-error

ssh:
	$(ssh) $(remote)