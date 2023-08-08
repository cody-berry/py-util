reset = "\033[0m"
bold = "\033[1m"
faint = "\033[2m"
italic = "\033[3m"
underline = "\033[4m"
strikethrough = "\033[9m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
indigo = "\033[38;2;8;73;158m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
blackBackground = "\033[40m"
redBackground = "\033[41m"
greenBackground = "\033[42m"
yellowBackground = "\033[43m"
blueBackground = "\033[44m"
indigoBackground = "\033[48;2;8;73;158m"
magentaBackground = "\033[45m"
cyanBackground = "\033[46m"
whiteBackground = "\033[47m"
resetForeground = "\033[39m"
resetBackground = "\033[49m"

print(f"{bold}Bold{reset} "
      f"{faint}Faint{reset} "
      f"{italic}Italic{reset} "
      f"{underline}Underline{reset} "
      f"{strikethrough}Strikethrough{reset} Reset")
print(f"Foreground: {black}B{reset}{red}R{reset}{yellow}Y{reset}"
      f"{green}G{reset}{blue}U{reset}{indigo}I{reset}{cyan}C{reset}"
      f"{magenta}M{reset}{white}W{resetForeground} ResetForeground")
print(f"Background: "
      f"{blackBackground}B{reset}"
      f"{redBackground}R{reset}"
      f"{yellowBackground}Y{reset}"
      f"{greenBackground}G{reset}"
      f"{blueBackground}U{reset}"
      f"{indigoBackground}I{reset}"
      f"{cyanBackground}C{reset}"
      f"{magentaBackground}M{reset}"
      f"{whiteBackground}W{resetBackground} ResetBackground"
      )
print(f"Mixing: "
      f"{red}{whiteBackground}RedForegroundWhiteBackground{reset} "
      f"{green}{blueBackground}GreenForegroundBlueBackground{reset}")
