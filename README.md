## Executes a program with modified PATH environment

### What is this?

This example modifies the Windows's PATH environment and executes specified program.

### How useful is this?

This can make it easy that a program runs in the isolated environment.



### How to use?

Get the file from Git.


```cmd
> git clone https://github.com/rubyu/path-override.git
```

```cmd
> cd path-override
```

Here we will try to make an Anaconda environment named `IsolatedEnv`, for example.

```cmd
> conda create -n IsolatedEnv python=2.7
```

Let's try to activate it.

```cmd
> call %userprofile%\Anaconda3\Scripts\activate.bat %userprofile%\Anaconda3\envs\IsolatedEnv
```

If it goes well, let's save the PATH in a file so as not to forget it.

```cmd
> ECHO %PATH% > path.txt
```

There is nothing to do in this environment anymore. Let's deactivate.

```cmd
> deactivate
```

and, then call the executable file in `IsolatedEnv`. 
Please note that `python.exe` exists below the folder `%userprofile%\Anaconda3\envs\IsolatedEnv`.

```cmd
> path-override.py path.txt %userprofile%\Anaconda3\envs\IsolatedEnv\python.exe --version
```

The result is the following.

```
exec_file: C:\Users\user\Anaconda3\envs\IsolatedEnv\python.exe
path_file: path.txt
args: ['--version']
return_code: 0
Python 2.7.14 :: Anaconda, Inc.
```

### Why did not you use BAT or VBS?

Microsoft seems to have a unique view on calling process, especially about arguments. 
Regarding the escaping of arguments, it is a special one unparalleled. 
Let's not approach them unless necessary.
