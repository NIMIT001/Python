def calculate_fuel_consumption():
    try:
        liters = float(input("Enter the number of liters to fill the tank: "))
        distance = float(input("Enter the distance covered: "))
        
        if liters <= 0 or distance <= 0:
            print("Invalid Input")
            return
        
        # European format: Liters per 100KM
        liters_per_100km = (liters / distance) * 100
        
        # Convert to U.S. format
        miles = distance * 0.6214
        gallons = liters * 0.2642
        miles_per_gallon = miles / gallons
        
        # Print results with two decimal places
        print("Liters/100KM")
        print(f"{liters_per_100km:.2f}")#.2f is used for limiting the number to two decimal 
        print("Miles/gallons")
        print(f"{miles_per_gallon:.2f}")
    
    except ValueError:
        print("Invalid Input")

# Run the function
calculate_fuel_consumption()