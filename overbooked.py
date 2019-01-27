"""
This program will check for overscheduled nodes on a supercomputer using PBS.
"""
import subprocess

MAX_SYSTEM_CORES = 28 # The max number of cores per node.

def import_command():
    '''
    This function is used to import data from qstat's command output into a
    multi-dimensional dictionary.
    Returns: a multi-dimensional dictionary of
             - nodes-ids
              - job-ids runing on node.
               - number of cores requested by job.
    '''
    data = {}
    data_command = str(subprocess.run(['qstat', '-atwn1'], \
    stdout=subprocess.PIPE)).split("\\n")[10:] # Running qstat through Python.
    for entry in data_command[:-1]: # The last entry printed is empty.
        data_entry = entry.split() # Split each line of data into a list.
        #Iterate through each node listed per job. For jobs on more than one node.
        for entry in data_entry[11].split("+"):
            key1 = entry.split("/")[0] # Get node id
            if key1 != "--": # If the job isn't on a node, disregard it.
                key2 = data_entry[0] # Add job id to dictionary.
                value = entry.split("/")[1].split("*")[-1] # Add requested cores.
                update_dict2(data, key1, key2, value) # Update dictionary
    return data

def update_dict2(dict2, key1, key2, value):
    '''
    This function updates/creates a 2-dimensional dictionary.
    key1: should be an imutable variable that is the first level dict key.
    key2: should be an imutable type that is used as the second level dict key
    value: this can be any type that will be used as a the dictionary value.
    '''
    if key1 not in dict2: # If key1 is not present in dictionary,
        dict2[key1] = {} # Initalize a new empty dictionary.
    dict2[key1][key2] = value # Assign value to dictionary entry.

def main():
    data = import_command() # Import data from command. See function comment.
    for key1 in data: # Iterate through node ids.
        core_sum = 0
        for key2 in data[key1]: # Iterate through job ids.
            core_sum += int(data[key1][key2])
        if core_sum > MAX_SYSTEM_CORES: # If requested core > max then print node.
            print("{}: {}".format(key1,data[key1]))#Print jobs on overscheduled nodes.

main()