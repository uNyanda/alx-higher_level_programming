#!/bin/bash
# Send an OPTIONS request to the specified URL and display accepted methods
curl --silent --head "$1" | grep -i Allow | awk '{print $2}' | tr ',' ' '
