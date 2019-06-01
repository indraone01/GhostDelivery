# GhostDelivery

This tool creates a obfuscated .vbs script to download a payload hosted on a server to %TEMP% directory, execute payload and gain persistence
by editing registry keys and creating a scheduled task to run payload at login.  

# Features: 
Downloads payload to TEMP directory and executes payload
to bypass windows smart screen. Disables Defender, UAC/user account control, Defender Notifications, injects Command Prompt and Microsoft Edge shortcuts with payload path (%TEMP%/payload.exe), adds a scheduled task called "WindowsDefender" for payload to be run at login and obfuscates the vbs delivery script. This tool also has a serveo function to deliver obfuscated vbs script.

# Prerequisites
Python 2.7



