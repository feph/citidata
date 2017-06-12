# citidata
A python package to read and parse .citi data files produced by various measurement equipments.


## Status
This package is currently in alpha status but can be used to create plots etc. from measured data. If you experience parse errors with specific files or the A.01.01 format, please let me know!

## Reference
A document describing the A.01.00 standard can be found here:
http://na.support.keysight.com/plts/help/WebHelp/FilePrint/CITIfile_Format.htm

## Usage example
Examine all *.citi files in the current directory and print descriptions of their data packages and dump the independent and dependent values:
```
import citidata
import glob
all_my_files = glob.glob("*.citi")
for filename in all_my_files:
    print("=== %s ===" % filename)
    citi_file = citidata.genfromfile(filename)
    for package in citi_file.packages:
        print(package)
        print(package.indep)
        print(package.deps)
```

## Contact
Written by Philip Feuerschütz <feph@mailbox.org>
