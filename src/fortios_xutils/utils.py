#
# Copyright (C) 2020 Satoru SATOH <satoru.satoh@gmail.com>.
# SPDX-License-Identifier: MIT
#
"""Utility functions
"""
from __future__ import absolute_import

import collections.abc
import datetime
import glob
import hashlib
import os.path
import os

import anyconfig
import jmespath


_ENCODINGS = ("utf-8", "shift-jis")


def ensure_dir_exists(filepath, subdir=None):
    """Ensure dir for given file path `filepath` exists

    :param filepath: File path might be created later
    :param subdir: Sub dir
    :return: A dir path
    """
    tdir = os.path.dirname(filepath)
    if subdir:
        tdir = os.path.join(tdir, subdir)

    if not os.path.exists(tdir):
        os.makedirs(tdir)

    return tdir


def is_str(obj):
    """
    >>> is_str(u"foo")
    True
    >>> is_str("192.168.122.1/24")
    True
    >>> import ipaddress
    >>> is_str(ipaddress.ip_interface("192.168.122.1/24"))
    False
    """
    return isinstance(obj, (str, collections.abc.ByteString))


def timestamp(date_=False):
    """Generate timestamp string.

    :param date_: datetime.datetime object or False (default)
    """
    return (date_ or datetime.datetime.now()).strftime("%F_%H_%M_%S")


def checksum(filepath, hcnstrctr=hashlib.md5, enc="utf-8"):
    """Compute the checksum of given file, `filepath`

    :raises: OSError, IOError
    """
    return hcnstrctr(open(filepath).read().encode(enc)).hexdigest()


def get_subdir(filepath):
      """
      :param filepath: Path to the input file

      >>> get_subdir("/tmp/a/b/c/d.yml")
      'c'
      >>> get_subdir("/tmp/x.json")
      'tmp'
      >>> get_subdir("/")
      ''
      >>> get_subdir("a.yml")
      ''
      """
      return os.path.split(os.path.dirname(filepath))


def try_ac_load(filepath, type_=None, encodings=_ENCODINGS):
    """
    Try to open and load `filepath` using anyconfig.load.

    :param filepath: File path to load
    :param type_: File type of the file, `filepath`
    :param encodings: Character set encodings to try

    :return:
        A mapping object or sequence objects loaded from `filepath` or None
    """
    for enc in encodings:
        try:
            with open(filepath, encoding=enc) as inp:
                return anyconfig.load(inp, ac_parser=type_)
        except UnicodeDecodeError:
            pass

    return None


def save_file(data, filepath, **ac_opts):
    """
    An wrapper for anyconfig.dump.

    :param data: Data to save
    :param filepath:  Path to output file
    :param ac_opts: Keyword arguments will be given to anyconfig.dump
    """
    ensure_dir_exists(filepath)
    anyconfig.dump(data, filepath, **ac_opts)


def search(jmespath_exp, data):
    """
    Just an wrapper for :func:`jmespath.search`

    >>> search("[].a[]",
    ...        [dict(a=[1, 2], b=2), dict(b=3, c=4), dict(a=[3,4])])
    [1, 2, 3, 4]
    >>> search("[].x", [dict(a=[1, 2], b=2)])
    []
    """
    return jmespath.search(jmespath_exp, data)


def expand_glob_paths_itr(filepaths, marker='*'):
    """
    :param filepaths: A list of file paths
    """
    for fpath in filepaths:
        if marker in fpath:
            for path in sorted(glob.glob(fpath)):
                yield path
        else:
            yield fpath

# vim:sw=4:ts=4:et:
