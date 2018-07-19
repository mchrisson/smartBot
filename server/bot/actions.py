#Actions
import random

def getCustomerSalesVolume( slotsDictionary ) :
	# slotdict['Customer'] do something
	return { 'salesVolume' :random.choice([1000, 1500]) }

def dummyAction( slotdict ) :
	return {}

action = {
	'getCustomerSalesVolume': getCustomerSalesVolume,
	'dummyAction': dummyAction
}
