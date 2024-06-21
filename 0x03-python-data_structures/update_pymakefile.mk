#!/usr/bin/make -s -f
TARGET_MAKEFILE := Makefile
OLD_MAIN_FILE := $(shell grep -oP 'SCRIPT = \K.*' $(TARGET_MAKEFILE))

# Get the latest file number
LATEST_NUM := $(shell ls -v | grep -oP '^\K\d+' | tail -n 1)

# Check if main and test files exist for the latest number
MAIN_FILE := $(shell if [ -f "$(LATEST_NUM)-main.py" ]; then echo "$(LATEST_NUM)-main.py"; fi)
TEST_FILES := $(shell if [ -z "$(shell ls -v $(LATEST_NUM)*.py 2>/dev/null | grep -v "$(LATEST_NUM)-main.py" | tr '\n' ' ')" ]; then echo "No test files found for the latest number."; else ls -v $(LATEST_NUM)*.py | grep -v "$(LATEST_NUM)-main.py" | tr '\n' ' '; fi); if [ "$$?" -ne 0 ]; then echo "Custom error message"; FILES=""; fi

README_SH := update_pyreadme.sh

.PHONY: update_makefile

# Updtes the target makefile.
update_makefile:
	@echo "Updating $(TARGET_MAKEFILE)..."
	@if [ "$(MAIN_FILE)" = "$(OLD_MAIN_FILE)" ]; then \
		echo "No new main file found..."; \
		sed -i 's|SCRIPT = .*|SCRIPT = |' $(TARGET_MAKEFILE); \
	else \
		sed -i 's|SCRIPT = .*|SCRIPT = $(MAIN_FILE)|' $(TARGET_MAKEFILE); \
	fi
	@if [ -z "$(SCRIPT)" ]; then \
		if [ -z "$(FILE)" ]; then \
			echo "Both SCRIPT and FILE variables are empty. Cannot update EXECUTABLE variable."; \
		else \
			sed -i 's|EXECUTABLE = .*|EXECUTABLE = $(FILE)|' $(TARGET_MAKEFILE); \
		fi; \
	else \
		sed -i 's|EXECUTABLE = .*|EXECUTABLE = $(SCRIPT)|' $(TARGET_MAKEFILE); \
	fi
	@if [ -z "$(TEST_FILES)" ]; then \
		echo "Didn't find new test files"; \
	else \
		sed -i 's|FILE = .*|FILE = $(TEST_FILES)|' $(TARGET_MAKEFILE); \
	fi

# Updates the README file.
update_pyreadme:
	@if [ -n "$(README_SH)" ]; then \
		chmod u+x $(README_SH); \
		echo "Running $(README_SH)..."; \
		./$(README_SH); \
	fi
