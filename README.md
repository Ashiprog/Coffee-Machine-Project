# Coffee-Machine-Project
Simulates a coffee maker machine in Python. Users select coffee types (espresso, latte, cappuccino), manage ingredient inventory, and calculate costs. A practical exercise for learning Python programming, covering functions, conditionals, and simulation of coffee-making processes.

Menu and Resources Initialization
Menu Definition:
The MENU dictionary defines three types of coffee (espresso, latte, cappuccino) with specific ingredients and cost.

Initial Resources:
The resources dictionary initializes available quantities of water, milk, coffee, and money.

Functions
Machine Report Function:
machine_report() prints the current status of resources (water, milk, coffee, money).

Check Coffee Resources Function:
check_coffee_resources(coffee) verifies if there are enough ingredients to make the selected coffee.

Check Money Function:
check_money(coffee) validates if the inserted coins are sufficient to purchase the selected coffee.

Make Coffee Function:
make_coffee(coffee) deducts required ingredients from resources after making the selected coffee.

Main Program Execution
Main Program Loop:
Continuously interacts with the coffee maker until the user chooses to turn it off.


Usage Instructions:
Run the Python script.
Select a coffee type (espresso, latte, cappuccino), check resources with "report", or turn off the machine with "off".

Inserting Coins:
After selecting a coffee type, insert coins (quarters, dimes, nickles, pennies) as prompted.

Enjoying Coffee:
If sufficient resources and money are available, the program dispenses the selected coffee and calculates change.
Exiting the Program:

Use "off" to exit the program when finished.
