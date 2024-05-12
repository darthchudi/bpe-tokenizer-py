test:
	@python -m unittest *_test.py

run:
	@python main.py

lint:
	# Run the linter
	@ruff check --fix

	# Format the files
	@ruff format