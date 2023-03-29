
install:
	@poetry install
server:
	@uvicorn passgenapi.main:app --reload
format:
	@black -l 79 .
	@isort .
lint:
	@black -l 79 --check .
	@isort --check .
test:
	@echo PRECISA ATIVAR O SERVIDOR PARA RODAR OS TESTES DE API!
	@pytest tests/units/test_hash_generator.py -v
	@pytest tests/units/test_password_generator.py -v
sec:
	@pip-audit