import sys

class OutputRedirector():
    def __init__(self, fp):
        self.fp = fp
    def write(self ,s):
        self.write(s)
    def writeline(self, line):
        self.writeline(line)
    def flush(self):
        self.flush();


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)