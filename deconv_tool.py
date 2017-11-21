"""
written by
Ioannis Athanasiadis(supernlogn)

It converts all f-strings inside python files of a root dir 
to python files with simple strings 
and stores the converted files to another dir
"""
from deconverter import deconvert_project
import argparse

prog_name = 'f-string deconverter tool'
desc = 'A tool to deconvert all f-strings in python files of your project.'
parser = argparse.ArgumentParser(prog_name, description=desc)

parser.add_argument('input_folder',
                    type=str,
                    help="A folder from which to deconvert all f-strings in its python files")

parser.add_argument('output_folder',
                    type=str,
                    help="A folder to which all deconverted python files go")

args = parser.parse_args()

if __name__ == "__main__":
  deconvert_project(args.input_folder, args.output_folder)
  # deconvert_strings_in_file('kitti.py', 'kitti_gen.py')