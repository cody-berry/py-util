reset = "\033[0m"
bold = "\033[1m"
faint = "\033[2m"
italic = "\033[3m"
underline = "\033[4m"
strikethrough = "\033[9m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
orange = "\033[38;2;255;153;0m"
yellow = "\033[33m"
blue = "\033[34m"
indigo = "\033[38;2;8;73;158m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
blackBackground = "\033[40m"
redBackground = "\033[41m"
greenBackground = "\033[42m"
orangeBackground = "\033[48;2;255;153;0m"
yellowBackground = "\033[43m"
blueBackground = "\033[44m"
indigoBackground = "\033[48;2;8;73;158m"
magentaBackground = "\033[45m"
cyanBackground = "\033[46m"
whiteBackground = "\033[47m"
resetForeground = "\033[39m"
resetBackground = "\033[49m"
brightWhite = "\033[1;37m"
offWhite = "\033[0;37m"
creamWhite = "\033[1;33m"
ivoryWhite = "\033[1;93m"
brightWhiteBackground = "\033[1;47m"
offWhiteBackground = "\033[0;47m"

print(f"{bold}Bold{reset} "
      f"{faint}Faint{reset} "
      f"{italic}Italic{reset} "
      f"{underline}Underline{reset} "
      f"{strikethrough}Strikethrough{reset} Reset")
print(f"Foreground: {black}B{reset}{red}R{reset}{orange}O{reset}"
      f"{yellow}Y{reset}{green}G{reset}{blue}U{reset}{indigo}I{reset}"
      f"{cyan}C{reset}{magenta}M{reset}{white}W{resetForeground} ResetForeground")
print(f"Background: "
      f"{blackBackground}B{reset}"
      f"{redBackground}R{reset}"
      f"{orangeBackground}O{reset}"
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
print(f"Background colors: "
      f"{brightWhiteBackground}Bright white{reset} "
      f"{offWhiteBackground}Off white{reset} \n"
      f"Foreground colors: "
      f"{brightWhite}Bright white{reset} "
      f"{offWhite}Off white{reset} "
      f"{creamWhite}Cream white{reset} "
      f"{ivoryWhite}Ivory white{reset}")
