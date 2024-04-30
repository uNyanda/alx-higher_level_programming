#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me and cause the server to respond with a message containing You got me!, in the body of the response
curl --silent --location --request POST 0.0.0.0:5000/catch_me --data "user_id=98"
