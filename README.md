# Description

`attach` is a session manager for `dtach`.

If all you need is detachment and attachment functionality, `screen` is overkill. Unfortunately, using `dtach` requires manually managing socket files. Let `attach` manage `dtach` sessions (sockets) for you instead.

# Usage

    attach [‐option ...] [session | [command [arguments ...]]

How do I create a new session?

    attach pianobar

How do I reattach to a detached session?

    attach pianobar

What if I want the session name to be different from the command name?

    attach -s radio pianobar

How do I list sessions?

    attach

How do I delete a ghost session from a __rare__ dirty dtach exit?

    attach -L | grep pianobar | xargs rm

Is there more?

    attach --help

# Extras Directory

`attach.rb` is a [Homebrew](http://mxcl.github.com/homebrew "Homebrew") formula to be installed in `$(brew --prefix)/Library/Formula`.

`attach.usage` is a [Compleat](https://github.com/mbrubeck/compleat "Completion for human beings") completion file to be installed in `~/.compleat`.

`_attach` is a [Zsh](http://www.zsh.org) completion file to be installed somewhere in `$FPATH`.

# Multiple Windows

What if once in a blue moon, I need multiple windows, should I just revert to `screen` or `tmux`? No, there is a much simpler alternative, but more on that later. First, a few words on `screen` and `tmux`.

[GNU Screen](http://www.gnu.org/software/screen "GNU Screen") has not been updated for a couple of years and others are reluctant to adopt it since it has twisted spaghetti code that will make an Italian chef cringe. It is riddled with bugs and the configuration file syntax is attrocious. Most result to googling for other's dot files to copy/paste. However, it does have the advantage of being installed everywhere.

[TMUX](http://tmux.sourceforge.net "TMUX") is the new kid on the block, has great potential, and is installed by default on a few BSD derivatives. Though, a few years old, it is still quite buggy, especially on Mac OS X. For example, `pbpaste`, used to paste the contents of the clipboard to stdin, does not work. The patch to make `pbpaste` work will will result in _fatal: dispatch\_imsg: imsg\_read failed_ when executing `tmux attach-session`, which defeats the purpose of using tmux if one cannot reattach. It can also randomly freeze and fail to exit when the subprocess exits. There are also problems with _RPROMPT_ in ZSH being malformed and the cursor being misplaced.

# attach + dtach + dvtm = awesome

The UNIX [philosophy](http://en.wikipedia.org/wiki/Unix_philosophy) is 'Write programs that do one thing and do it well.', also known as, 'Keep it simple, stupid!' [dvtm](http://www.brain-dump.org/projects/dvtm) (Dynamic Virtual Terminal Manager) is a tiling window manager similar to X11 window managers for the console. Using `attach` with `dvtm` is simple. One does not have to worry about configuration files, in fact, there are none, nor does one have to worry about the _TERM_ environmental variable and how to get `tput colors` to output _256_. It just works.

    attach -s evil-project dvtm

# License

Copyright (c) 2011 Sorin Ionescu.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
