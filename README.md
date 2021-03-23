# var_info
**var_info** is a set of helper functions for displaying human friendly information about an object's visible attributes.

```python
from var_info import var_info, udir
from pprint import pprint as print

some_file = open('example.txt','w')

print(var_info(some_file))

["buffer -> <class '_io.BufferedWriter'>",
 'close()',
 'closed: bool -> False',
 'detach()',
 'encoding: str -> cp1252',
 'errors: str -> strict',
 'fileno()',
 'flush()',
 'isatty()',
 'line_buffering: bool -> False',
 'mode: str -> w',
 'name: str -> example.txt',
 "newlines -> <class 'NoneType'>",
 'read()',
 'readable()',
 'readline()',
 'readlines()',
 'reconfigure()',
 'seek()',
 'seekable()',
 'tell()',
 'truncate()',
 'writable()',
 'write()',
 'write_through: bool -> False',
 'writelines()']

print(udir(some_file))
 ['buffer',
 'close',
 'closed',
 'detach',
 'encoding',
 'errors',
 'fileno',
 'flush',
 'isatty',
 'line_buffering',
 'mode',
 'name',
 'newlines',
 'read',
 'readable',
 'readline',
 'readlines',
 'reconfigure',
 'seek',
 'seekable',
 'tell',
 'truncate',
 'writable',
 'write',
 'write_through',
 'writelines']
 ```


