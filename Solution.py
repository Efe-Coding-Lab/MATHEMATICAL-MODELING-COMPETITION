# All code is automated, meaning only the number of cars can be changed, and all values can be calculated automatically.
# Extra graphs can be added easily, but I haven't added them to keep it simple.

# Car Data
car_count = 3162884
annual_tree_co2_consumption = 6600
# The annual CO2 consumption of a tree is calculated as 2,640 on average in 2.5 hours, totaling 6,600.

# Population Data
total_population = 15840900
# One person produces 0.625kg of CO2 in 1 hour. In a year, there are 365x24=8,760 hours, resulting in 5,475kg of CO2 per person.
total_co2_emission_by_individuals = 15840900 * 5475

# Car Fuel Types
lpg = car_count * 353 / 1000
diesel = car_count * 351 / 1000
gasoline = car_count * 269 / 1000
hybrid_electric = car_count * 9 / 1000
other = car_count * 3 / 1000
# Calculating the proportion of each type of car.

def car_model_split(x):
    renault_count = x * 158 / 1000
    volkswagen_count = x * 108 / 1000
    fiat_count = x * 111 / 1000
    dacia_count = x * 43 / 1000
    opel_count = x * 55 / 1000
    hyundai_count = x * 60 / 1000
    ford_count = x * 66 / 1000
    toyota_count = x * 51 / 1000
    mercedes_count = x * 43 / 1000
    nissan_count = x * 42 / 1000
    other_models = x * 265 / 1000
    return (
        renault_count,
        volkswagen_count,
        fiat_count,
        dacia_count,
        opel_count,
        hyundai_count,
        ford_count,
        toyota_count,
        mercedes_count,
        nissan_count,
        other_models,
    )
# Calculating how many cars of each model there are.

# Importing pandas library
import pandas as pd
df = pd.read_csv("data.csv", decimal=",")
df

# Calculating fuel consumption for LPG and hybrid cars based on the CO2 emissions of gasoline cars.

df["lpg_usage"] = df["CO2_gasoline(gr/km)"] * 8 / 10
df["hybrid_usage"] = df["CO2_gasoline(gr/km)"] * 95 / 100

car_count_df = pd.DataFrame()
car_count_df["Car Brands"] = df["Car Brands"]
car_count_df["lpg_car_count"] = car_model_split(lpg)
car_count_df["diesel_car_count"] = car_model_split(diesel)
car_count_df["gasoline_car_count"] = car_model_split(gasoline)
car_count_df["hybrid_car_count"] = car_model_split(hybrid_electric)
car_count_df["other_car_count"] = car_model_split(other)

car_co2_emission_amount = pd.DataFrame()
car_co2_emission_amount["Car Brands"] = df["Car Brands"]
car_co2_emission_amount["lpg_co2_emission_amount"] = (
    car_count_df["lpg_car_count"] * df["lpg_usage"] * 15000
)
car_co2_emission_amount["diesel_co2_emission_amount"] = (
    car_count_df["diesel_car_count"] * df["CO2_diesel(gr/km)"] * 15000
)
car_co2_emission_amount["gasoline_co2_emission_amount"] = (
    car_count_df["gasoline_car_count"] * df["CO2_gasoline(gr/km)"] * 15000
)
car_co2_emission_amount["hybrid_co2_emission_amount"] = (
    car_count_df["hybrid_car_count"] * df["hybrid_usage"] * 15000
)
car_co2_emission_amount["other_co2_emission_amount"] = (
    car_count_df["other_car_count"] * 0 * 15000
)
# Assuming 15,000 km as a basis, multiplying model-specific values automatically.

# Calculating the total CO2 emissions from LPG cars.
total_lpg_co2 = car_co2_emission_amount["lpg_co2_emission_amount"].sum()
# Calculating the total CO2 emissions from diesel cars.
total_diesel_co2 = car_co2_emission_amount["diesel_co2_emission_amount"].sum()
# Calculating the total CO2 emissions from gasoline cars.
total_gasoline_co2 = car_co2_emission_amount["gasoline_co2_emission_amount"].sum()
# Calculating the total CO2 emissions from hybrid cars.
total_hybrid_co2 = car_co2_emission_amount["hybrid_co2_emission_amount"].sum()
# Calculating the total CO2 emissions from other cars.
total_other_co2 = car_co2_emission_amount["other_co2_emission_amount"].sum()
# Calculating the total CO2 emissions from all cars.
total_co2_emission_from_all_cars = (
    total_other_co2 + total_gasoline_co2 + total_diesel_co2 + total_hybrid_co2 + total_lpg_co2
)

a = total_co2_emission_from_all_cars / annual_tree_co2_consumption
a

# The required number of trees for all cars and individuals to reduce their annual CO2 emission to zero.
total_co2_emission_from_individuals = total_population * 5475
total_tree_count_needed = (
    total_co2_emission_from_individuals / annual_tree_co2_consumption
)
total_tree_count_needed
# The total number of trees required to offset the CO2 emissions from all cars and individuals and reduce it to zero.
