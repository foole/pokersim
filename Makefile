.PHONY: test clean-test

test:
	PYTHONPATH=.:${PYTHONPATH} pytest -vv --cov=pokersim --cov-report term-missing tests/

debug-test:
	PYTHONPATH=.:${PYTHONPATH} pytest -vv --cov=pokersim --cov-report term-missing --pdb tests/

clean-test:
	find tests/ -name "__pycache__" -type d -exec rm -fr {} \;

clean: clean-test
	find pokersim/ -name "__pycache__" -type d -exec rm -fr {} \;
