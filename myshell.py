#!/usr/bin/python3
# Using python 3.6.7
# William O'Hanlon - 17477494


from cmd import Cmd
import sys, os
import subprocess
import shlex
from pathlib import Path
import threading, time, multiprocessing

global file_pos
global og_file_pos
global ENDC
global colour_blue
global colour_red
global colour_green

class MyPrompt(Cmd):
    def do_quit(self, args):
        print("Quitting")
        raise SystemExit

    # Sorter for sorting how files will be printed using dir
    # Sorts alphabetically like unix, if there are hidden files then they are sorted by their second character, not the dot
    def sorter(self, file):
        cond = file.split(".")
        if len(cond) > 1:
            return cond[1]
        return cond[0]

    def do_dir(self, args):
        global file_pos
        try:
            tmp_dir = file_pos
            hidden = False     # Condition on whether or not to print hidden files

            if len(args.strip()) > 0:
                if args.split()[-1] == "h":
                    hidden = True
                    args = "".join(args[:-1])  # Enabling hidden files

                tmp_dir += "/" + args.strip()  # Changing which directory list file contents from i.e. if a directory is provided to dir, show contents of this directory not current directory

            files = os.listdir(tmp_dir)
            files = sorted(files, key=self.sorter)
            for name in files:
                if name[0] != ".": # Filter out hidden files
                    print(name)

                elif hidden: # Print hidden files if asked for
                    print("{:}{:}{:}".format(colour_green, name, ENDC))
        except OSError:
            print("dir: cannot access {:s}: No such file or directory".format(args))

    def do_cd(self, args):
        global file_pos
        try:       
            if len(args) == 0 or args == '~': # Empty command i.e. just cd. Return to hoe directory
                try:
                    tmp_dir = Path.home()
                    os.chdir(tmp_dir)
                except PermissionError:
                    print("Permission Denied")

            else:
                tmp_dir = file_pos + "/" + args

                # Check if directory exists
                # If so change file position

                os.chdir(tmp_dir)

            file_pos = os.getcwd()

        except FileNotFoundError:
            # If not don't change file position
            print("cd: cannot access {:}: No such file or directory".format(args))

        except PermissionError:
            print("cd: cannot access {:}: Permission denied".format(args))

        except NotADirectoryError:
            print("cd: cannot access {:}: No such directory".format(args))

        except:
            print("cd: cannot access {:}: An error occured".format(args))

    def complete_cd(self, text, line, begidx, endidx):
        # begidx is the beginning index of the word to match in the complete line
        # endidx is the end index
        # Auto complete for cd
        return [file for file in os.listdir(file_pos) if file.startswith(text)]

    def do_pwd(self, args):
        print(file_pos)

    def do_clr(self, args): # Args should be empty for clr
        if len(args) == 0:
            sys.stdout.write("\033c")

        else:
            print("clr does not have an option: '{:}'".format(args))

    def do_echo(self, args):
        cond = True
        while cond:
            try:
                args = " ".join(shlex.split(args))

            except ValueError: # If args is empty string
                # Uneven number of quotations in inputted string i.e. unclosed quotations
                # echo asks for input, appending input output until the right quotation is entered in order to clse quotation
                sys.stdout.write(">") # cursor before input
                # Add input to args until shlex.split(args) doesn't throw a ValueError i.e. required quotation entered
                s = input()
                args = args + "\n" + s # Add input line by line

            else:
                cond = False
        
        print(args)
            

    def do_myshell(self, batchfile):
        if batchfile.strip() == "": # If no file is given
            print("Please give name of batch file")
            batchfile = input()

        try:
            with open(file_pos + "/" + batchfile, "r") as f:
                cmdList = f.readlines()
                for cmd in cmdList:
                    cmd = (cmd.strip()).split()
                    if len(cmd) > 0:                 # Empty list checker
                        self.onecmd(" ".join(cmd)) # Run command
                        # If the command is wrong, program prints command name not found

        except FileNotFoundError:
            print("myshell: cannot access {:}: No such file in directory {:}".format(batchfile, file_pos))

    def do_help(self, args):
        try:
            cond = False
            if len(args) == 0: # If no command given i.e. general help file
                cond = True

            file = og_file_pos + "/" + "readme"
            
            if cond: # If no commad given i.e. just looking for readme
                with open(file, "r") as f:
                    ts = os.get_terminal_size() # Get terminal size first, for amount of lines to print
                    counter = 0                 # Keep count of number of lines printed in order to only peint enough lines to file screen
                    a = f.readlines()
                    for line in a:
                        if counter <= ts.lines - 10: # If room on screen print line 
                            counter += 1
                        else:
                            # Screen full, wait for enter to be pressed to continue
                            print("-------------\nPress Enter To Continue\n-------------")
                            enter = input()
                            while enter != "":
                                enter = input()
                            counter = 0
                        print(line.rstrip())
                    wait = input()   # Wait for any input from the user to exit
                    self.do_clr("")  # Clear screen after readme

            else:
                command = 'do_{:}'.format(args.strip())
                if hasattr(self, command):  # Check if there's a do command for this argument
                    # Find args.strip() part in readme file
                    self.printHelp(args.strip(), file)

                else:
                    print("Help not available for given command.\nTo access help files for commands, type 'help command'.")


        except:
            print("Help not available for given command.\nTo access help files for commands, type 'help command'.")

    def printHelp(self, command, file):
        # Finding the part of the readme which corresponds to the given command
        with open(file, "r") as f:
            a = f.read().split("NAME:\n-- ")  # Splitting on this header as its in front of the beginning of every command help description
            for i in range(1, len(a)):
                description = a[i]
                if command == description[:len(command)]:
                    self.do_clr("")       # Clear screen and print help for command
                    print(description)
                    return
            f.close()
            # If the program reaches here then command was not found 
            print("Help not available for given command: {:}".format(command))


    def do_environ(self, args):
        if len(args) == 0:
            d = os.environ
            for key in d:
                print("{:} = {:}".format(key, d[key]))

        else:
            print("environ does not have an option: '{:}'".format(args))

    def do_pause(self, args):
        if len(args) > 0:
            print("pause does not have an option: '{:}'".format(args))
            return None   # Exit pause if argument(s) given

        # Pause shell until the enter key is pressed
        # Clear screen
        self.do_clr("")
        print("The shell has been paused, to unpause press the enter key.")
        key = input()
        if len(key) == 0:
            return None

        else:
            self.do_pause("")

    def emptyline(self, *args):
        # Exists to do nothing when the enter key is pressed with no command
        # Without this the last executed command will execute again 
        pass

    def precmd(self, line):
        if len(line) == 0:
            return "" # For when there's no command

        redirect_cmd = {"dir":1, "environ":1, "echo":1, "help":1} # The only commands which should support i/o redirection
        line_lst = line.split()
        
        # Checks and handling for redirection
        redirect = {">":True, ">>":False} # ">" for output and "<" for input 
        index = [i for i in range(len(line_lst)) if line_lst[i] in redirect] # index of redirection arrow (> or >>) in line_lst ( line.split() )
        
        if line_lst[0] in redirect_cmd and len(index): # i/o redirection, check if i/o redirection supported by the command
            try:
                values = (index[0], redirect[line_lst[index[0]]]) # Getting whether > or >>, has to be one or other
                # index[0] is index of > or >>
                # values = (index of redirection arrow, boolean for whether > or >>)
                
                if not values[1]:
                    sys.stdout = open(line_lst[index[0] + 1], 'a+') # Sets standard output to be file, file always located after >>
                    # Appends data to file if data in it

                else:
                    sys.stdout = open(line_lst[index[0] + 1], 'w') # Sets standard output to be file, file always located after >, overwrites data in file
                return " ".join(line_lst[:index[0]] + line_lst[index[0] + 2:]) # Pass command to corresponding function, minus the redirection arrow and the output file name

            except: # Should never happen
                print("An error has occured")
                return ""
        else:
            return line

    def parseline(self, line):
        """Parse the line into a command name and a string containing
        the arguments.  Returns a tuple containing (command, args, line).
        'command' and 'args' may be None if the line couldn't be parsed.
        Executed within onecmd, deteremines what's passed to do methods.
        Changed parsing so cmd* isn't interpretted as cmd
        """
        if not line: # empty line i.e. enter pressed, cmd set up to execute last executed command when this happens but I've overwritten that
            return None, None, line

        # Find first whitespace and use it to split the line into command and args
        i, n = 0, len(line)
        while i < n and line[i] != " ":
            i += 1
        
        command, arg = line[:i], line[i:].strip()

        if len(line) > 0:
            if line[-1] == '&': # Background processes
                if hasattr(self, 'do_{:}'.format(command.strip("&"))):
                    try:
                        run = 'do_{:}'.format(command.strip("&"))
                        getter = getattr(self, run)
                        thread = threading.Thread(target=getter, args=(arg.strip("&"),), name=run)
                        thread.daemon = True    # Daemonize thread
                        thread.start()
                        return None, None, None  # Sends onecmd to emptyline function, nothing happens in shell

                    except:
                        print("An error has occured")
                        return None, None, line

                else:
                    try:
                        run = 'default'
                        getter = getattr(self, run)
                        thread = threading.Thread(target=getter, args=("".join(line.split("&")),), name=run)
                        thread.daemon = True    # Daemonize thread
                        thread.start()
                        return None, None, None  # Sends onecmd to emptyline function, nothing happens in shell

                    except:
                        print("An error has occured")
                        return None, None, line

        return command, arg, line # these variables get passed to onecmd


    def postcmd(self, stop, line): # Stop is the return value of onecmd, when a cmd is executed precmd, onecmd, corresponding do method, postcmd are all executed respectively
        sys.stdout = sys.__stdout__ # Reset stdout
        sys.stdin = sys.__stdin__   # Reset stdin
        self.prompt = '{:}:~{:} $ {:}'.format(colour_blue, file_pos, ENDC)
        # If file path changes change path show on screen behind cursor

    def completedefault(self, text, line, begidx, endidx):
        # begidx is the beginning index of the word to match in the complete line
        # endidx is the end index
        # Auto complete for cd
        return [file for file in os.listdir(file_pos) if file.startswith(text)]

    def default(self, args): # Runs if an unknown command is entered
        try:
            # Will run any system binary
            # Commands which are found not to have do methods are sent here where they are attempted to a run as processes
            # Therefore any system binary can be run in the shell, including ls except for unix commands which have counter part do methods with the same name i.e. dir
            # Handling processes and external applications
            args = args.split()
            
            # Process handling
            if len(args) == 1:
                p = subprocess.Popen(args[0]) 
            else:
                p = subprocess.Popen(args)
            p.wait()

        except:
            print("{:s}: does not exist as a command".format(" ".join(args))) # If the wrong command is entered i.e. one which a function is not set up for

if __name__ == '__main__':
    file_pos = os.getcwd() # Initiate file_pos as current path
    og_file_pos = os.getcwd() # Location of shell and help files
    prompt = MyPrompt()
    # colour_blue for prompt
    colour_blue = '\033[94m'
    colour_red = '\033[91m'
    colour_green = '\033[93m'
    ENDC = '\033[0m'
    prompt.prompt = '{:}:~{:} $ {:}'.format(colour_blue, file_pos, ENDC)
    prompt.cmdloop("Starting prompt...")
