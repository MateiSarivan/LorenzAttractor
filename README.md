# LorenzAttractor

# Installation

1) In an anaconda terminal insert
>>> conda install -c mateisarivan lorat

or 

2) Clone git repository MateiSarivan/LorenzAttractor using
git clone https://github.com/MateiSarivan/LorenzAttractor.git
Afterwards change directory. E.g.:
cd "Your_Path"//LorenzAttractor 
where "Your_Path" represents the directory where you cloned the repository 

in your conda terminal change directory to:
>>> setup.py install

# Running and generation of results

In your python environment terminal insert into your command line
>>> lorat-simulation

This will open the gui where the user can select the input parameters (x, y, z) and the time step dt and number of samples N. After the user has selected the desired parameters click "Save". The user can then navigate to the desired path for saving the results and click the button "Select folder". A folder called "LoratResults" will be created. If an additional session is opened where the user selects other initial conditions the program will ask the user again for the desired folder. If the folder is already created the user can simply select the "LoratResults" folder before clicking the "Select Folder" button. Thus, no new folder will be created in this scenario. 

After the location of the results has been selected a new folder will be created for each combination of initial conditions (x,y,z), dt, and N.

>>> Path\LoratResults\N&dt=2;x=1;y=1;z=1

where N&dt=1 represent the first slider value dt=0.01 and N=500. For higher slider values dt will decrease while N will increase.

The folder will contain the following files:
>> - .csv file containing data in csv form with the following structure: values of initial conditions (x,y,z), N, dt, and total time of data sampling for each set of constants beta, sigma, rho. On the following lines, for each pair of (beta,sigma,ro) the time elapsed for the experiment and the values of the sampled (x,y,z) at each time step are given with up to 3 decimals. There are in total 5 sets of (x,y,z) for each set of (beta,sigma,ro): WRITE beta, sigma, ro COMBINATIONS.
>> - .numpy file containing the data of the experiment in numpy format. The data is given under a dictionary stucture experiment_data={"init_x" = value of initial x, "init_y" = value of initial y, "initial_z" = value of initial z, "dt" = value of dt, "N" = value of N, "elapsed_time" = value of time elapsed for the experiment, "beta" = [list with beta constants], "sigma" = [list with sigma constants], "rho" = [list with rho constants], "data" = [for each pair of (sigma, beta, rho)]: [1: sampled values for x (list)], "2": sampled values for y(list), "3": sampled values for z(list), "4": elapsed time for generating the (x, y, z) set (float)}
>> - .pdf the pdf with the results obtained (Parameters, Information regarding operating platform, and 3D and 2D graphs of the Lorenz Attractor for each (sigma, beta, rho), combination).
>> - .png images of the 3D and 2D graphs generated for each (sigma,beta,rho) combination.asd