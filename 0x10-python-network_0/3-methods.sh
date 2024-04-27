#!/bin/bash
# Send an OPTIONS request to the specified URL and display accepted methods
curl -sI "$1" | grep -i Allow | awk '{print $2}' | tr ',' ' '
