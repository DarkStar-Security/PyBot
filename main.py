# -*- coding: utf-8 -*-
import optparse
import asyncio
import sys

from core.log import Log
from core.bot_class import Bot


loop = asyncio.get_event_loop()

config = {"server": , "port": , "chans": ["#"]}
log = Log("logs.txt")


def exe(coro):
    return loop.run_until_complete(coro)


def authenticate():
    global test
    test = Bot(config)
    exe( test.connect() )
    data = str( exe( test.recv_data() ))
    log.log_write(data)
    exe( test.send_nick() )
    exe( test.send_user() )
    # These are done multiple times on purpose. If it's done once it may fail.
    exe( test.identify() )
    exe( test.identify() )
    exe( test.identify() )        
    exe( test.mode_set() )
    exe( test.mode_set() )
    exe( test.mode_set() )        
    receive_data(test) 

    #exe( test.send_message("Hello!", config["chans"]) )


def receive_data(bot, check=True):
    while check:
        data = str(exe(bot.recv_data()))
        """
        Armillaria: (:is now your hidden)
        Anonops: (:Global!services@anonops)
        """
        if config['server'] == 'irc.anonops.com':
        
            if data.find(':Global!services@anonops') != -1:
                bot.join()
                receive_command(bot)

                # exe( bot.register() )
                exe(bot.recv_data())
                exe(bot.identify())
                exe(bot.recv_data())
                exe(bot.mode_set())
                bot.recv_data()
                bot.join()
                exe(bot.identify())
                exe(bot.recv_data())
                exe(bot.mode_set())
                check = False
                receive_command(bot)
        elif config['server'] == 'irc.armillaria.net':
        
            if data.find(':is now your hidden') != -1:
                bot.join()
                check = False
                receive_command(bot) 


def receive_command(bot):
    while True:
        try:
            data = str(exe(bot.recv_data()))
            exe(bot.command(data))
        except KeyboardInterrupt:
            return test.sock.close(), sys.exit()


def check_input():
    parser = optparse.OptionParser("%prog -n <bot_file>")
    parser.add_option("-s", dest="server", help="irc server")
    parser.add_option("-p", dest="port", help="irc port [6697]")
    parser.add_option("-c", dest="channels", help="channels the bot should connect to")
    (options, args) = parser.parse_args()

    if not (options.server or config["server"]):
        parser.print_help()
        exit(0)

    config["server"] = options.server if options.server else config["server"]
    config["port"] = int(options.port) if options.port else 6697
    config["chans"] = options.channels.split(',') if options.channels else config["chans"]


def main():
    check_input()
    authenticate()
    authenticate()
    authenticate()

if __name__ == "__main__":
    main()
