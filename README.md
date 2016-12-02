#DataScience-Project

##About

:p

##Getting Started
Please use Anaconda if you aren't already for some strange reason.  
Create a virtual environment like so:  
```bash
conda create --name **_EnvName_** --file requirements.txt
```

Then activate the environment before you get to work:
```bash
source activate **_EnvName_**
```

Deactivate when you are done like this:
```bash
source deactivate
```

##Contributing

###Work on your own branch 
Merge conflicts are ugly, and it's really bad when somebody "accidentally"
pushes binaries, temps, and other large files. If it only happened in your
branch, revert to a clean state so nobody has to merge dirty project files to
master. Create a new branch and switch to it with one command:
```bash
git checkout -b **_BranchName_**
```

You'll now be working on your own branch until you checkout to a different
branch. Try not to checkout another branch unless you got corresponding developer's OK.

###master 
Someone who knows what they are doing should take care of merging to master.
Create a pull request to have your work merged in. In the end, your merged
work is what counts, so make sure your branch is clean.

By keeping master clean like this and working on separate branches, we never
have to receive a message from a developer saying something like "Don't pull!
My notebook is corrupted!" It sounds like a ridiculous statement, but it
happens. It really shouldn't.

##Updates

###Getting them
Just pull the latest changes from the repo! If anything goes wrong due to
dependencies, make sure you get the latest requirements. Like so:  
```bash
conda install --yes --file requirements.txt
```

Do this while your virtual environment is active, of course.

###Making them
If you added a dependency to the environment, keep everyone on the bleeding
edge too! Do this by running:
```bash
conda list --export > requirements.txt
```

Once again, inside of your environment. Just push these changes and everyone
else can refer to the "Getting them" section above. :D

##Misc.

Here are some data science best practice. I like the one that says to mark
your notebooks with your initials:


http://svds.com/jupyter-notebook-best-practices-for-data-science/


For more conda stuff, here's a conda vs pip vs virtualenv table:

http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html
