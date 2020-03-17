import numpy as np
import datetime as dt

# Dictionary of general categories and their calorie per lb density
densities = {"Vegetables"   : 100.0,
            "Fruits"        : 300.0,
            "UnProcCC"      : 500.0,
            "Legumes"       : 600.0,
            "AnimalProd"    : 1000.0,
            "ProcCC"        : 1400.0,
            "JunkFood"      : 2300.0,
            "NutsSeeds"     : 2800.0,
            "OilFat"        : 4000.0
}

################### CLASSES ########################
class Meal:
    # Initializer
    def __init__(self,category,weight):
        self.category = category
        self.weight = weight
        self.date = dt.date.today()
        self.list = [[category,weight]]

    def add_item(self,category,weight):
        self.list.append([category,weight])

    def change_date(self,year,month,day):
        self.date = dt.date(year,month,day)





################### FUNCTIONS ######################
# Get the weight of a single meal
def get_mealweight(Meal):
    mealweight = 0.0
    for row in Meal.list:
        mealweight += row[1]
    return mealweight


# Get the average calorie density for a given meal
def avg_cal_density_meal(Meal):
    avg_cal_density = 0.0
    weightsum = get_mealweight(Meal)
    for row in Meal.list:
        avg_cal_density += row[1]*densities[row[0]]/weightsum
    return avg_cal_density
