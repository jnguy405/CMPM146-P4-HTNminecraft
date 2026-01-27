import pyhop

'''begin operators'''

def op_punch_for_wood(state, ID):
	if state.time[ID] >= 4:
		state.wood[ID] += 1
		state.time[ID] -= 4
		return state
	return False

def op_craft_wooden_axe_at_bench(state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >=2:
		state.wooden_axe[ID] += 1
		state.plank[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

# Syntax for adding more operators:
# op_def operator_name(state, ID):
# if state.time[ID] >= required_time and state.resource1[ID] >= required_amount1 and ... :
# state.resourceX[ID] += change_in_resourceX
# state.resourceY[ID] -= change_in_resourceY
# state.time[ID] -= required_time
# return state
# return False
# ------------------------------------------------

# your code here

pyhop.declare_operators(op_punch_for_wood, op_craft_wooden_axe_at_bench)

'''end operators'''

def check_enough(state, ID, item, num):
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough(state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

def produce(state, ID, item):
    if item == 'wood': 
        return [('produce_wood', ID)]
    
    elif item == 'plank':
        return [('have_enough', ID, 'wood', 1), ('op_craft_plank', ID)]
    
    elif item == 'stick':
        return [('have_enough', ID, 'plank', 2), ('op_craft_stick', ID)]
    
    elif item == 'bench':
        if getattr(state, 'made_bench', {}).get(ID, False) is True:
            return False
        else:
            state.made_bench[ID] = True
        return [('have_enough', ID, 'plank', 4), ('op_craft_bench', ID)]
    
    elif item == 'wooden_axe':
        if getattr(state, 'made_wooden_axe', {}).get(ID, False) is True:
            return False
        else:
            state.made_wooden_axe[ID] = True
        return [('produce_wooden_axe', ID)]
    
    elif item == 'wooden_pickaxe':
        if getattr(state, 'made_wooden_pickaxe', {}).get(ID, False) is True:
            return False
        else:
            state.made_wooden_pickaxe[ID] = True
        return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'plank', 3), ('have_enough', ID, 'stick', 2), ('op_craft_wooden_pickaxe_at_bench', ID)]
    
    elif item == 'stone_axe':
        if getattr(state, 'made_stone_axe', {}).get(ID, False) is True:
            return False
        else:
            state.made_stone_axe[ID] = True
        return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'cobble', 3), ('have_enough', ID, 'stick', 2), ('op_craft_stone_axe_at_bench', ID)]
    
    elif item == 'stone_pickaxe':
        if getattr(state, 'made_stone_pickaxe', {}).get(ID, False) is True:
            return False
        else:
            state.made_stone_pickaxe[ID] = True
        return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'cobble', 3), ('have_enough', ID, 'stick', 2), ('op_craft_stone_pickaxe_at_bench', ID)]
    
    elif item == 'furnace':
        if getattr(state, 'made_furnace', {}).get(ID, False) is True:
            return False
        else:
            state.made_furnace[ID] = True
        return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'cobble', 8), ('op_craft_furnace_at_bench', ID)]
    
    elif item == 'iron_axe':
        if getattr(state, 'made_iron_axe', {}).get(ID, False) is True:
            return False
        else:
            state.made_iron_axe[ID] = True
        return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 3), ('have_enough', ID, 'stick', 2), ('op_craft_iron_axe_at_bench', ID)]
    
    elif item == 'iron_pickaxe':
        if getattr(state, 'made_iron_pickaxe', {}).get(ID, False) is True:
            return False
        else:
            state.made_iron_pickaxe[ID] = True
        return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 3), ('have_enough', ID, 'stick', 2), ('op_craft_iron_pickaxe_at_bench', ID)]
    
    elif item == 'ingot':
        return [('have_enough', ID, 'furnace', 1), ('have_enough', ID, 'coal', 1), ('have_enough', ID, 'ore', 1), ('op_smelt_ore_in_furnace', ID)]
    
    elif item == 'coal':
        # multiple ways to get coal
        # try iron_pickaxe first (fastest)
        if state.iron_pickaxe.get(ID, 0) >= 1:
            return [('op_iron_pickaxe_for_coal', ID)]
        elif state.stone_pickaxe.get(ID, 0) >= 1:
            return [('op_stone_pickaxe_for_coal', ID)]
        elif state.wooden_pickaxe.get(ID, 0) >= 1:
            return [('op_wooden_pickaxe_for_coal', ID)]
        else:
            return False  # need a pickaxe
    
    elif item == 'ore':
        # multiple ways to get ore
        if state.iron_pickaxe.get(ID, 0) >= 1:
            return [('op_iron_pickaxe_for_ore', ID)]
        elif state.stone_pickaxe.get(ID, 0) >= 1:
            return [('op_stone_pickaxe_for_ore', ID)]
        else:
            return False  # need an appropriate pickaxe
    
    elif item == 'cobble':
        # multiple ways to get cobble
        if state.iron_pickaxe.get(ID, 0) >= 1:
            return [('op_iron_pickaxe_for_cobble', ID)]
        elif state.stone_pickaxe.get(ID, 0) >= 1:
            return [('op_stone_pickaxe_for_cobble', ID)]
        elif state.wooden_pickaxe.get(ID, 0) >= 1:
            return [('op_wooden_pickaxe_for_cobble', ID)]
        else:
            return False  # need a pickaxe
    
    elif item == 'rail':
        if getattr(state, 'made_rail', {}).get(ID, False) is True:
            return False
        else:
            state.made_rail[ID] = True
        return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 6), ('have_enough', ID, 'stick', 1), ('op_craft_rail_at_bench', ID)]
    
    elif item == 'cart':
        if getattr(state, 'made_cart', {}).get(ID, False) is True:
            return False
        else:
            state.made_cart[ID] = True
        return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 5), ('op_craft_cart_at_bench', ID)]
    
    else:
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
pyhop.declare_methods('produce_wood', punch_for_wood, wooden_axe_for_wood, stone_axe_for_wood, iron_axe_for_wood)
pyhop.declare_methods('produce_plank', craft_plank)
pyhop.declare_methods('produce_stick', craft_stick)
pyhop.declare_methods('produce_bench', craft_bench)
pyhop.declare_methods('produce_wooden_axe', craft_wooden_axe_at_bench)
pyhop.declare_methods('produce_wooden_pickaxe', craft_wooden_pickaxe_at_bench)
pyhop.declare_methods('produce_stone_axe', craft_stone_axe_at_bench)
pyhop.declare_methods('produce_stone_pickaxe', craft_stone_pickaxe_at_bench)
pyhop.declare_methods('produce_furnace', craft_furnace_at_bench)
pyhop.declare_methods('produce_iron_axe', craft_iron_axe_at_bench)
pyhop.declare_methods('produce_iron_pickaxe', craft_iron_pickaxe_at_bench)
pyhop.declare_methods('produce_ingot', smelt_ore_in_furnace)
pyhop.declare_methods('produce_coal', wooden_pickaxe_for_coal, stone_pickaxe_for_coal, iron_pickaxe_for_coal)
pyhop.declare_methods('produce_ore', stone_pickaxe_for_ore, iron_pickaxe_for_ore)
pyhop.declare_methods('produce_cobble', wooden_pickaxe_for_cobble, stone_pickaxe_for_cobble, iron_pickaxe_for_cobble)
pyhop.declare_methods('produce_rail', craft_rail_at_bench)
pyhop.declare_methods('produce_cart', craft_cart_at_bench)

'''end recipe methods'''

# declare state
state = pyhop.State('state')
state.wood = {'agent': 0}
state.time = {'agent': 4}
# state.time = {'agent': 46}
state.wooden_axe = {'agent': 0}
state.made_wooden_axe = {'agent': False}

# Syntax for adding more resources to the state:
# state.resource_name = {'agent': initial_amount}
# ------------------------------------------------

# your code here 

# pyhop.print_operators()
# pyhop.print_methods()

pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 1)], verbose=3)
# pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 12)], verbose=3)