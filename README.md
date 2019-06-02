# GhostDelivery

This tool creates a obfuscated .vbs script to download a payload hosted on a server to %TEMP% directory, disable windows AV, execute payload and gain persistence
by editing registry keys and creating a scheduled task to run payload at login.  

# Features: 
Downloads payload to TEMP directory and executes payload
to bypass windows smart screen. Disables Defender, UAC/user account control, Defender Notifications, injects/creates Command Prompt and Microsoft Edge shortcuts with payload path (%TEMP%/payload.exe), adds a scheduled task called "WindowsDefender" for payload to be run at login and obfuscates the vbs delivery script. This tool also has a serveo function to deliver obfuscated vbs script.

# Light version:

The light version is less noisy and only delivers/executes payload, creates a scheduled task named "WindowsDefender" to run payload at login for persistence and injects/creates Command Prompt and Microsoft Edge shortcuts with payload path.

# Prerequisites
*Python 2.7, Modules imported in script.
(random, sys, string, os, time, base64)




