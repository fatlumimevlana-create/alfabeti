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

    - name: Install Buildozer dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

    - name: Install Buildozer
      run: |
        pip install --upgrade pip
        pip install buildozer

    - name: Run Buildozer
      run: |
        buildozer clean
        buildozer -v android debug
