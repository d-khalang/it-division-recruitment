# Questions

## Question 1

What is the time complexity of the following C program?

```c
#include <stdio.h>

#define MAXN 100

int main() {
    int n = 0, i = 0, j = 0;
    int mat[MAXN][MAXN];

    fscanf(stdin, "%d", &n);

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            fscanf(stdin, "%d", &mat[i][j]);
        }
    }

    for (i = 0; i < n; i++) {
        mat[i][0] *= 2;
    }
}
```
Answer:
The overall time complexity is O(n2), as the it is O(n2)for the nested loop and O(n) for the final loop.

## Question 2

What is a memory leak? Explain how to correctly free memory after a dynamic
memory allocation in C

Answer:
A memory leak happens when programmers allocate memory somewhere in the code and do not free or delete that after the operation. It reduces the performance and, in the worst case, there wouldn't be enough spare memory or other parts of the program to be executed if there are too many memory leaks. In C it is done by free() at the end of functions or programs.

## Question 3

What is an abstract method in OOP? How is it used?
Answer:
An abstract method is a method that is declared but not implemented. It has a method's signature like its name, parameters and return type. But the implementation and determining what the method should do is the responsibility of the chile class. it is like a blueprint for all the subclasses to preserve the same structure

## Question 4

How is `systemd` used in most Linux systems?
Answer:
Is is the service and system manager in most Linux systems. It is the first process that runs after the kernel.
It handles boot process, logging, resource management and allocation. 

## Question 5

What is a `git rebase`?
Answer:
rebase is a kind of alternative for merge. it creates a new commit and moves the commits in a feature branch to the master branch. imagine you are working on a feature branch and commit 3 times. one commit is also committed to the master then you can go to the feature branch and pull that again to be updated with the master. then you can rebase and it applies you commit to the updated feature branch. Then you can checkout to the master and rebase in order to rebase the commits on feature branch to the master and by doing so you have everything linear in the master
