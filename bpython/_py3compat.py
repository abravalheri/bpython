# The MIT License
#
# Copyright (c) 2012 the bpython authors.
# Copyright (c) 2015 Sebastian Ramacher
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


"""
    Helper module for Python 3 compatibility.

    Defines the following attributes:

    - py3: True if the hosting Python runtime is of Python version 3 or later
"""


import sys
import threading

py3 = sys.version_info[0] == 3


if py3:

    def try_decode(s, encoding):
        return s


else:

    def try_decode(s, encoding):
        """Try to decode s which is str names. Return None if not decodable"""
        if not isinstance(s, unicode):
            try:
                return s.decode(encoding)
            except UnicodeDecodeError:
                return None
        return s


if py3:

    def is_main_thread():
        return threading.main_thread() == threading.current_thread()


else:

    def is_main_thread():
        return isinstance(threading.current_thread(), threading._MainThread)
