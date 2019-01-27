# Overbooked
A simple tool to check if PBS is currently over scheduling any node in a HPC cluster.

## Usage
If the system you are on uses modules you may need to load the python module before exicuting `overbooked.py`.  
For example: `module load python/3.6`  

The system will scan the cluster using the `qstat` command and print out the ID's of any nodes that appear to be overbooked. Overbooked meaning that there are more processes alotted to users than available and as such the processes are using the same resources.

Example Output:  
`i1n6: {'1749209.head1.cm.cluster': '3', '1749221.head1.cm.cluster': '6', '1768777.head1.cm.cluster': '28'}`  
The line above shows that the node `i1n6` is currently running three jobs. This appears to be a problem because the last job has requested all 28 of the cores available on the node but other jobs are still present using another 9 combined cores.

## Config
The default max cores per node value is set at 28. Change that to fit your systems config before running.  
Then simply run `python3 overbooked.py`.

## Dependencies
`Python >= 3.6`