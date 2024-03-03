# os.path module    --->    Sub-module of OS
#                   --->    Used to work on paths

'''
>>> import os
>>> dir(os)
['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 
 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 
'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 
'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 
'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 
'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 
'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 
'X_OK', '_AddedDllDirectory', '_Environ', '__all__', 
'__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', 
'_check_methods', '_execvpe', '_exists', '_exit', 
'_fspath', '_get_exports_list', '_walk', '_wrap_close', 
'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 
'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 
'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 
'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 
'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 
'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 
'ftruncate', 'get_exec_path', 'get_handle_inheritable', 
'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 
'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 
'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 
'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 
'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 
'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 
'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 
'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 
'statvfs_result', 'strerror', 'supports_bytes_environ', 
'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 
'supports_follow_symlinks', 'symlink', 'sys', 'system', 
'terminal_size', 'times', 'times_result', 'truncate', 
'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 
'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']


Here, we search for 'path'
>>> print(os.path.sep)
\
'''



# os.path operations:
# os.path.sep
# os.path.basename(path)
# os.path.dirname(path)
# os.path.join(path1, path2)
# os.path.split(path)      ---> Used to split the path name into a pair head and tail.
# os.path.getsize(path)    ---> in bytes
# os.path.exists(path)
# os.path.isfile(path)
# os.path.isdir(path)
# os.path.islink(path)

# Further, we will learn about getatime(access time), getctime(creation time), getmtime(modifying time), but in order to understand these, we must first understand os.path.