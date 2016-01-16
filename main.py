import sys
from bot.ircbot import IRCBot,IRCBotSettings

def main():
    if len(sys.argv) != 4:
        print("Usage: main.py <server[:port]> <channel> <nickname>")
        sys.exit(1)

    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print("Error: Erroneous port.")
            sys.exit(1)
    else:
        port = 6667
    channel = sys.argv[2]
    nickname = sys.argv[3]

    settings = IRCBotSettings(channel, "big_boys_bitch_boy_bot", server, port)

    bot = IRCBot(settings)
    bot.start()

if __name__ == "__main__":
    main()