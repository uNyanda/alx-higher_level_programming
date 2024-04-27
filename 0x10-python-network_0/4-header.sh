#!/bin/bash
# This script sends a GET request, and displays the body response.
curl --silent --request GET "$1" --header "X-School-User-Id: 98"
