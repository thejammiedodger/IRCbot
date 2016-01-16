#! /usr/bin/env python


"""
IRC bot that downloads and displays posts from online imageboard to
via private messages
"""
import json
import urllib.request
import irc.bot
import irc.strings
from irc.client import Event, ServerConnection
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

class IRCBotSettings:
    def __init__(self, channel, nickname, server, port=6667):
        self.LOCATION = [(server, port)]
        self.CHANNEL = channel
        self.NICK = nickname
        self.SERVER = server
        self.PORT = port


class IRCBot(irc.bot.SingleServerIRCBot):
    """
    Implements the bot interface provided by the irc module for accessing
    single servers.
    """
    def __init__(self, settings:IRCBotSettings):
        """
        Creates connection to irc server by calling superclass constructor.
        :param settings: IRCBotSettings instance containing connection settings
        :return: new IRCBot instance
        """
        super(IRCBot, self).__init__(settings.LOCATION, settings.NICK, settings.NICK)
        self.channel = settings.CHANNEL

    def on_nicknameinuse(self, conn:ServerConnection, event:Event)->str:
        """
        Trigered if username is take. Changes the username by appending
        69 to it
        :param conn: ServerConnection to irc server
        :param event: Event
        :return: str containing new username
        """
        conn.nick(conn.get_nickname() + "69")

    def on_welcome(self, conn:ServerConnection, event:Event):
        """
        Triggered when a welcome message is received meaning
        that the server connections has been established. Joins the channel
        specified by self.channel.
        :param conn: ServerConnection
        :param event: Event
        :return: None
        """
        conn.join(self.channel)

    def on_privmsg(self, conn:ServerConnection, event:Event):
        """
        Triggered when a private message has been received. Executes the
        appropriate command. This is one of the primary ways the bot interacts
        with users.
        :param conn: ServerConnection
        :param event: Event
        :return: None
        """
        self.do_command(event, event.arguments[0])

    def on_pubmsg(self, conn:ServerConnection, event:Event):
        """
        Triggered when a public message is received. The other significant
        way of interacting. Checks with the users nickname is allowed to execute
        command and then passes the command to the do_command method.
        :param conn: ServerConnection
        :param event: Event
        :return: None
        """

        a = event.arguments[0].split(":", 1)
        if len(a) > 1 and (irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()) or irc.strings.lower(a[0]) == "bb"):
            self.do_command(event, a[1].strip())
        return

    def on_dccmsg(self, conn:ServerConnection, event:Event):
        """
        Triggered when a non-chat DCC message has been received. DCC messages
        are raw bytes so there's potential for using this for file transfer. Currently
        for testing we merely decode them as text messages
        :param conn: ServerConnection
        :param event: Event
        :return:None
        """
        text = event.arguments[0].decode('utf-8')
        conn.privmsg("You said: " + text)

    def on_dccchat(self, conn:ServerConnection, event:Event):
        """

        :param conn: ServerConnection
        :param event: Event
        :return:None
        """
        if len(event.arguments) != 2:
            return
        args = event.arguments[1].split()
        if len(args) == 4:
            try:
                address = ip_numstr_to_quad(args[2])
                port = int(args[3])
            except ValueError:
                return
            self.dcc_connect(address, port)

    def do_command(self, event:Event, cmd):
        """
        Executes the specified command.
        :param event: Event
        :param cmd: str
        :return: None
        """
        print(cmd)
        nick = event.source.nick
        conn = self.connection



        if nick != "bigboy69":
            return
        if cmd == "disconnect":
            self.disconnect()
        elif cmd == "i":
            conn.privmsg(self.channel, ">implying")
        elif cmd == "m":
            conn.privmsg(self.channel, "Mediocre.")
        elif cmd[:6].lower() == "insult":
            url = 'http://quandyfactory.com/insult/json'
            with urllib.request.urlopen(url) as page:
                try:
                    contents = page.read()
                    insult = json.loads(contents.decode())["insult"].lower()
                    insult = cmd[7:]+" "+(insult if cmd[7:].find("bigboy")==-1 else " a bitch doesn't insult his owner.")

                    conn.privmsg(self.channel, insult)
                except TypeError:
                    print("type error")
        elif cmd == "die":
            self.die()
        elif cmd == "post":
            conn.notice(nick, "Hello")
        elif cmd == "dcc":
            dcc = self.dcc_listen()
            conn.ctcp("DCC", nick, "CHAT chat %s %d" % (
                ip_quad_to_numstr(dcc.localaddress),
                dcc.localport))
        elif cmd=="get":
            pass
        else:
            conn.notice(nick, "Not understood: " + cmd)


