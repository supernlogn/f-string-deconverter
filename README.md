# f-string_deconverter
convert python f-string to older and compatible python string

This project provides a tool to convert:
* python expression with f-strings to expression with simple python string
* python files with f-strings to files with simple python strings
* folders of python files with f-strings to folders of python files with simple python strings
 
### Dependencies & Libraries
1. re
2. os
3. itertools

All are provided by the python 3 installation

### Examples
###### convert string expression
old_expr:
```python 
    s = f"{alpha},{beta},{gamma:06d}" 
``` 
to new_expr:
```python 
    s = "{},{},{:06d}".format(alpha, beta, gamma) 
```

```python
    from deconverter import deconvert_string
    old_expr = 's = f"{alpha},{beta},{gamma:06d}"'
    new_expr = deconvert_string(old_expr)
```

###### convert files:
file1.py to file2.py
```python
    from deconverter import deconvert_strings_in_file
    deconvert_strings_in_file('file1.py', 'file2.py')
```ndencies & Libraries

    re
    os
    itertools All provided by the pyth

###### convert folders
folder1 to folder2
```python
    from deconverter import deconvert_project
    deconvert_project(folder1, folder2)
```

### Use case
vod-converter: [https://github.com/umautobots/vod-converter] uses python3.6 f-strings
               can be converted just by running this script:
```Shell
python3 deconv_tool.py /full/path/to/vod-converter /full/path/to/vod-converter
```

After this command vod-converter can be executed with python3.5 which is python3 in
older python distros. 

Users can also import the deconverter.py as a module or use the deconv_tool.py.

#### Note
This repo is still under development/testing,
if you find any bugs, please report them to the issues tab.

Thanks for using it!!!

