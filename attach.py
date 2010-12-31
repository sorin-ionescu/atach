#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


"""A session manager for dtach."""

__author__ = 'Sorin Ionescu'
__email__ = 'sorin.ionescu@gmail.com'
__copyright__ = 'Copyright (c) 2010 Sorin Ionescu'
__license__ = 'MIT'
__version__ = '1.0.3'

# Changelog
#
# 2010-12-27: v1.0.3 Fixed many bugs.


# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from subprocess import call
import getopt
import os
import re
import stat
import sys
import tempfile
import textwrap

# ------------------------------------------------------------------------------
# Setup
# ------------------------------------------------------------------------------
NAME = os.path.basename(sys.argv[0])
SOCKET_DIR = "%s/dtach-%s" % (tempfile.gettempdir(), os.environ['USER'])


# ------------------------------------------------------------------------------
# Program
# ------------------------------------------------------------------------------
def list_sessions(full_path=False):
    """
    Lists created sessions.

    Note: Ghost sessions may be listed if dtach did not cleanly exit
      and must be deleted manually.
    """
    regex = re.compile(r'^(.+)\.dtach$')
    if not os.path.exists(SOCKET_DIR):
        return
    for session in os.listdir(SOCKET_DIR):
        match = regex.match(session)
        if match:
            if full_path:
                print(os.path.join(SOCKET_DIR, session))
            else:
                print(match.group(1))

def attach_session(options, dtach_options):
    """
    Attaches to an existing session.

    Arguments:
    options -- the script options.
    dtach_options -- the dtach options.
    """
    session_socket = socket_path(options['session'])
    if os.path.exists(session_socket) \
        and stat.S_ISSOCK(os.stat(session_socket).st_mode):
        os.execvp('dtach', ['dtach', '-a', session_socket] + dtach_options)
    else:
        sys.stderr.write(
            "%s: session '%s' does not exit.\n" % (NAME, options['session']))
        sys.exit(1)

def create_session(options, dtach_options, command):
    """
    Creates or attaches to an existing session.

    Arguments:
    options -- the script options.
    dtach_options -- the dtach options.
    command -- the command dtach will execute.
    """
    os.execvp('dtach', ['dtach', '-n' if options['detached'] else '-A',
        socket_path(options['session'])] + dtach_options + command)

def socket_path(name):
    """
    Returns the full path to a socket.

    Arguments:
    name -- the session name for which to return a socket.
    """
    return "%s/%s.dtach" % (SOCKET_DIR, name)

def print_version():
    """Prints version and license information."""
    sys.stderr.write(textwrap.dedent('''\
        %(prog)s %(version)s

        %(copyright)s

        This program is free software. You may modify or distribute it',
        under the terms of the MIT License.\n''' % {'prog': NAME,
            'version': __version__, 'copyright': __copyright__}))

def print_help():
    """Prints usage information and available options."""
    sys.stderr.write(textwrap.dedent('''\
        Usage: %(prog)s [‐option ...] [session | [command [arguments ...]]

        Options:
            -l, --list             List sessions.
            -L, --sockets          List sockets.
            -s, --session=NAME     Set the session name.
            -c, --char=C           Set the detach character (default: ^\).
            -r, --redraw=METHOD    Set the redraw method (none, ctrl_l, or winch).
            -d, --detached         Start the session detched.
            -D, --no-detach        Disable detaching.
            -Z, --no-suspend       Disable suspending.
            -v, --version          Display version and copyright.
            -h, --help             Display this help.

        Report bugs to <sorin.ionescu@gmail.com>.\n''') % {'prog': NAME})

def parse_argv():
    """
    Parses arguments.

    Returns:
    options -- the script options.
    dtach_options -- the dtach options.
    command -- the command.
    """
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            'lLs:c:r:dDZvh',
            ['list', 'sockets', 'session=', 'char=', 'redraw=',
                'detached', 'no-detach', 'no-suspend', 'version', 'help'])
    except getopt.GetoptError, err:
        sys.stderr.write(
            "%s: %s\n" % (NAME, str(err)))
        sys.exit(1)
    options = {'session': None, 'detached': False}
    dtach_options = []
    for opt, arg in opts:
        if opt in ('-l', '--list'):
            list_sessions(False)
            sys.exit(0)
        elif opt in ('-L', '--sockets'):
            list_sessions(True)
            sys.exit(0)
        elif opt in ('-s', '--session'):
            options['session'] = arg
        elif opt in ('-c', '--char'):
            dtach_options.append('-e')
            dtach_options.append(arg)
        elif opt in ('-r', '--redraw'):
            dtach_options.append('-r')
            dtach_options.append(arg)
        elif opt in ('-d', '--detached'):
            options['detached'] = True
        elif opt in ('-D', '--no-detach'):
            dtach_options.append('-E')
        elif opt in ('-Z', '--no-suspend'):
            dtach_options.append('-z')
        elif opt in ('-v', '--version'):
            print_version()
            sys.exit(0)
        elif opt in ('-h', '--help'):
            print_help()
            sys.exit(0)
    return options, dtach_options, args

def main():
    """
    A `main` in Python? Ha, ha!

    Note: Switches purposely differ from dtach for clarity and memorability.
    """
    return_code = call('which dtach &>/dev/null', shell=True)
    if return_code != 0:
        sys.stderr.write("%s: dtach not found.\n" % (NAME,))
        sys.exit(1)

    if not os.path.exists(SOCKET_DIR):
        os.mkdir(SOCKET_DIR)

    options, dtach_options, command = parse_argv()
    if options['session'] and not len(command):
        attach_session(options, dtach_options)
    elif len(command):
        if not options['session']:
            options['session'] = command[0]
        create_session(options, dtach_options, command)
    else:
        list_sessions(False)

# This file is not meant to be sourced.
if __name__ == '__main__':
    main()

