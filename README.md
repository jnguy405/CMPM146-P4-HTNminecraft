# CMPM 146 P4 HTN Minecraft

## Jenalee Nguyen and Neila Miranda

The autoHTN heuristic:


For this heuristic we have tried many different variations to each test case to pass.


Checking the current task that we are in, given by the parameter that holds the subtasks list. We first check if there is something to be produced then we get the item we are trying to create.


Next, in a loop that checks the calling_stack we get the task that's in the stack. If the item and the task item are the same we prune this current check and return true


The next check is to see if we have enough of the resource to craft the goal item. If the goal amount for the craft is higher than zero and meet the required craftable amount then prune this check and return true.


Finally we have one more check for time; it simply checks if we have enough time for the craft to continue.


When all checks are done and nothing passed then the function return False, meaning that the system keeps on searching for the next step  

