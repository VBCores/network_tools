code := `pwd`
tests := code + "/tests"
packages := "controller utils.py"

# Add source dir to pythonpath
pythonpath := "PYTHONPATH=./:" + code
# Executables
pytest := pythonpath + " pytest"
test_command := pytest + " --verbosity=2 --showlocals --strict-markers"

cov_level := "85"

# Проверка кода
lint:
    mypy {{code}}
    ruff check {{code}} {{tests}}
    black --skip-string-normalization --check {{code}} {{tests}}

# Отформатировать код
format files=packages:
    isort {{files}}
    black --skip-string-normalization {{files}}

# Запустить тесты
test:
    {{test_command}} --cov --cov-fail-under={{cov_level}}

# Запустить последний неудачный тест
test-failed:
    {{test_command}} --last-failed

# Собрать отчет о покрытии тестами
test-cov:
    {{test_command}} --cov-report html

# Линтинг и тестирование
validate: lint test
