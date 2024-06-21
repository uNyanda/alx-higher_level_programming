PY = python3
SCRIPT =
EXECUTABLE = 3-infinite_add.py
FILE = 3-infinite_add.py

.PHONY: all test chmod git clean

all: chmod test count style

test:
	@echo
	@if [ "$(SCRIPT)" = "" ]; then \
		echo "Running $(FILE)..."; \
	sleep 1; \
		$(PY) $(FILE); \
	else \
		echo "Running $(SCRIPT)..."; \
	sleep 1; \
		$(PY) $(SCRIPT); \
	fi

chmod:
	@echo
	@chmod u+x $(EXECUTABLE)
	@echo "$(EXECUTABLE) made an executable"

git:
	@echo "Enter a commit message: "; \
	read NEW_MSG; \
	git add .;\
	git commit -m "$$NEW_MSG"; \
	git push

clean:
	rm -f *.pyc

count:
	@echo
	@echo "Line count:"
	@wc -l $(FILE)
	@sleep 1
	@echo

style:
	@echo "Checking $(FILE) for style errors..."
	@sleep 2
	@bash -c '\
	OUTPUT=$$(pycodestyle --show-source $(FILE)); \
	if [ -n "$$OUTPUT" ]; then \
		echo $$OUTPUT; \
	else \
		echo "No errors"; \
	fi'
	@echo
