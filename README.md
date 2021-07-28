<a href="">
    <img src="./img/loop_alpha.png" alt="LorenzAttractor logo" title="Lorat" align="right" height="60" />
</a>

# LorenzAttractor

![PyTest](https://github.com/MateiSarivan/LorenzAttractor/actions/workflows/lorat.yml/badge.svg)

Choosing the right initial conditions, the right sampling step and the right sampling range for generating the beautiful Lorenz Attractor loops can be quite difficult depending on the selected σ, β and ρ constants. We propose hereby a GUI tool that can be used to easily run parametric studies on the lorenz equations.

# Installation

1. 
a) In an anaconda terminal execute (you may want to use a virtual environment <see b)>):

    >conda install -c mateisarivan -c conda-forge lorat

b) To cleanly remove the installed package use:

    >conda create -n lorat_env
    >conda activate lorat_env
    >conda install -c mateisarivan -c conda-forge lorat

or 

2. 
Clone git repository MateiSarivan/LorenzAttractor using

    >git clone https://github.com/MateiSarivan/LorenzAttractor.git

Afterwards change directory to get inside the cloned repository E.g.:

    >cd path\to\cloned\repository\LorenzAttractor 
Install the package:

    >python setup.py install

# Running and generation of results

In your terminal execute:

    >lorat-simulation

<p align="center">
  <img src="./img/lorat_simulation.png" alt="Scrennshot of the lorat-simulation GUI" width="738">
</p>

This will open the gui where the user can select the input parameters (x, y, z) and the time step dt and number of samples N by using sliders. After the user has selected the desired parameters click "Save". 

<p align="center">
  <img src="./img/pick_where_to_store_results.png" alt="Scrennshot of the lorat-simulation GUI" width="738">
</p>

The user can then navigate to the desired path for saving the results and click the button "Select folder". A folder called "LoratResults" will be created. If an additional session is opened where the user selects other initial conditions the program will ask the user again for the desired folder. If the folder is already created the user can simply select the "LoratResults" folder before clicking the "Select Folder" button. Thus, no new folder will be created in this scenario. 

<p align="center">
  <img src="./img/experiment_folder.png" alt="Scrennshot of the lorat-simulation GUI" width="738">
</p>

After the location of the results has been selected, inside the "LoratResults", a new folder will be created with a random name everytime a new experiment is being saved.

While saving, the GUI window will become unresponsive, please be patient.

The folder will contain the following files:
- .csv file containing data in csv form with the following structure: values of initial conditions (x,y,z), N, dt, and total time of data sampling for each set of constants beta, sigma, rho. On the following lines, for each pair of (beta,sigma,rho) the time elapsed for the experiment and the values of the sampled (x,y,z) at each time step are given with up to 3 decimals. There are in total 5 sets of (x,y,z) for each set of (beta,sigma,rho): WRITE beta, sigma, rho COMBINATIONS.
- .numpy file containing the data of the experiment in numpy format. The data is given under a dictionary stucture 

        experiment_data={
            "init_x" = value of initial x,
            "init_y" = value of initial y,
            "initial_z" = value of initial z,
            "dt" = value of dt,
            "N" = value of N, 
            "elapsed_time" = value of time elapsed for the experiment,
            "beta" = [list with beta constants], 
            "sigma" = [list with sigma constants], 
            "rho" = [list with rho constants], 
            "data" = [for each pair of (sigma, beta, rho): 
                1: [sampled values for x(list)],
                2: [sampled values for y(list)],
                3: [sampled values for z(list)], 
                4: elapsed time for generating the (x, y, z)(float)
        }
- .pdf the pdf with the results obtained (Parameters, Information regarding operating platform, and 3D and 2D graphs of the Lorenz Attractor for each (sigma, beta, rho), combination).
- .png images of the 3D and 2D graphs generated for each (sigma,beta,rho) 

# Uninstall

This only works properly if you have used a virtual environemnt. You simply have to delete the environemnt with:

    >conda env remove -n lorat_env

All the generated file will remain on your computer