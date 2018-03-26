import math

journal = [
  {"events":["carrot","exercise","weekend"],"squirrel":False},
  {"events":["bread","pudding","brushed teeth","weekend","touched tree"],"squirrel":False},
  {"events":["carrot","nachos","brushed teeth","cycling","weekend"],"squirrel":False},
  {"events":["brussel sprouts","ice cream","brushed teeth","computer","weekend"],"squirrel":False},
  {"events":["potatoes","candy","brushed teeth","exercise","weekend","dentist"],"squirrel":False},
  {"events":["brussel sprouts","pudding","brushed teeth","running","weekend"],"squirrel":False},
  {"events":["pizza","brushed teeth","computer","work","touched tree"],"squirrel":False},
  {"events":["bread","beer","brushed teeth","cycling","work"],"squirrel":False},
  {"events":["cauliflower","brushed teeth","work"],"squirrel":False},
  {"events":["pizza","brushed teeth","cycling","work"],"squirrel":False},
  {"events":["lasagna","nachos","brushed teeth","work"],"squirrel":False},
  {"events":["brushed teeth","weekend","touched tree"],"squirrel":False},
  {"events":["lettuce","brushed teeth","television","weekend"],"squirrel":False},
  {"events":["spaghetti","brushed teeth","work"],"squirrel":False},
  {"events":["brushed teeth","computer","work"],"squirrel":False},
  {"events":["lettuce","nachos","brushed teeth","work"],"squirrel":False},
  {"events":["carrot","brushed teeth","running","work"],"squirrel":False},
  {"events":["brushed teeth","work"],"squirrel":False},
  {"events":["cauliflower","reading","weekend"],"squirrel":False},
  {"events":["bread","brushed teeth","weekend"],"squirrel":False},
  {"events":["lasagna","brushed teeth","exercise","work"],"squirrel":False},
  {"events":["spaghetti","brushed teeth","reading","work"],"squirrel":False},
  {"events":["carrot","ice cream","brushed teeth","television","work"],"squirrel":False},
  {"events":["spaghetti","nachos","work"],"squirrel":False},
  {"events":["cauliflower","ice cream","brushed teeth","cycling","work"],"squirrel":False},
  {"events":["spaghetti","peanuts","computer","weekend"],"squirrel":True},
  {"events":["potatoes","ice cream","brushed teeth","computer","weekend"],"squirrel":False},
  {"events":["potatoes","ice cream","brushed teeth","work"],"squirrel":False},
  {"events":["peanuts","brushed teeth","running","work"],"squirrel":False},
  {"events":["potatoes","exercise","work"],"squirrel":False},
  {"events":["pizza","ice cream","computer","work"],"squirrel":False},
  {"events":["lasagna","ice cream","work"],"squirrel":False},
  {"events":["cauliflower","candy","reading","weekend"],"squirrel":False},
  {"events":["lasagna","nachos","brushed teeth","running","weekend"],"squirrel":False},
  {"events":["potatoes","brushed teeth","work"],"squirrel":False},
  {"events":["carrot","work"],"squirrel":False},
  {"events":["pizza","beer","work","dentist"],"squirrel":False},
  {"events":["lasagna","pudding","cycling","work"],"squirrel":False},
  {"events":["spaghetti","brushed teeth","reading","work"],"squirrel":False},
  {"events":["spaghetti","pudding","television","weekend"],"squirrel":False},
  {"events":["bread","brushed teeth","exercise","weekend"],"squirrel":False},
  {"events":["lasagna","peanuts","work"],"squirrel":True},
  {"events":["pizza","work"],"squirrel":False},
  {"events":["potatoes","exercise","work"],"squirrel":False},
  {"events":["brushed teeth","exercise","work"],"squirrel":False},
  {"events":["spaghetti","brushed teeth","television","work"],"squirrel":False},
  {"events":["pizza","cycling","weekend"],"squirrel":False},
  {"events":["carrot","brushed teeth","weekend"],"squirrel":False},
  {"events":["carrot","beer","brushed teeth","work"],"squirrel":False},
  {"events":["pizza","peanuts","candy","work"],"squirrel":True},
  {"events":["carrot","peanuts","brushed teeth","reading","work"],"squirrel":False},
  {"events":["potatoes","peanuts","brushed teeth","work"],"squirrel":False},
  {"events":["carrot","nachos","brushed teeth","exercise","work"],"squirrel":False},
  {"events":["pizza","peanuts","brushed teeth","television","weekend"],"squirrel":False},
  {"events":["lasagna","brushed teeth","cycling","weekend"],"squirrel":False},
  {"events":["cauliflower","peanuts","brushed teeth","computer","work","touched tree"],"squirrel":False},
  {"events":["lettuce","brushed teeth","television","work"],"squirrel":False},
  {"events":["potatoes","brushed teeth","computer","work"],"squirrel":False},
  {"events":["bread","candy","work"],"squirrel":False},
  {"events":["potatoes","nachos","work"],"squirrel":False},
  {"events":["carrot","pudding","brushed teeth","weekend"],"squirrel":False},
  {"events":["carrot","brushed teeth","exercise","weekend","touched tree"],"squirrel":False},
  {"events":["brussel sprouts","running","work"],"squirrel":False},
  {"events":["brushed teeth","work"],"squirrel":False},
  {"events":["lettuce","brushed teeth","running","work"],"squirrel":False},
  {"events":["candy","brushed teeth","work"],"squirrel":False},
  {"events":["brussel sprouts","brushed teeth","computer","work"],"squirrel":False},
  {"events":["bread","brushed teeth","weekend"],"squirrel":False},
  {"events":["cauliflower","brushed teeth","weekend"],"squirrel":False},
  {"events":["spaghetti","candy","television","work","touched tree"],"squirrel":False},
  {"events":["carrot","pudding","brushed teeth","work"],"squirrel":False},
  {"events":["lettuce","brushed teeth","work"],"squirrel":False},
  {"events":["carrot","ice cream","brushed teeth","cycling","work"],"squirrel":False},
  {"events":["pizza","brushed teeth","work"],"squirrel":False},
  {"events":["spaghetti","peanuts","exercise","weekend"],"squirrel":True},
  {"events":["bread","beer","computer","weekend","touched tree"],"squirrel":False},
  {"events":["brushed teeth","running","work"],"squirrel":False},
  {"events":["lettuce","peanuts","brushed teeth","work","touched tree"],"squirrel":False},
  {"events":["lasagna","brushed teeth","television","work"],"squirrel":False},
  {"events":["cauliflower","brushed teeth","running","work"],"squirrel":False},
  {"events":["carrot","brushed teeth","running","work"],"squirrel":False},
  {"events":["carrot","reading","weekend"],"squirrel":False},
  {"events":["carrot","peanuts","reading","weekend"],"squirrel":True},
  {"events":["potatoes","brushed teeth","running","work"],"squirrel":False},
  {"events":["lasagna","ice cream","work","touched tree"],"squirrel":False},
  {"events":["cauliflower","peanuts","brushed teeth","cycling","work"],"squirrel":False},
  {"events":["pizza","brushed teeth","running","work"],"squirrel":False},
  {"events":["lettuce","brushed teeth","work"],"squirrel":False},
  {"events":["bread","brushed teeth","television","weekend"],"squirrel":False},
  {"events":["cauliflower","peanuts","brushed teeth","weekend"],"squirrel":False}
]

def phi(table):
	return (table[3] * table[0] - table[2] * table[1]) / (math.sqrt((table[2] + table[3]) * (table[0] + table[1]) * (table[1] + table[3]) * (table[0] + table[2])))

# check if the event is found
def hasEvent(event, entry):
	if event in entry['events']:
		return entry['events'].index(event)

def tableFor(event, journal):
	table = [0, 0, 0, 0]
	# loop in to the journal
	for x in range(len(journal)):
		entry = journal[x]
		index = 0	
		# print(entry)
		if event in entry['events']:
			index += 1
		
		if entry['squirrel']:
			index += 2

		table[index] += 1

	return table

def gatherCorrelations(journal):
	phis = {}

	for i in range(len(journal)):
		events = journal[i]['events']
		for x in range(len(events)):
			event = events[x]
			if event not in phis:
				phis[event] = phi(tableFor(event, journal))

	return phis



correlations = gatherCorrelations(journal)
for x, val in correlations.items():
	correlation = correlations[x]
	if correlation > 0.1 or correlation < -0.1:
		print(x + ": " + str(val))

