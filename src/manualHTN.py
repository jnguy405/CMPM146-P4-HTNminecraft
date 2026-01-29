import pyhop

'''begin operators'''

def op_punch_for_wood(state, ID):
    if state.time[ID] >= 4:
        state.wood[ID] += 1
        state.time[ID] -= 4
        return state
    return False

def op_craft_wooden_axe_at_bench(state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >= 2:
        state.wooden_axe[ID] += 1
        state.plank[ID] -= 3
        state.stick[ID] -= 2
        state.time[ID] -= 1
        return state
    return False

# Wood gathering with different axes
def op_wooden_axe_for_wood(state, ID):
    if state.time[ID] >= 2 and state.wooden_axe[ID] >= 1:
        state.wood[ID] += 1
        state.time[ID] -= 2
        return state
    return False

def op_stone_axe_for_wood(state, ID):
    if state.time[ID] >= 1 and state.stone_axe[ID] >= 1:
        state.wood[ID] += 1
        state.time[ID] -= 1
        return state
    return False

def op_iron_axe_for_wood(state, ID):
    if state.time[ID] >= 1 and state.iron_axe[ID] >= 1:
        state.wood[ID] += 1
        state.time[ID] -= 1
        return state
    return False

# Basic crafting operations
def op_craft_plank(state, ID):
    if state.time[ID] >= 1 and state.wood[ID] >= 1:
        state.plank[ID] += 4
        state.wood[ID] -= 1
        state.time[ID] -= 1
        return state
    return False

def op_craft_stick(state, ID):
    if state.time[ID] >= 1 and state.plank[ID] >= 2:
        state.stick[ID] += 4
        state.plank[ID] -= 2
        state.time[ID] -= 1
        return state
    return False

def op_craft_bench(state, ID):
    if state.time[ID] >= 1 and state.plank[ID] >= 4:
        state.bench[ID] += 1
        state.plank[ID] -= 4
        state.time[ID] -= 1
        return state
    return False

# Tool crafting operations
def op_craft_wooden_pickaxe_at_bench(state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >= 2:
        state.wooden_pickaxe[ID] += 1
        state.plank[ID] -= 3
        state.stick[ID] -= 2
        state.time[ID] -= 1
        return state
    return False

def op_craft_stone_axe_at_bench(state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 3 and state.stick[ID] >= 2:
        state.stone_axe[ID] += 1
        state.cobble[ID] -= 3
        state.stick[ID] -= 2
        state.time[ID] -= 1
        return state
    return False

def op_craft_stone_pickaxe_at_bench(state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 3 and state.stick[ID] >= 2:
        state.stone_pickaxe[ID] += 1
        state.cobble[ID] -= 3
        state.stick[ID] -= 2
        state.time[ID] -= 1
        return state
    return False

def op_craft_furnace_at_bench(state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 8:
        state.furnace[ID] += 1
        state.cobble[ID] -= 8
        state.time[ID] -= 1
        return state
    return False

def op_craft_iron_axe_at_bench(state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 3 and state.stick[ID] >= 2:
        state.iron_axe[ID] += 1
        state.ingot[ID] -= 3
        state.stick[ID] -= 2
        state.time[ID] -= 1
        return state
    return False

def op_craft_iron_pickaxe_at_bench(state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 3 and state.stick[ID] >= 2:
        state.iron_pickaxe[ID] += 1
        state.ingot[ID] -= 3
        state.stick[ID] -= 2
        state.time[ID] -= 1
        return state
    return False

# Smelting operation
def op_smelt_ore_in_furnace(state, ID):
    if state.time[ID] >= 5 and state.furnace[ID] >= 1 and state.coal[ID] >= 1 and state.ore[ID] >= 1:
        state.ingot[ID] += 1
        state.coal[ID] -= 1
        state.ore[ID] -= 1
        state.time[ID] -= 5
        return state
    return False

# Gathering with pickaxes (coal, ore, cobble)
def op_wooden_pickaxe_for_coal(state, ID):
    if state.time[ID] >= 4 and state.wooden_pickaxe[ID] >= 1:
        state.coal[ID] += 1
        state.time[ID] -= 4
        return state
    return False

def op_stone_pickaxe_for_coal(state, ID):
    if state.time[ID] >= 2 and state.stone_pickaxe[ID] >= 1:
        state.coal[ID] += 1
        state.time[ID] -= 2
        return state
    return False

def op_iron_pickaxe_for_coal(state, ID):
    if state.time[ID] >= 1 and state.iron_pickaxe[ID] >= 1:
        state.coal[ID] += 1
        state.time[ID] -= 1
        return state
    return False

def op_stone_pickaxe_for_ore(state, ID):
    if state.time[ID] >= 4 and state.stone_pickaxe[ID] >= 1:
        state.ore[ID] += 1
        state.time[ID] -= 4
        return state
    return False

def op_iron_pickaxe_for_ore(state, ID):
    if state.time[ID] >= 2 and state.iron_pickaxe[ID] >= 1:
        state.ore[ID] += 1
        state.time[ID] -= 2
        return state
    return False

def op_wooden_pickaxe_for_cobble(state, ID):
    if state.time[ID] >= 4 and state.wooden_pickaxe[ID] >= 1:
        state.cobble[ID] += 1
        state.time[ID] -= 4
        return state
    return False

def op_stone_pickaxe_for_cobble(state, ID):
    if state.time[ID] >= 2 and state.stone_pickaxe[ID] >= 1:
        state.cobble[ID] += 1
        state.time[ID] -= 2
        return state
    return False

def op_iron_pickaxe_for_cobble(state, ID):
    if state.time[ID] >= 1 and state.iron_pickaxe[ID] >= 1:
        state.cobble[ID] += 1
        state.time[ID] -= 1
        return state
    return False

# Advanced crafting (rail and cart)
def op_craft_rail_at_bench(state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 6 and state.stick[ID] >= 1:
        state.rail[ID] += 16
        state.ingot[ID] -= 6
        state.stick[ID] -= 1
        state.time[ID] -= 1
        return state
    return False

def op_craft_cart_at_bench(state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 5:
        state.cart[ID] += 1
        state.ingot[ID] -= 5
        state.time[ID] -= 1
        return state
    return False

# Register all operators
pyhop.declare_operators(
    op_punch_for_wood,
    op_wooden_axe_for_wood,
    op_stone_axe_for_wood,
    op_iron_axe_for_wood,
    op_craft_plank,
    op_craft_stick,
    op_craft_bench,
    op_craft_wooden_axe_at_bench,
    op_craft_wooden_pickaxe_at_bench,
    op_craft_stone_axe_at_bench,
    op_craft_stone_pickaxe_at_bench,
    op_craft_furnace_at_bench,
    op_craft_iron_axe_at_bench,
    op_craft_iron_pickaxe_at_bench,
    op_smelt_ore_in_furnace,
    op_wooden_pickaxe_for_coal,
    op_stone_pickaxe_for_coal,
    op_iron_pickaxe_for_coal,
    op_stone_pickaxe_for_ore,
    op_iron_pickaxe_for_ore,
    op_wooden_pickaxe_for_cobble,
    op_stone_pickaxe_for_cobble,
    op_iron_pickaxe_for_cobble,
    op_craft_rail_at_bench,
    op_craft_cart_at_bench
)

'''end operators'''

def check_enough(state, ID, item, num):
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough(state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

ITEM_RECIPES = {
    'wood': {
        'methods': ['punch_for_wood', 'wooden_axe_for_wood', 'stone_axe_for_wood', 'iron_axe_for_wood'],
        'consume_once_flag': False  # These can be done multiple times
    },
    'plank': {
        'prerequisites': [('wood', 1)],
        'operator': 'op_craft_plank',
        'consume_once_flag': False
    },
    'stick': {
        'prerequisites': [('plank', 2)],
        'operator': 'op_craft_stick',
        'consume_once_flag': False
    },
    'bench': {
        'prerequisites': [('plank', 4)],
        'operator': 'op_craft_bench',
        'consume_once_flag': True,
        'flag_name': 'made_bench'
    },
    'wooden_axe': {
        'methods': ['craft_wooden_axe_at_bench'],
        'consume_once_flag': True,
        'flag_name': 'made_wooden_axe'
    },
    'wooden_pickaxe': {
        'prerequisites': [('bench', 1), ('plank', 3), ('stick', 2)],
        'operator': 'op_craft_wooden_pickaxe_at_bench',
        'consume_once_flag': True,
        'flag_name': 'made_wooden_pickaxe'
    },
    'stone_axe': {
        'prerequisites': [('bench', 1), ('cobble', 3), ('stick', 2)],
        'operator': 'op_craft_stone_axe_at_bench',
        'consume_once_flag': True,
        'flag_name': 'made_stone_axe'
    },
    'stone_pickaxe': {
        'prerequisites': [('bench', 1), ('cobble', 3), ('stick', 2)],
        'operator': 'op_craft_stone_pickaxe_at_bench',
        'consume_once_flag': True,
        'flag_name': 'made_stone_pickaxe'
    },
    'furnace': {
        'prerequisites': [('bench', 1), ('cobble', 8)],
        'operator': 'op_craft_furnace_at_bench',
        'consume_once_flag': True,
        'flag_name': 'made_furnace'
    },
    'iron_axe': {
        'prerequisites': [('bench', 1), ('ingot', 3), ('stick', 2)],
        'operator': 'op_craft_iron_axe_at_bench',
        'consume_once_flag': True,
        'flag_name': 'made_iron_axe'
    },
    'iron_pickaxe': {
        'prerequisites': [('bench', 1), ('ingot', 3), ('stick', 2)],
        'operator': 'op_craft_iron_pickaxe_at_bench',
        'consume_once_flag': True,
        'flag_name': 'made_iron_pickaxe'
    },
    'ingot': {
        'prerequisites': [('furnace', 1), ('coal', 1), ('ore', 1)],
        'operator': 'op_smelt_ore_in_furnace',
        'consume_once_flag': False
    },
    'coal': {
        'methods': ['wooden_pickaxe_for_coal', 'stone_pickaxe_for_coal', 'iron_pickaxe_for_coal'],
        'consume_once_flag': False
    },
    'ore': {
        'methods': ['stone_pickaxe_for_ore', 'iron_pickaxe_for_ore'],
        'consume_once_flag': False
    },
    'cobble': {
        'methods': ['wooden_pickaxe_for_cobble', 'stone_pickaxe_for_cobble', 'iron_pickaxe_for_cobble'],
        'consume_once_flag': False
    },
    'rail': {
        'prerequisites': [('bench', 1), ('ingot', 6), ('stick', 1)],
        'operator': 'op_craft_rail_at_bench',
        'consume_once_flag': True,
        'flag_name': 'made_rail'
    },
    'cart': {
        'prerequisites': [('bench', 1), ('ingot', 5)],
        'operator': 'op_craft_cart_at_bench',
        'consume_once_flag': True,
        'flag_name': 'made_cart'
    }
}

def produce(state, ID, item):
    """Refactored produce function using recipe definitions
    
    Example workflow for 'wooden_axe':
    1. Check if 'wooden_axe' exists in ITEM_RECIPES
    2. Since it's a 'consume_once_flag' item, check/set the made_wooden_axe flag
    3. Item has 'methods': ['craft_wooden_axe_at_bench']
    4. Returns: [('produce_wooden_axe', ID)]
    5. pyhop then uses the registered 'produce_wooden_axe' method which calls craft_wooden_axe_at_bench
    
    Example workflow for 'plank':
    1. Check if 'plank' exists in ITEM_RECIPES
    2. Item has 'prerequisites': [('wood', 1)] and 'operator': 'op_craft_plank'
    3. Returns: [('have_enough', ID, 'wood', 1), ('op_craft_plank', ID)]
    4. pyhop first ensures we have wood, then executes the craft operator

    """
    
    # Check if item exists in our recipe definitions
    if item not in ITEM_RECIPES:
        return False
    
    recipe = ITEM_RECIPES[item]
    
    # Handle "consume once" items (tools)
    if recipe.get('consume_once_flag', False):
        flag_name = recipe['flag_name']
        if getattr(state, flag_name, {}).get(ID, False):
            return False
        # Set the flag
        if not hasattr(state, flag_name):
            setattr(state, flag_name, {})
        getattr(state, flag_name)[ID] = True
    
    # Handle items with multiple production methods
    if 'methods' in recipe:
        # Return the appropriate method call
        return [('produce_' + item, ID)]
    
    # Handle items with direct prerequisites and operators
    elif 'prerequisites' in recipe and 'operator' in recipe:
        # Build the list of prerequisite checks
        prerequisites = [('have_enough', ID, req_item, req_amount) 
                        for req_item, req_amount in recipe['prerequisites']]
        # Add the operator at the end
        prerequisites.append((recipe['operator'], ID))
        return prerequisites
    
    return False

pyhop.declare_methods('have_enough', check_enough, produce_enough)
pyhop.declare_methods('produce', produce)

'''begin recipe methods'''

def punch_for_wood(state, ID):
    return [('op_punch_for_wood', ID)]

def wooden_axe_for_wood(state, ID):
    return [('have_enough', ID, 'wooden_axe', 1), ('op_wooden_axe_for_wood', ID)]

def stone_axe_for_wood(state, ID):
    return [('have_enough', ID, 'stone_axe', 1), ('op_stone_axe_for_wood', ID)]

def iron_axe_for_wood(state, ID):
    return [('have_enough', ID, 'iron_axe', 1), ('op_iron_axe_for_wood', ID)]

def craft_plank(state, ID):
    return [('op_craft_plank', ID)]

def craft_stick(state, ID):
    return [('op_craft_stick', ID)]

def craft_bench(state, ID):
    return [('op_craft_bench', ID)]

def craft_wooden_axe_at_bench(state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'plank', 3), ('op_craft_wooden_axe_at_bench', ID)]

def craft_wooden_pickaxe_at_bench(state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'plank', 3), ('op_craft_wooden_pickaxe_at_bench', ID)]

def craft_stone_axe_at_bench(state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'cobble', 3), ('op_craft_stone_axe_at_bench', ID)]

def craft_stone_pickaxe_at_bench(state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'cobble', 3), ('op_craft_stone_pickaxe_at_bench', ID)]

def craft_furnace_at_bench(state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'cobble', 8), ('op_craft_furnace_at_bench', ID)]

def craft_iron_axe_at_bench(state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'ingot', 3), ('op_craft_iron_axe_at_bench', ID)]

def craft_iron_pickaxe_at_bench(state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'ingot', 3), ('op_craft_iron_pickaxe_at_bench', ID)]

def smelt_ore_in_furnace(state, ID):
    return [('op_smelt_ore_in_furnace', ID)]

def wooden_pickaxe_for_coal(state, ID):
    return [('have_enough', ID, 'wooden_pickaxe', 1), ('op_wooden_pickaxe_for_coal', ID)]

def stone_pickaxe_for_coal(state, ID):
    return [('have_enough', ID, 'stone_pickaxe', 1), ('op_stone_pickaxe_for_coal', ID)]

def iron_pickaxe_for_coal(state, ID):
    return [('have_enough', ID, 'iron_pickaxe', 1), ('op_iron_pickaxe_for_coal', ID)]

def stone_pickaxe_for_ore(state, ID):
    return [('have_enough', ID, 'stone_pickaxe', 1), ('op_stone_pickaxe_for_ore', ID)]

def iron_pickaxe_for_ore(state, ID):
    return [('have_enough', ID, 'iron_pickaxe', 1), ('op_iron_pickaxe_for_ore', ID)]

def wooden_pickaxe_for_cobble(state, ID):
    return [('have_enough', ID, 'wooden_pickaxe', 1), ('op_wooden_pickaxe_for_cobble', ID)]

def stone_pickaxe_for_cobble(state, ID):
    return [('have_enough', ID, 'stone_pickaxe', 1), ('op_stone_pickaxe_for_cobble', ID)]

def iron_pickaxe_for_cobble(state, ID):
    return [('have_enough', ID, 'iron_pickaxe', 1), ('op_iron_pickaxe_for_cobble', ID)]

def craft_rail_at_bench(state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 6), ('have_enough', ID, 'stick', 1), ('op_craft_rail_at_bench', ID)]

def craft_cart_at_bench(state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 5), ('op_craft_cart_at_bench', ID)]

# Register all recipe methods
def registerMethods():
    """Register all recipe methods based on ITEM_RECIPES"""
    
    # Register produce_wood methods
    pyhop.declare_methods('produce_wood', 
                        iron_axe_for_wood,        # 1 time (fastest)
                        stone_axe_for_wood,       # 1 time  
                        wooden_axe_for_wood,      # 2 time
                        punch_for_wood)           # 4 time (slowest)
    
    # Register other items with single methods
    single_method_items = {
        'plank': craft_plank,
        'stick': craft_stick,
        'bench': craft_bench,
        'wooden_axe': craft_wooden_axe_at_bench,
        'wooden_pickaxe': craft_wooden_pickaxe_at_bench,
        'stone_axe': craft_stone_axe_at_bench,
        'stone_pickaxe': craft_stone_pickaxe_at_bench,
        'furnace': craft_furnace_at_bench,
        'iron_axe': craft_iron_axe_at_bench,
        'iron_pickaxe': craft_iron_pickaxe_at_bench,
        'ingot': smelt_ore_in_furnace,
        'rail': craft_rail_at_bench,
        'cart': craft_cart_at_bench
    }
    
    for item_name, method_func in single_method_items.items():
        pyhop.declare_methods(f'produce_{item_name}', method_func)
    
    # Register items with multiple methods
    pyhop.declare_methods('produce_coal', 
                         wooden_pickaxe_for_coal, stone_pickaxe_for_coal, 
                         iron_pickaxe_for_coal)
    pyhop.declare_methods('produce_ore', 
                         stone_pickaxe_for_ore, iron_pickaxe_for_ore)
    pyhop.declare_methods('produce_cobble', 
                         wooden_pickaxe_for_cobble, stone_pickaxe_for_cobble, 
                         iron_pickaxe_for_cobble)

'''end recipe methods'''

#
# Declare states
#
def initialState(time=4):
    """Create initial game state as a pyhop.State with all resources"""
    state = pyhop.State('state')
    
    # All resources as dictionaries
    resources = [
        'wood', 'plank', 'stick', 'bench', 'wooden_axe', 'wooden_pickaxe',
        'cobble', 'stone_axe', 'stone_pickaxe', 'furnace', 'iron_axe',
        'iron_pickaxe', 'ingot', 'coal', 'ore', 'rail', 'cart'
    ]
    
    # Initialize all resources to 0
    for resource in resources:
        setattr(state, resource, {'agent': 0})
    
    # Initialize time
    state.time = {'agent': time}
    
    # Initialize all flags to False
    flags = [
        'made_bench', 'made_wooden_axe', 'made_wooden_pickaxe',
        'made_stone_axe', 'made_stone_pickaxe', 'made_furnace',
        'made_iron_axe', 'made_iron_pickaxe', 'made_rail', 'made_cart'
    ]
    
    for flag in flags:
        setattr(state, flag, {'agent': False})
    
    return state

#
# Define a simple heuristic to filter out time consuming production
#
def heuristic(state, curr_task, tasks, plan, depth, calling_stack):
    # Only prune if we have tasks remaining AND no time
    if tasks and state.time['agent'] <= 0:
        # Check if any remaining tasks require time
        for task in tasks:
            if task[0] == 'have_enough':
                item = task[2]
                needed = task[3]
                current = getattr(state, item, {}).get('agent', 0)
                if current < needed:
                    return True  # Need to produce more, but no time
    return False  # Don't prune

pyhop.add_check(heuristic)

registerMethods()
state = initialState(time=4)

# pyhop.print_operators()
# pyhop.print_methods()

pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 1)], verbose=3)
# pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 12)], verbose=3)

# Test 1: Get 1 wood (already works)
state = initialState(time=4)
print("Test 1: Get 1 wood")
result = pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 1)], verbose=1)
print(f"Result: {result}\n")

# Test 2: Get wooden axe
state = initialState(time=20)
print("Test 2: Get wooden axe")
result = pyhop.pyhop(state, [('have_enough', 'agent', 'wooden_axe', 1)], verbose=1)
print(f"Result: {result}\n")

# Test 3: Get 4 wood with wooden axe
state = initialState(time=20)
state.wooden_axe = {'agent': 1}  # Start with axe
print("Test 3: Get 4 wood with existing wooden axe")
result = pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 4)], verbose=1)
print(f"Result: {result}\n")