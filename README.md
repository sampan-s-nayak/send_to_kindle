# Send_To_Kindle
a python script to send ebooks to kindle after converting (if required) to .mobi. can be used to send multiple files at once or a single file at a time

# Dependencies
ebook-convert cli tool must be installed

# Usage
make sure kindle is connected and mounted, and then execute s2k.py using the following flags
```
usage: s2k.py [-h] [-d] [-f] path

send ebooks to kindle (files are converted if necessary)

positional arguments:
  path        input path

optional arguments:
  -h, --help  show this help message and exit
  -d, --dir   accepts the path to the directory containing the ebook files
  -f, --file  accepts the path to the ebook file
```
# Adding to .bashrc or .zshrc
add the following line in your .bashrc or .zshrc file
```
alias s2k="<replace with path to s2k.py>"
```
now the script can be run as a command (make sure that s2k is executable, can be done using ```chmod +x s2k.py```) now you can drop the .py

```
command usage: s2k [-h] [-d] [-f] path
```

# Debugging
modify the following to make it work on your pc in case you encounter any problems
```python
# config
OUTPUT_FORMAT = '.mobi' # change it to the format you require
FORMATS_TO_IGNORE = ['mobi','azw3']
PROCESSED_FILES_PATH = os.path.join('/home',getpass.getuser(),'Processed_Ebooks') # path to the directory where the processed files are stored
KINDLE_PATH = os.path.join('/','media',getpass.getuser(),'Kindle') # path to kindle, change on windows
EBOOK_FILE_FORMATS = ['pdf','mobi','azw3','ePub','.txt','htm'] # add more if needed
```
