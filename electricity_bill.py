def calculate_bill(units):
    fixed_charge = 150
    energy_charge = 0

    if units <= 100:
        energy_charge = units * 4.50
    elif units <= 300:
        energy_charge = (100 * 4.50) + (units - 100) * 6.00
    elif units <= 600:
        energy_charge = (100 * 4.50) + (200 * 6.00) + (units - 300) * 8.00
    else:
        energy_charge = (100 * 4.50) + (200 * 6.00) + (300 * 8.00) + (units - 600) * 11.00

    total_bill = energy_charge + fixed_charge

    # Apply 7% surcharge if energy charge exceeds 4000
    if energy_charge > 4000:
        surcharge = energy_charge * 0.07
        total_bill += surcharge
        print(f"Energy Charge: Rs. {energy_charge:.2f}")
        print(f"Surcharge (7%): Rs. {surcharge:.2f}")
    else:
        print(f"Energy Charge: Rs. {energy_charge:.2f}")

    print(f"Meter Charge: Rs. {fixed_charge:.2f}")
    print(f"Total Bill Amount: Rs. {total_bill:.2f}")
    return total_bill

# Example usage:
units_consumed = 650
print(f"Units Consumed: {units_consumed}")
calculate_bill(units_consumed)