city_name = "Istanbul,Turkey"
pop_1927 = 691000
pop_2017 = 15029231

pop_change = pop_1927 - pop_2017

percentage_gr = (pop_change / pop_1927) * 100

annual_gr = percentage_gr/(2017-1927)

print(annual_gr)


def population_growth(year_one, year_two, population_one, population_two):

    pop_change = population_two - population_one

    percentage_gr = (pop_change / population_one) * 100

    growth_rate = percentage_gr/year_two - year_one

    return growth_rate


set_one = population_growth(1927, 2017, pop_1927, pop_2017)

set_two = population_growth(1950, 2000, 983000,	8831800)

print(set_one)
print(set_two)

report = "The population grew from " + str(1927) + "to" + str(pop_2017)
+ "with a total change of " + str(pop_change) + " the annual percentage gr was"
+ str(annual_gr)

print(report)
