#!/bin/bash

# This script downloads covid data and display it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
TODAY=$(date)
DEATH=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
echo "On $TODAY, there were $POSITIVE positive covid cases, $NEGATIVE negative covid cases, $DEATH deaths, and $HOSPITALIZED people hospitalized."

