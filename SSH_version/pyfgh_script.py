
# imports
import multiprocessing
import PyFGH.main as main
from PyFGH.util import pyfghutil, DataObject
import sys, ast

# Initialize objects. My what a cleverly named class structure
holder = DataObject.InputData()


# More setup of our object
holder.setNlist(ast.literal_eval(sys.argv[1]))
holder.setLlist(ast.literal_eval(sys.argv[2]))
holder.setD(int(sys.argv[3]))


# Setting up where to find the data. This fortunately is static
holder.setequilibrium_file("equil.csv")
holder.setpotential_energy("potential.csv")


# More things that should be variable
holder.setEigenvalueMethod(bool(sys.argv[4]))
holder.setcalculation(sys.argv[5])

# Static value
holder.setcalculation2("Read from File")

# I won't make this variable you can't make me
holder.setcores_amount(max(1, multiprocessing.cpu_count()))

# Seriously, is this another freaking variable??
holder.setNumberOfEigenvalues(int(sys.argv[6]))

# Calculations
holder.setVmethod(holder.getcalculation2())
holder.setinputobject(holder)

# todo Extract the useful data here, probably jsonify it
wfn, freq = main.datagrabber(holder)

# create a json of data we want
save = {'freq': freq}

# This is the value we want to return
#todo probably json notate this, then save as a result.json, which then can be called by our client or openpbs
print(list(freq))

# save json to file


# todo TRY TO DO ALL THE BELOW