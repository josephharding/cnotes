import json


class AdventureGame:

		
	def __init__(self):
		self.is_running = True
		self.config = self.loadconfig('config.json')
		self.stringconfig = self.loadconfig('strings.json')
		self.currentchoice = None
		self.currentenctxt = None
		self.encorder('start')

	def encorder(self, encname):
		self.loadencounter(encname)
		print(self.currentenctxt)
		self.currentchoice.show_options()

	def getstring(self, stringname):
		if stringname in self.stringconfig:
			result = self.stringconfig[stringname]
		else:
			result = '{stringname} not found'.format(stringname=stringname)
		return result		

	def createchoice(self, name):
		result = 'notfound'
		choiceconfig = self.config['config']['choice']
		for choice in choiceconfig:
			if choice['name'] == name:
				result = Choice()
				for optionname in choice['options']:
					result.add_option(self.createoption(optionname))
		return result

	def createoption(self, name):
		result = 'notfound'
		optionconfig = self.config['config']['option']
		for option in optionconfig:
			if option['name'] == name:
				result = Option(self.getstring(option['text']),option['action'])
		if result == 'notfound':
			raise Exception('option {name} does not exist'.format(name=name))
		return result

	def loadencounter(self, name):
		enco = self.getencounter(name)
		self.currentchoice = self.createchoice(enco['choice'])
		self.currentenctxt = self.getstring(enco['text'])

	def getencounter(self, name):
		startencounter = 'not_found'
		encounterconfig = self.config['config']['encounter']
		for encounter in encounterconfig:
			if encounter['name'] == name:
				startencounter = encounter
		return startencounter

# with used to open contents of external file
# define loc variable string for use with json.loads
	def loadconfig(self, filename):
		with open(filename, 'r') as content_file:
			content = content_file.read()
		return json.loads(content)

	def should_update(self):
		return self.is_running
    	
	def update(self):
		choice = raw_input("> ")
		if choice == 'x':
			self.is_running = False
		else:
			action = self.currentchoice.handle_input(choice)
			if action == 'gameover':
				self.is_running = False
			else:
				if action != 'invalid_choice':
					self.encorder(action)
				else:
					print('Try again')

class Choice:
	
	def __init__(self):
		self.option_list = []

	def add_option(self, op):
		self.option_list.append(op)
	
	def show_options(self):
		for op_index, op in enumerate(self.option_list):
			mytext = "<{ind}>  {optext}".format(ind=op_index+1,optext=op.get_optext())
			print(mytext)

	def handle_input(self, choice):
		result = "invalid_choice"
		for op_index, op in enumerate(self.option_list):
			if choice == str(op_index+1):
				result = op.get_action()
		return result		
		

class Option:

	def __init__(self, optext, action):
		self.optext = optext
		self.action = action

	def get_optext(self):
		return self.optext

	def get_action(self):
		return self.action



if __name__ == "__main__":

	game = AdventureGame()


	while game.should_update():
		game.update()

	print("GAME OVER")
 
