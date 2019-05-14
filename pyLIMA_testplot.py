'''
Welcome to pyLIMA tutorial!
Let's learn how pyLIMA works by fitting an example.
Please help yourself with the pyLIMA documentation
'''

### First import the required libraries
import numpy as np
import matplotlib.pyplot as plt
import os, sys

from pyLIMA import event
from pyLIMA import telescopes
from pyLIMA import microlmodels

### Create an event object. You can choose the name and RA,DEC in degrees :

your_event = event.Event()
your_event.name = 'pyLIMA_testTarget'
your_event.ra = 269.39166666666665 
your_event.dec = -29.22083333333333

### Now we need some observations. That's good, we obtain some data on two
### telescopes. Both are in I band and magnitude units :

data_1 = np.loadtxt('./data/Survey_1.dat')
telescope_1 = telescopes.Telescope(name='OGLE', camera_filter='I', light_curve_magnitude=data_1)

data_2 = np.loadtxt('./data/Followup_1.dat')
telescope_2 = telescopes.Telescope(name='LCOGT', camera_filter='I', light_curve_magnitude=data_2)

### Add the telescopes to your event :
your_event.telescopes.append(telescope_1)
your_event.telescopes.append(telescope_2)

### Find the survey telescope :
your_event.find_survey('OGLE')

### Sanity check
your_event.check_event()


### Construct the model you want to fit. Let's go basic with a PSPL, without second_order effects :
model_1 = microlmodels.create_model('PSPL', your_event)

### Let's try with the simplest Levenvberg_Marquardt algorithm :
your_event.fit(model_1,'LM')

### Let's see some plots.
your_event.fits[0].produce_outputs()
#print('Chi2_LM :',your_event.fits[0].outputs.fit_parameters.chichi)
#plt.show()
f1 = plt.figure(1)
plt.savefig('/home/airpush/TOM-Development/static/img/pyLIMA1.png')
f2 = plt.figure(2)
plt.savefig('/home/airpush/TOM-Development/static/img/pyLIMA2.png')


### Let's try with differential evolution  algorithm. WAIT UNTIL THE FIGURE POP UP.
#your_event.fit(model_1,'DE')
#your_event.fits[1].produce_outputs()
#print('Chi2_DE :',your_event.fits[1].outputs.fit_parameters.chichi)
#plt.show()


