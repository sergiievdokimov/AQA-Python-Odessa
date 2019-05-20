# AQA-Python-Odessa

Status badge:
[![CircleCI](https://circleci.com/gh/sergiievdokimov/Python-AQA-course/tree/master.svg?style=svg)](https://circleci.com/gh/sergiievdokimov/Python-AQA-course/tree/master)

To run tests on CI you need to:
1) Install necessary dependencies via running appropriate commands:
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
2) run tests:
    . venv/bin/activate
    pytest --alluredir ~/AQA-Python-Odessa/reports/results
    
The project contains next tags:
- UI - tag for UI tests with Selenium