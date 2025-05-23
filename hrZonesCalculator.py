# Given data
age = 30
resting_heart_rate = 73  # bpm
max_heart_rate = 220 - age  # Estimated maximum heart rate
heart_rate_reserve = max_heart_rate - resting_heart_rate

# Calculate heart rate zones using the Karvonen formula
zones = {
    "Zone 1 (50-60%)": ((heart_rate_reserve * 0.50) + resting_heart_rate, (heart_rate_reserve * 0.60) + resting_heart_rate),
    "Zone 2 (60-70%)": ((heart_rate_reserve * 0.60) + resting_heart_rate, (heart_rate_reserve * 0.70) + resting_heart_rate),
    "Zone 3 (70-80%)": ((heart_rate_reserve * 0.70) + resting_heart_rate, (heart_rate_reserve * 0.80) + resting_heart_rate),
    "Zone 4 (80-90%)": ((heart_rate_reserve * 0.80) + resting_heart_rate, (heart_rate_reserve * 0.90) + resting_heart_rate),
    "Zone 5 (90-100%)": ((heart_rate_reserve * 0.90) + resting_heart_rate, (heart_rate_reserve * 1.00) + resting_heart_rate)
}

print(zones)
