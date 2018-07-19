#intents Dictionary
intent = {
	'I_Goodbye_HEADER' : {
		'responses' : [
				'Goodbye {0[FirstName]}, Have a nice day!', 'Bye {0[FirstName]}, See ya later..'
			],
		'action' : 'dummyAction',
		'actionProvidesResponse' : False,
		'entities' : {},
		'outIntents': []
	},
	'I_Customer_HEADER' : {
		'responses' : [
				'You have selected Customers, ask further questions', 'Customers have been selected, proceed with further questions'
			],
		'action' : 'dummyAction',
		'actionProvidesResponse' : False,
		'entities' : {},
		'outIntents': ['I_Customer_Total_Sales_Volume', 'I_Goodbye_HEADER'] #later add customer related intents, HEADER intents
	},
	'I_Welcome_Name_Input' : {
		'responses' : [
				'Hi {0[FirstName]}, How may I help you with regards to People, Customer, Suppliers and Business news'
			],
		'action' : 'dummyAction',
		'actionProvidesResponse' : False,
		'entities' : {'FirstName': True, 'LastName': False},
		'outIntents': ['I_Customer_HEADER', 'I_Goodbye_HEADER'] #later add i_People_HEADER, etc
	},
	'I_Customer_Total_Sales_Volume' : {
		'responses' : [
				'Total sales volume for Customer {0[Customer]} is {1[salesVolume]} euros', 'Sales volume for Customer {0[Customer]} is {1[salesVolume]} euros'
			],
		'action' : 'getCustomerSalesVolume',
		'actionProvidesResponse' : False,
		'entities' : {'Customer': True},
		'outIntents': ['I_Goodbye_HEADER', 'I_Customer_Total_Sales_Volume']
	}
}
