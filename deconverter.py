"""
written by
Ioannis Athanasiadis(supernlogn)
functions for deconverting f-strings inside expressions to simple python strings
"""
import re
import os
from itertools import chain


__all__ = [ 'deconvert_string',
            'deconvert_strings_in_file',
            'deconvert_project']

def deconvert_string(s, sep_space=1):
  """Deconverts a f-string of python3.6 and beyond to a simple python string 
     Args:
        s: f-string to deconvert
        sep_space: space between commas of format arguments
     Return:
        deconverted string in the old python3 string format 
        
        Example: "{alpha}, {beta}, {f(gamma)}" 
          deconverts to 
                 "{}, {}, {}".format(alpha, beta, f(gamma))
  """
  in_arg = False
  in_formating = False
  special_character = False
  buffers = {}
  b1 = "main_string"
  b2 = "arguments"
  buffers[b1] = ""
  buffers[b2] = ""
  sep = ',' + ' '*sep_space
  current_buffer = b1

  for c in s:
    if c == '\\':
      special_character = True
    elif special_character:
      special_character = False
    elif c == '{':
      in_arg = True
      current_buffer = b1
    elif c == '}' and in_arg:
      in_arg = False
      in_formating = False
      buffers[b2] += sep
      current_buffer = b1
    elif c == ':' and in_arg:
      current_buffer = b1
      in_formating = True
    elif in_formating and in_arg:
      current_buffer = b1
    elif in_arg:
      current_buffer = b2
    else:
      current_buffer = b1
    buffers[current_buffer] += c

  last_char = ""
  if not buffers["main_string"] == "":
    if buffers["main_string"][-1] == '\n':
      last_char = '\n'
      buffers["main_string"] = buffers["main_string"][:-1] 
  if not buffers["arguments"] == "":
    buffers["arguments"] = buffers["arguments"][:-len(sep)]
  
  if buffers["arguments"] == "":
    return buffers["main_string"] + last_char
  else:
    return buffers["main_string"] + ".format(" + buffers["arguments"] + ")" + last_char


def deconvert_strings_in_file(rd_file_p, wr_file_p):
  """Deconverts all strings in a file
    Descr:
      Produces a file specified by wr_file_p which is
      the same as rd_file_p but with all f-strings deconverted to normal strings
    Args:
      rd_file_p: path of input file to deconvert
      wr_file_p: path of output file of deconvertion
  """
  with open(rd_file_p, "r") as rd_file:
    file_data = rd_file.read()
    with open(wr_file_p, "w") as wr_file:
      patern1 = re.compile('[f]{1,1}["]{1,1}[\s\S]*?[!\\]+["]{1,1}')
      patern2 = re.compile('[f]{1,1}[\']{1,1}[\s\S]*?[!\\]+[\']{1,1}')
      f_strings = chain(re.finditer(patern1, file_data), 
                        re.finditer(patern2, file_data))
      total_f_strings = [(s.start(), s.end()) for s in f_strings]
      total_f_strings.sort(key= lambda x: x[1])
      print(total_f_strings)
      i = 0
      for f_str in total_f_strings:
        start = f_str[0]
        end = f_str[1]
        wr_file.write(file_data[i:start])
        wr_file.write(deconvert_string(file_data[start+1:end]))
        i = end
      wr_file.write(file_data[i:])

def make_chain_dirs(file_path):
  """Create all directories above a file path"""
  if(file_path.rfind('/') == -1):
    return
  folder_path = file_path[:file_path.rfind('/')]
  try: 
    os.makedirs(folder_path)
  except OSError:
    if not os.path.isdir(folder_path):
      raise

def deconvert_project(prj_root_fold_in, prj_root_fold_out):
  """deconvert recursively all files inside a directory
    CAUTION:
      paths can only be full unix-like paths.
  """
  for root, dirs, files in os.walk(prj_root_fold_in):
    for file_rd in files:
      if file_rd.endswith('.py'):
        file_rd = root + "/" + file_rd
        file_wr = file_rd.replace(prj_root_fold_in, prj_root_fold_out)
        print(file_rd,"--->", file_wr)
        make_chain_dirs(file_wr)
        deconvert_strings_in_file(file_rd, file_wr)
