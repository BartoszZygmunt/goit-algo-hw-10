import pulp

# Create a problem variable
prob = pulp.LpProblem("Beverage_Production", pulp.LpMaximize)

# Decision variables: quantities of Lemonade and Fruit Juice to produce
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Resource constraints
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Constraints for resource usage
prob += 2 * lemonade + 1 * fruit_juice <= water_limit, "Water"
prob += 1 * lemonade <= sugar_limit, "Sugar"
prob += 1 * lemonade <= lemon_juice_limit, "Lemon_Juice"
prob += 2 * fruit_juice <= fruit_puree_limit, "Fruit_Puree"

# Objective function: Maximize total production (Lemonade + Fruit Juice)
prob += lemonade + fruit_juice, "Total_Production"

# Solve the problem
prob.solve()

# Print the results
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Optimal production of Lemonade: {lemonade.varValue} units")
print(f"Optimal production of Fruit Juice: {fruit_juice.varValue} units")
