# python_den

## Linux commands learnt
```
mkdir 
cd 
cd ../
ls, ls -a , ls -l, ls -al
code .
. -> current dir
../ -> one step back from current dir
../../ -> two step back from current dir
```
VS Code keyboard shortcut

```
Ctrl ~ to got to terminal
ctrl m,ctrl m to maximize terminal
```

## git commands I used
### git setup steps
```
1.install git, get gitHub credentials and setup SSH
2.create new repository on gitHub 
3.create local repository folder in your working directory(python_den)
    3.1-go to python_den folder and run git init
    3.2-create a file(README.md) and run below 
        git add (README.md)
        git commit -m "message"
4.add origin to remote
    git remote add origin <git repository url>
5.push changes to remote, run 
    git push -u origin master            

and changes are uploaded
```

Other supporting git commands I used
```
git status

to see current remote
git remote 
to see remote urls
git remote -v

git log 
git log --oneline
git show <commit id>

To see branch list
git branch

to change branch name (master to main )
git branch -M <new_branch_name>
```

