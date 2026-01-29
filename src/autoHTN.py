import pyhop
import json

def check_enough(state, ID, item, num):
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough(state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

pyhop.declare_methods('have_enough', check_enough, produce_enough)

def produce(state, ID, item):
	return [('produce_{}'.format(item), ID)]

pyhop.declare_methods('produce', produce)

def make_method(name, rule):
	# Creates a method function from a recipe rule in JSON
	# Contains: preconditions to check and operator to call
	# Produces: what it makes
	# Requires: what it needs
	# Time: time required to make
	# Returns a method function
	# Checks the preconditions, then returns the task list if they are met
	# Calls the appropriate operator to perform the action
	def method(state, ID):
		# list of tasks
		tasks = []
		# foreach precondition in rule['Preconditions']:
		for item, qty in rule.get('Requires', {}).items():
			tasks.append(('have_enough', ID, item, qty))
		for item, qty in rule.get('Consumes', {}).items():
			tasks.append(('have_enough', ID, item, qty))
		
		# tasks.append(('have_enough', ID, precondition['item'], precondition['amount']))
		# tasks.append(('op_produce_{}'.format(name), ID))
		# return tasks
		operator_name = 'op_produce_{}'.format(name)
		tasks.append((operator_name, ID))

		return tasks
	return method

def declare_methods(data):
	# some recipes are faster than others for the same product even though they might require extra tools
	# sort the recipes so that faster recipes go first

	# your code here
	# hint: call make_method, then declare the method to pyhop using pyhop.declare_methods('foo', m1, m2, ..., mk)	

	# -------------------------------------------------------------------------------
	# Create a dictionary to hold methods for each product
	product_methods = {}

	# get recipes from data
	recipes = data['Recipes']
	sorted_recipes = sorted(recipes.keys(), key=lambda r: recipes[r]['Time'])

	# for each recipe in the sorted recipes
	# create a method with make_method, add it to product_methods
	for recipe_name in sorted_recipes:
		rule = recipes[recipe_name]

		# for each product produced by the recipe; initialize product_methods entry if not present
		for product_name in rule['Produces']:
			if product_name not in product_methods:
				product_methods[product_name] = []
		
		# create method and add to product_methods for each product
		method = make_method(recipe_name, rule)
		product_methods[product_name].append(method)

	# declare methods to pyhop
	for product, methods in product_methods.items():
		pyhop.declare_methods(product, *methods)


	# for each recipe in data['Recipes']:
	# method = make_method(recipe_name, recipe_rule)
	# add method to product_methods[product_name]

	# for each product_name in product_methods:
	# sort product_methods[product_name] by recipe['Time']
	# pyhop.declare_methods(product_name, *product_methods[product_name])			

def make_operator(rule):
	def operator(state, ID):
		# your code here

		# if not enough time
		# return False
		if state.time[ID] < rule['Time']:
			return False
		
		# for each required item in rule['Requires']:
		# if not enough of that item
		# return False
		for item, qty in rule.get('Requires', {}).items():
			if getattr(state, item)[ID] < qty:
				return False
		
		# for each consumed item in rule['Consumes']:
		# if not enough of that item
		for item, qty in rule.get('Consumes', {}).items():
			if getattr(state, item)[ID] < qty:
				return False
		
		# subtract time, consumed items; add the produced items
		state.time[ID] -= rule['Time']

		for item, qty in rule.get('Consumes', {}).items():
			getattr(state, item)[ID] -= qty
		
		for item, qty in rule.get('Produces', {}).items():
			getattr(state, item)[ID] += qty

		return state
	return operator

def declare_operators(data):
	# your code here
	# hint: call make_operator, then declare the operator to pyhop using pyhop.declare_operators(o1, o2, ..., ok)

	# list of operators
	operators = []
	# for each recipe in data['Recipes']:
	for recipe_name, recipe_rule in data['Recipes'].items():
		operator = make_operator(recipe_rule)
		operators.append(operator)
	# operator = make_operator(recipe_rule)
	# operators.append(operator)
	# pyhop.declare_operators(*operators)
	pyhop.declare_operators(*operators)

def add_heuristic(data, ID):
	# prune search branch if heuristic() returns True
	# do not change parameters to heuristic(), but can add more heuristic functions with the same parameters: 
	# e.g. def heuristic2(...); pyhop.add_check(heuristic2)
	def heuristic(state, curr_task, tasks, plan, depth, calling_stack):
		# your code here

		if curr_task in calling_stack:
			return True
		# if repeated cycle detected in calling_stack
		# return True
		if state.time[ID] < 0:
			return True

		# check if time left is enough to complete curr_task and remaining tasks
		# if not enough time
		# return True
			
		# are we producing something we've already made?
		# if current task == item we've already made
		# return True

		if curr_task[0] == 'produce':
			item = curr_task[2]

			if item in data['Tools'] and getattr(state, item)[ID] >= 1:
				return True
		return False

		# more domain knowledge based pruning conditions

		return False # if True, prune this branch

	pyhop.add_check(heuristic)

def define_ordering(data, ID):
	# if needed, use the function below to return a different ordering for the methods
	# note that this should always return the same methods, in a new order, and should not add/remove any new ones
	def reorder_methods(state, curr_task, tasks, plan, depth, calling_stack, methods):
		# If task is to produce an item that is required by another task in tasks,
		# move that method to the front of the methods list
		# check for most efficient method (fastest time) to produce the item
		# prioritize methods with tools or items already available in state (we already have them)
		# return the reordered methods list
		
		return methods
	
	pyhop.define_ordering(reorder_methods)

def set_up_state(data, ID):
	state = pyhop.State('state')
	setattr(state, 'time', {ID: data['Problem']['Time']})

	for item in data['Items']:
		setattr(state, item, {ID: 0})

	for item in data['Tools']:
		setattr(state, item, {ID: 0})

	for item, num in data['Problem']['Initial'].items():
		setattr(state, item, {ID: num})

	return state

def set_up_goals(data, ID):
	goals = []
	for item, num in data['Problem']['Goal'].items():
		goals.append(('have_enough', ID, item, num))

	return goals

if __name__ == '__main__':
	import sys
	rules_filename = 'crafting.json'
	if len(sys.argv) > 1:
		rules_filename = sys.argv[1]

	with open(rules_filename) as f:
		data = json.load(f)

	state = set_up_state(data, 'agent')
	goals = set_up_goals(data, 'agent')

	declare_operators(data)
	declare_methods(data)
	add_heuristic(data, 'agent')
	define_ordering(data, 'agent')

	# pyhop.print_operators()
	# pyhop.print_methods()

	# Hint: verbose output can take a long time even if the solution is correct; 
	# try verbose=1 if it is taking too long
	pyhop.pyhop(state, goals, verbose=1)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'cart', 1),('have_enough', 'agent', 'rail', 20)], verbose=3)
