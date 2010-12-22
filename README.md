# Description

`attach` is a session manager for `dtach`.

If all you need is detachment and attachment functionality, `screen` is overkill. Unfortunately, using `dtach` requires manually managing socket files. Let `attach` manage dtach sessions (sockets) for you instead.

# Usage

    attach [OPTION]... [SESSION | COMMAND]

How do I create a new session?

    attach pianobar

How do I reattach to a session?

    attach pianobar

What if I want the session name to be different from the command name?

    attach -s radio pianobar

How do I list sessions?

    attach

How do I delete a ghost session from a __rare__ dirty dtach exit?
    
    attach -L | grep pianobar | xargs rm

Is there more functionality?

    attach --help

# License

Copyright (c) 2010 Sorin Ionescu. 

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
