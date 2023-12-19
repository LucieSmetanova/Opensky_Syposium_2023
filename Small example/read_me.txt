------------------------------------------------------------------------------------------------------------------------
Instructions for small working example of PM utilization analysis of one week of October 2022 at Oslo Gardermoen airport
------------------------------------------------------------------------------------------------------------------------

The folder contains the following:

- Input folder with cleaned input data obtained from the Opensky historical database
- Python scripts for each part of analysis
- Empty output folder prepared for output data from each python script

--------------
Instructions:
--------------
This folder is designed to run independently on device-specific paths. It can be downloaded and the scripts run directly with the default settings. 
To successfully obtain all the results, please run the scripts in the order indicated in the script names.

All the input and output .csv files are delimited with space.

-------------
The scripts:
-------------
- 01_ENGM_determine_runway_small - takes the raw input data and assign each flight trajectory to a runway
				 - gives two types of output files, one with runway indication for each flight and another with data subset based on runway
- 02-05_ENGM_PM1-4 - outputs subset of flights adhering to the PM systems at Oslo Gardermoen airport
- 06_merge_PM_files - takes the outputs from 02-05 scripts and merges them to one PM_dataset output file
- 07_check_PM_flights - gives plot of flights in the PM_dataset for visual correctness check
- 08_check_nonPM_flights - gives plot of flights not identified as PM
- 09_PM_util_calc - takes the PM subsets as inputs and outputs files with information at which point each of the flights left the PM arc
- 10_PM_util_percent - calculates the PM utilization in percents using output files from script 09
		     - the output is text log directly in Python IDE console