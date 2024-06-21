#!/usr/bin/make -s -f
include update_pymakefile.mk

PY = python3
SCRIPT = 
EXECUTABLE = 102-magic_calculation.py
FILE = 102-magic_calculation.py 

.PHONY: all test chmod git clean

all: chmod test count style

test:
	@echo
	@if [ "$(SCRIPT)" = "" ]; then \
		echo "Running $(FILE)..."; \
		sleep 1; \
		$(PY) $(FILE); \
		EXECUTABLE=$(FILE); \
	else \
		echo "Running $(SCRIPT)..."; \
		sleep 1; \
		$(PY) $(SCRIPT); \
		EXECUTABLE=$(SCRIPT); \
	fi
	@echo
	@echo "$(EXECUTABLE) is the executable file"

chmod:
	@echo
	@chmod u+x $(EXECUTABLE)
	@echo "$(EXECUTABLE) made an executable"

git:
	@git add .
	@if [ -f .commit_msg ]; then \
		git commit -m "$$(cat .commit_msg)"; \
		rm .commit_msg; \
	else \
		read -p "Enter commit message: " msg; \
		git commit -m "$$msg"; \
	fi
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
	OUTPUT=$$(pycodestyle $(FILE)); \
	if [ -n "$$OUTPUT" ]; then \
		echo $$OUTPUT; \
        else \
                echo "No errors"; \
        fi'
	@echo
