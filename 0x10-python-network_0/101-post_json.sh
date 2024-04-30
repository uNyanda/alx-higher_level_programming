#!/bin/bash
# This scipt sends a JSON POST request to the specified URL using curl.
curl --silent --request POST --header "Content-Type: application/json" --data @"$2" "$1" 
