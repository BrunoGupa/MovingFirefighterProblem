# The Moving Firefighter Problem
The Moving Firefighter Problem (MFP) is a generalization of the original Firefighter Problem presented by Hartnell. 
It incorporates a function τ that defines the time a firefighter takes to move from one vertex to another. The article 
that presents this problem will soon be available online.

This repository contains the mixed-integer quadratically constrained program (MIQCP) for the 
optimization version of the MFP for a single firefighter (1-MFP). 

 * "run_batch.py" runs the complete batch instances used in the article.
 * "get_D_value.py" finds an upper bound for the defense rounds D.
 * "recursive_function.py" finds the minimum value for the burning rounds B  needed to 
achieve the optimal objective.
 * "verify_function.py" is necessary to ensure that the diffusive process finishes for the defending rounds B.
 * "gens_for_paper.py" contains the seeds used for the paper. 
 * "utils.py" and "plots.py" are responsible for the plotting process. The plots are saved in 
the "img" folder.
 * The "csv_s" folder contains the results obtained by running "run_batch.py," which are reported in the paper. 


Link to the article will be available soon:

Bruno R. Gutiérrez-De-La-Paz, Jesús García-Díaz, Rolando Menchaca-Méndez, Mauro A.
Montenegro-Meza, Ricardo Menchaca-Méndez, Omar A. Gutiérrez-De-La-Paz. The Moving Firefighter Problem.


To execute the implemented formulations is need to install Gurobi.

## Install gurobipy:

- **Source**: https://www.gurobi.com/gurobi-and-anaconda-for-windows/

### Step one: Download and install Anaconda

Gurobi supports Python 2.7 and 3.7 for Windows. However, to run our code install Python 3.X. 
Please choose the version of Anaconda you wish to download (the download will start automatically):

Once the download is complete, click on it to run the installer.

### Step two: Install Gurobi into Anaconda

The next step is to install the Gurobi package into Anaconda. You do this by first adding the Gurobi channel 
into your Anaconda platform and then installing the gurobi package from this channel.

From an Anaconda terminal, issue the following command to add the Gurobi channel to your default search list:

```
$ conda config --add channels http://conda.anaconda.org/gurobi
```

Now issue the following command to install the Gurobi package:

```
$ conda install gurobi
```

You can remove the Gurobi package at any time by issuing the command:

```
$ conda remove gurobi
```

### Step three: Install a Gurobi License

The third step is to install a Gurobi license (if you haven’t already done so).

You are now ready to use Gurobi from within Anaconda. Your next step is to install the instances generators 
of the Moving Firefighter Problem (MFP)

## Moving Firefighter Problem Generator
- **Source:** <https://github.com/omargup/moving_firefighter_problem_generator>



## Running the implemented formulation

Run "run_batch.py." Feel free to change the hyperparameters. Be careful because a more considerable number 
of nodes in a graph or a smaller lambda value could mean a more considerable running time.

The results are saved in ./Runs/csv_s directory as cvs files divided by the number of nodes in the graph.
