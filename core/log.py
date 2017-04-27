# -*- coding: utf-8 -*-
import datetime


class Log:
    def __init__(self, log_file):
        self.open_file(log_file)

    def open_file(self, file_name):
        try:
            self.logs = open(file_name, "a")
            self.logs.write("Rib is being launched {}".format(datetime.datetime.now()))
        except:
            print("There was an error opening the log.txt")
            exit(0)

    def log_write(self, msg):
        self.logs.write(msg + "\n")

    def report_error(self, error):
        error = "There was an error:\t{} :{}\n".format(str(error.__class__), str(error))
        self.log_write(error)

    def close(self):
        self.logs.close()
