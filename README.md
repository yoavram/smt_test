# Sumatra Test

## What Is this?

This is a simple Python simulation that can be used to test and experiment the [Sumatra](http://packages.python.org/Sumatra/index.html) Simulation Management Tool.

Sumatra is a tool I found out about recently (10/12) that manages your computational experiments: simulations, calculations, analysis, any program your going to be running many times to create lots of data. It keeps track of what exactly you ran, in terms of source code, parameters, environment configuration, dependencies, etc.; when you ran it; how long it took; what was the input and output results. It lets you easily repeat configurations to be run again. And it let's you browse a library of your activity via your browser.

I've been looking for something like this ever since I ran my 1000th simulation on our lab's computer cluster, I was so frustrated with keeping track of what I'm running. So I decided I'd put this tutorial online for the sake of others, and for demoing it to colleagues. 

Note that demo this will not prevent you the need from installing and setting up *Sumatra* - but it will give you a quick simulation to run with it, and I provide some troubleshooting of problems I stumbled upon.

## The Simulation

The simulation itself is pretty basic:

  - Start off with a n individuals
  - Divide them to two types, n/2 each
  - In every simulation step, randomly sample the next generation so that each type gives birth to invdividuals of the same type
  - Run x number of steps

n is given by a parameter called popsize and x by ticks. Both are at the params file under the *default* section.

The simulation is implemented in Python 2.7 and required NumPy to be installed.

## Setup Sumatra

I did this on Windows, I did this on Linux. See the troubleshoot section for solving problems.

  - Install *Sumatra* - `pip install sumatra`
  - Install *GitPython* - `pip install GitPython`  
  - Get the code for this project by using `git clone`
  - Setup Sumatra - `smt init smt_test`
  - Configure Sumatra - 
    - `smt configure --executable=python`
    - `smt configure --main=main.py`
  - Run simulations: `smt run params`

## Experiment with it

Try different Sumatra stuff from [here](http://packages.python.org/Sumatra/command_reference.html), like:

  - `smt run --label=some_label params` to get a specific label for a record
  - `smt run --reason="why I ran this simulation" params`
  - `smt run params default.popsize=100000` to run a simulation with more individuals
  - `smt list` and `smt list -l` to see what already ran
  - `smt repeat some_label`
  - Try the [web interface](http://packages.python.org/Sumatra/web_interface.html) it's awesome: `smtweb &`

## Troubleshoot

1. On Windows: when trying to call `smt` from the Windows command line it didn't work so I had to call `python c:\python27\scripts\smt`. I managed a workaround by working from *Git Bash* instead of *cmd*, but then found out a solution in the [Sumatra Google Group](https://groups.google.com/forum/?fromgroups=#!topic/sumatra-users/Jlo7Ixhp1dM).
1. On a Linux cluster machine: I didn't have root control so installing and using *Sumatra* was a bit of tricky:
  - First I installed [virtualenv] locally, that is: `pip install --user virtualenv`. If you are using a different python installer, check how to do it.
  - Then I had to add the local site-packages folder to the PYHONPATH and the local bin folder to the PATH so that `virtualenv` would work. That took me some time because most tutorials assume *bash* but I'm using *csh*.
  - Then I started an *Sumatra* virtual environment - see directions [here](http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip/). You got to be on *bash* to call `bin/activate`!
  - Then I went on, and everything worked nicely.

## License

I'm talking about the license of the code and README, for Python's and Sumatra's licese visit their website, but I think both are pretty much free.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.

