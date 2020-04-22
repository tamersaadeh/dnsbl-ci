#!/usr/bin/env python3
#
# Requires: Python 3
#
# This script takes as input the folder produced by `convertlist.py`
# and builds the "list hosting" repo in the specified output path.
#
# Copyright (c) 2020 Tamer Saadeh
# Copyright (c) 2018 justdomains contributors (https://github.com/justdomains)
# MIT License (https://github.com/tamersaadeh/dnsbl-ci/LICENSE)
#

import argparse
import json
import os
import subprocess

from liquid import Liquid


def make_safe_dict(obj):
    if isinstance(obj, dict):
        return {k.lower().replace(' ', '_'): make_safe_dict(v) for k, v in obj.items()}
    elif isinstance(obj, (list, set, tuple)):
        t = type(obj)
        return t(make_safe_dict(o) for o in obj)
    else:
        return obj


def generate_file(details_file, template_file, output_file, base_url, log_level=''):
    with open(details_file) as f:
        _lists = json.load(f)
    _lists = make_safe_dict(_lists)
    liq = Liquid(template_file, liquid_from_file=True, liquid_loglevel=log_level)
    rendered = liq.render(lists=_lists, base_url=base_url)
    with open(output_file, 'w') as f:
        f.write(rendered)


if __name__ == '__main__':
    # Retrieve the input path and output path as arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to the output folder produced by convertlist.py")
    parser.add_argument("output_path",
                        help="path to a desired output folder in which the list hosting repo's files will be built")
    parser.add_argument("-b", "--base-url", required=True,
                        help="the base public URL at which the contents of the repo/ folder will be accessible (once separately uploaded) - this is used for properly forming README list download links")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()

    input_lists_path = os.path.join(args.input_path, "lists/")  # type: str

    # Ensure that the output directory exists
    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)

    # rsync the lists folder
    if args.verbosity >= 1:
        print("Syncing: {!s} -> {!s}".format(input_lists_path, os.path.join(args.output_path, "lists/")))
    rsync_call_array = ["rsync", "-avh", input_lists_path, os.path.join(args.output_path, "lists/"), "--delete"]
    if args.verbosity >= 2:
        print("\t{!s}".format(" ".join(rsync_call_array)))
    rsync_output = subprocess.check_output(rsync_call_array, universal_newlines=True)
    if args.verbosity >= 2:
        for line in rsync_output.split('\n'):
            if len(line.strip()) > 0:
                print("\t" + line)

    details_file = os.path.join(args.input_path, 'details.json')

    if args.verbosity >= 1:
        print("Building: {!s}".format("README.md"))
    generate_file(os.path.join(args.input_path, 'details.json'), os.path.abspath('./templates/README.md'),
                  os.path.join(args.output_path, 'README.md'), args.base_url, log_level=args.verbosity)
    if args.verbosity >= 1:
        print("Building: {!s}".format("LICENSE"))
    generate_file(os.path.join(args.input_path, 'details.json'), os.path.abspath('./templates/LICENSE'),
                  os.path.join(args.output_path, 'LICENSE'), args.base_url, log_level=args.verbosity)

    print("Finished building repo in: {!s}".format(args.output_path))
