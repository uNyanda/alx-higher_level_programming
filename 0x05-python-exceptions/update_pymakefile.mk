#!/usr/bin/make -s -f

TARGET_MAKEFILE := Makefile
OLD_MAIN_FILE := $(shell grep -oP 'SCRIPT = \K.*' $(TARGET_MAKEFILE))

# Get the latest file number
LATEST_NUM := $(shell ls -v | grep -oP '^\K\d+' | tail -n 1)

# Check if main and test files exist for the latest number
MAIN_FILE := $(shell if [ -f "$(LATEST_NUM)-main.py" ]; then echo "$(LATEST_NUM)-main.py"; fi)
TEST_FILES := $(shell ls -v $(LATEST_NUM)*.py 2>/dev/null | grep -v "$(LATEST_NUM)-main.py" | tr '\n' ' ')

README_SH := update_pyreadme.sh

.PHONY: update_makefile

update_makefile:
	@echo "Updating $(TARGET_MAKEFILE)..."
	@if [ "$(MAIN_FILE)" != "$(OLD_MAIN_FILE)" ]; then \
		echo "New main file found..."; \
		sed -i "s|SCRIPT = .*|SCRIPT = $(MAIN_FILE)|" $(TARGET_MAKEFILE); \
		sed -i "s|FILE = .*|FILE = $(TEST_FILES)|" $(TARGET_MAKEFILE); \
	fi
	@SCRIPT_IN_MAKEFILE=$(shell grep -oP 'SCRIPT = \K.*' $(TARGET_MAKEFILE)); \
	FILE_IN_MAKEFILE=$(shell grep -oP 'FILE = \K.*' $(TARGET_MAKEFILE)); \
	if [ -z "$$SCRIPT_IN_MAKEFILE" ]; then \
		if [ -z "$$FILE_IN_MAKEFILE" ]; then \
			echo "Both SCRIPT and FILE variables are empty. Cannot update EXECUTABLE variable."; \
			sed -i "s|EXECUTABLE = .*|EXECUTABLE = |" $(TARGET_MAKEFILE); \
		else \
			sed -i "s|EXECUTABLE = .*|EXECUTABLE = $$FILE_IN_MAKEFILE|" $(TARGET_MAKEFILE); \
		fi; \
	else \
		sed -i "s|EXECUTABLE = .*|EXECUTABLE = $$SCRIPT_IN_MAKEFILE|" $(TARGET_MAKEFILE); \
	fi

# Updates the README file.
update_pyreadme:
	@if [ -n "$(README_SH)" ]; then \
		chmod u+x $(README_SH); \
		echo "Running $(README_SH)..."; \
		./$(README_SH); \
	fi
