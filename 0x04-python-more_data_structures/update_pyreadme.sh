#!/bin/bash

# Check if README.md exists
if [ ! -f README.md ]; then
    echo "Enter a header for your README.md:"
    read header
    echo "# $header" > README.md
    echo "" >> README.md
    echo "**This directory contains files that can be tested for $header .**" >> README.md
    echo "" >> README.md
    echo "## Tasks" >> README.md
    echo "" >> README.md
    echo "> [!IMPORTANT]" >> README.md
    echo "> Make the Python files executables using the following command:" >> README.md
    echo "" >> README.md
    echo "\`chmod +x <filename>\`" >> README.md
    echo "" >> README.md
    echo "> [!NOTE]" >> README.md
    echo "> If there aren't any main.py files provided for a task, use test files to run the program." >> README.md
    echo "" >> README.md
fi

# Loop until the user decides to stop
while true; do
    echo ""
    echo "What's the task title (or 'q' to quit):"
    read task_num
    if [ "$task_num" = "q" ]; then
        break
    fi
	echo ""
    echo "What's the file name for task $task_num:"
    read file_name
	echo ""
    echo "Enter a short description for the functions in $file_name:"
    read desc
    echo "" >> README.md
    echo "- **$task_num.**" >> README.md
    echo "" >> README.md
    echo "   - :file_folder: : \`$file_name\`: $desc" >> README.md
	echo "$task_num" >> .commit_msg
    while true; do
		echo ""
        echo "Do you still want to update the README file again? (yes/no)"
        read answer
        if [ "$answer" = "yes" ]; then
            break
        elif [ "$answer" = "no" ]; then
            exit 0
        else
            echo "Invalid input! Please enter 'yes' or 'no'."
        fi
    done
done
