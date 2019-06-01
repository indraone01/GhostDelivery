# GhostDelivery

This tool creates a obfuscated .vbs script to download a payload hosted on a server to %TEMP% directory, execute payload and gain persistence
by editing registry keys and creating a scheduled task to run payload at login.  

features:
*Downloads payload to TEMP directory and executes payload
to bypass windows smart screen
*Disables Defender
*Disables UAC
*Disables Defender Notifications
*Injects Command Prompt and Microsoft Edge
shortcuts with payload path (%TEMP%/payload.exe)
*Adds scheduled task for payload to be run at login
*Obfuscates the vbs script
*Has serveo option to deliver obfuscated vbs script

