#!/bin/bash  
echo "Installing python dependencies"
sudo apt-get install pip
sudo apt-get install espeak
sudo apt-get install python3-pyaudio
pip3 install pyttsx3
sudo apt-get update
echo "All python dependencies are installed, running the program"