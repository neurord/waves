# waves
**Repository of membrane potentiation traces in response to current injection for use in ajustador parameter 
optimization of moose_nerp models. Independently of optimizations, ephys_feature_extract can measure spike, AHP 
and other features from data and provide summary measures of those features**

*What does ephys_feature_extract do?*
It processes a set of electrophysiology traces (current clamp) for a defined list of neuron types. 
It measures numerous features from the data traces to provide the mean, standard deviation, and coefficient of variance 
for each feature for each type of neuron, as well as create plots of the feature values vs. injection amplitude.

*Important Notes*

- The program can be used to extract electrophysiology features for any number of neuron types, any number of neurons of each type.
- The program can be used for unlimited number of feature measurements. To add or remove features (optional) requires 
changing the desired_measurements array at the top.

**I. Preparing Your Data**

In order to run the function ephys_feature_extract.py, your experimental data must be stored in a specific way. 
The two file formats are CSV and igor binary:

A. CSV format

1. Create a directory to contain all the csv files, one csv file per neuron
2. Arrange each individual neuron's data collection in a CSV file with the first column time, and each subsequent 
column the membrane potential for a single current injection.
3. the first row has a header listing the current injection value for each column and the units, 
e.g. Time (ms), -200pA, -150pA, -100pA, -50pA, 0 pA
4. Name the file using the following naming convention: "neurontype_neuronidentifier.csv"

   -for example, "Npas1033.csv"
 

B. igor binary format

1. Create a directory to contain all the data
2. Prepare a subdirectory for each neuron's data with the name:
"unique-experiment-identifier_neurontype_Waves". 
3. In each subdirectory, create individual files for each wave labeled "W-date-experID_experimentnumber_seriesnumber_tracenumber_wavenumber.ibw"
- for example, "W05Jan2015_SLH00_1_3_1_1p1.ibw"
- The last four numbers are created by the software Patchmaster when exporting data as igor binary.

**II. Preparing to calculate physiological data**

A. For CSV files: Create a python file, by editing gpedata_experiment.py, providing the following information:

1. directory name with the CSV files (string in line 29)
2. time that current injection starts and ends (lines 13 and 14: injection_start and injection_end)
3. time period for measuring the baseline membrane potential, both before and after current injection.  Baseline_before (line 18) is less than or equal to injection_start, and baseline_after (line 19) is sometime after injection_end, to allow depolarization to decay. 
4. steady_after: measure steady state response to current injection between this time and injection_end
5. The array "alldata" should have the names of the neurons you want to be evaluated.

B. For igor binary format files: Create a python file, by editing A2Acre.py, providing the following information:

1. name of the directory containing the data (string in line 34)
2. The time that current injection starts and ends (lines 27 and 28: injection_start and injection_end)
3. time period for measuring the baseline membrane potential, both before and after current injection.  Baseline_before (line 12) is less than or equal to injection_start, and baseline_after (line 15) is sometime after injection_end, to allow depolarization to decay
4. steady_after: measure steady state response to current injection between this time and injection_end
5. Specify the python name of each neuron’s data, as well as a description of the current injection protocols.

- the python name of each neuron’s data should start with the neuron type
- for series of hyperpolarizing current injection, provide IV=(start_current, current_increment, series number)
- for series of depolarizing current injection, provide IF=(start_current, current_increment, series number)
- list of the duration of the trace, where time = trace_duration
- In summary: specify the following for each neuron’s data:

`neurontype_uniqueidentifier= IVCurveSeries(subdirname,params, IV=(min_inj,increment,series_number), IF=(min_inj,increment,series_number),time=duration_of_trace)`

f. The dictionary "alldata" at the end of the file collects the python names of the neurons you want evaluated, using the name as both the key and the value.

**III. Now run ephys_feature_extract.py in python 3**

Command line arguments: 

- a list of neuron types
- the name of the python file specifying the data

`python3 ephys_feature_extrac.py -n list of neuron types -w python_module`

e.g.

`python3 ephys_feature_extract.py -n arky proto Npas -w A2Acre`

 * Optional: 
 Edit the "desired_params" array in the ephys_feature_extract.py file to specify which features of the data you want to measure.
 For more information on feature definitions, see https://neurord.github.io/ajustador/features.html

*If you get an error, please read comments inside ephys_feature_extract.py*

*Please note that all the functions are in a separate file, ephys_feature_extract_func.py. There are comments to explain what each function does if there is an issue inside the comments*



