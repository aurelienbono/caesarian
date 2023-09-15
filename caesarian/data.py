""" 
function for transform  string data to integer data 

"""


class TransformData:
	def __init__(self,x=None) : 
		self.x = x 


# transformations of all the data manualy 
	def transform(self,x) : 
		new_array = []
		new_array.append(x[0])
		new_array.append(int(x[1])) 
		new_array.append(int(x[2])) 



		if x[3] == 'opportun' : 
			new_array.append(0)
		elif x[3] == 'premature':
			new_array.append(1)
		else : 
			new_array.append(2)


		if x[4] == 'faible' : 
			new_array.append(0)
		elif x[4]  == 'normale':
			new_array.append(1)
		else : 
			new_array.append(2)


		if x[5] == 'oui' : 
			new_array.append(0)
		else : 
			new_array.append(1)

	
		

		return new_array



