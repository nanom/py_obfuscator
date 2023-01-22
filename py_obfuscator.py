#!/usr/bin/env python3.9

import argparse
from modules.m_obfuscate import Obfuscate

def getArguments():
    ap = argparse.ArgumentParser(
        prog="./py_obfuscate.py",
        description="PyObfuscator is a basic command line tool that allows you to obfuscate Python code.", 
    )
    req_args = ap.add_argument_group("required arguments")
    req_args.add_argument("-i","--input_path", 
        required=True,
        type=str, 
        help="Python filename or program directory name."
    )
    ap.add_argument("-o","--output_dir", 
        required=False,
        type=str,
        default="output",
        help="Name of te output directory where the obfuscated program will be saved (default: %(default)s)."
    )
    ap.add_argument("-v","--program_vars", 
        required=False,
        default=None,
        type=str,
        help="Please list at least three variable names where the program will be split (eg: n1,n2,n3,...,nN). Otherwise, random names will be generated for you."
    )
    return vars(ap.parse_args())


if __name__ == '__main__':
    args = getArguments()

    program_vars = args.get('program_vars')
    if program_vars is not None:
        program_vars = [var_name for var_name in program_vars.split(",") if var_name != ""]

    ob = Obfuscate(
        input_path = args.get('input_path'),
        output_dir_name = args.get('output_dir'),
        program_vars = program_vars
        
    )
    ob.execute()