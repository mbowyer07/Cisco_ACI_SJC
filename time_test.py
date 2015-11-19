import sys
from cobra.mit.session import LoginSession
from cobra.mit.access import MoDirectory
from cobra.mit.request import ConfigRequest
from cobra.model.fv import *
import cobra.model.pol
import cobra.model.vz
import csv
import datetime

now = datetime.datetime.now()

time_of_err = now.strftime("%m\%d\%Y %H:%M")

print now
