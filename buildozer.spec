name: Build APK

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: "3.10"

    - name: Install Buildozer
      run: |
        pip install --upgrade pip
        pip install buildozer

    - name: Run Buildozer
      run: |
        buildozer -v android debug
