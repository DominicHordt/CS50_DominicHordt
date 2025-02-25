from pyfiglet import Figlet
import sys

if len(sys.argv) == 1:
    figlet = Figlet()
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] not in Figlet().getFonts():
            sys.exit("Invalid usage")
        else:
            figlet = Figlet(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

print(figlet.renderText(input("Input: ")))
