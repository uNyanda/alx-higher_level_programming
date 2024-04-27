#!/bin/bash
# Sends a POST request to the passed URL, and displays the body response
curl --silent --data POST --data "email=test@gmail" --data "subject=I will always be here for PLD" "$1"
