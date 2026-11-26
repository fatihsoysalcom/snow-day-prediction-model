import random

def predict_snow_day(temperature_celsius, snowfall_mm, school_closure_threshold_temp, school_closure_threshold_snow):
    """
    A simplified model to predict a snow day based on temperature and snowfall.

    Args:
        temperature_celsius (float): The current temperature in Celsius.
        snowfall_mm (float): The amount of snowfall in millimeters.
        school_closure_threshold_temp (float): The maximum temperature for a potential snow day.
        school_closure_threshold_snow (float): The minimum snowfall required for a potential snow day.

    Returns:
        bool: True if a snow day is predicted, False otherwise.
    """
    # Core logic: If it's cold enough AND there's enough snow, predict a snow day.
    if temperature_celsius <= school_closure_threshold_temp and snowfall_mm >= school_closure_threshold_snow:
        # Add a small random chance to simulate real-world unpredictability
        # In a real system, this would be based on more complex factors or historical data.
        return random.random() > 0.1 # 90% chance of snow day if conditions met
    else:
        return False

if __name__ == "__main__":
    # --- Configuration --- 
    # These thresholds would be determined by historical data and local school board policies
    # in a real-world application.
    MAX_TEMP_FOR_SNOW_DAY = -2.0  # Celsius
    MIN_SNOWFALL_FOR_SNOW_DAY = 50.0 # millimeters

    # --- Simulation --- 
    print("--- SnowDayCA - Simplified Prediction ---")

    # Scenario 1: Cold and snowy
    temp1 = -5.0
    snow1 = 75.0
    prediction1 = predict_snow_day(temp1, snow1, MAX_TEMP_FOR_SNOW_DAY, MIN_SNOWFALL_FOR_SNOW_DAY)
    print(f"\nScenario 1: Temp={temp1}°C, Snowfall={snow1}mm")
    print(f"Prediction: {'Snow Day!' if prediction1 else 'School Open'}")

    # Scenario 2: Cold but not enough snow
    temp2 = -3.0
    snow2 = 20.0
    prediction2 = predict_snow_day(temp2, snow2, MAX_TEMP_FOR_SNOW_DAY, MIN_SNOWFALL_FOR_SNOW_DAY)
    print(f"\nScenario 2: Temp={temp2}°C, Snowfall={snow2}mm")
    print(f"Prediction: {'Snow Day!' if prediction2 else 'School Open'}")

    # Scenario 3: Snowy but not cold enough
    temp3 = 1.0
    snow3 = 60.0
    prediction3 = predict_snow_day(temp3, snow3, MAX_TEMP_FOR_SNOW_DAY, MIN_SNOWFALL_FOR_SNOW_DAY)
    print(f"\nScenario 3: Temp={temp3}°C, Snowfall={snow3}mm")
    print(f"Prediction: {'Snow Day!' if prediction3 else 'School Open'}")

    # Scenario 4: Mild weather
    temp4 = 3.0
    snow4 = 5.0
    prediction4 = predict_snow_day(temp4, snow4, MAX_TEMP_FOR_SNOW_DAY, MIN_SNOWFALL_FOR_SNOW_DAY)
    print(f"\nScenario 4: Temp={temp4}°C, Snowfall={snow4}mm")
    print(f"Prediction: {'Snow Day!' if prediction4 else 'School Open'}")
