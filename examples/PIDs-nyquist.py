#!/usr/bin/pythont
# Example of LinResList.nyquist()

from os.path import join, dirname
from modelicares import LinResList, read_params

lins = LinResList('PID.mat', 'PID/*/')

# Parameter settings aren't recorded in the files, so we'll load the
# differential time constants from the corresponding dsin.txt files.
for lin in lins:
    lin.label = "Td = %g s" % read_params('Td', join(lin.dirname, 'dsin.txt'))

# and sort the results by that information:
lins.sort(key=lambda lin: lin.label)

# and finally plot:
lins.nyquist(title="Nyquist plot of Modelica.Blocks.Continuous.PID\n"
                   "with varying differential time constant",
             labels=lins.label, freqs=(0.1, 100));
