With no prior aquintance to Device_file and named pipe I tried to illustrate my understanding so far with this 'solution'.

# Python Task

You're working on a Python project: your project has to collect data from a
peripheral that is managed by your OS by the means of a
[device file](https://en.wikipedia.org/wiki/Device_file), then send
the data to another Python program through a named pipe. In order to interface
with the peripheral, you're using a [library](./FPP_Docs.md).

Every message that is received on the peripheral should be printed out by the
pipe-receiving program.

Your solution may be organised as your prefer, we just advise to separate the
two pieces of software (the peripheral reader and the message printer) in two
different folders in this directory.

_Note: your code cannot be tested, but it will be subject of discussion at the
interview, if you'll pass the task selection._