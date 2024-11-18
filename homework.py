# Function to calculate speed
def calculate_speed(distance, time):
    return distance / time

# Function to calculate acceleration
def calculate_acceleration(initial_velocity, final_velocity, time):
    return (final_velocity - initial_velocity) / time

# Function to calculate power (using work and time)
def calculate_power(work, time):
    return work / time

# Function to calculate power (using force and velocity)
def calculate_power_from_force_velocity(force, velocity):
    return force * velocity

# Function to calculate momentum
def calculate_momentum(mass, velocity):
    return mass * velocity

# Function to calculate the first equation of motion (v = u + at)
def calculate_final_velocity(initial_velocity, acceleration, time):
    return initial_velocity + acceleration * time

# Main code to interact with the user
def main():
    # Ask for inputs and calculate speed
    distance = float(input("Enter the distance (d) in meters: "))
    time = float(input("Enter the time (t) in seconds: "))
    speed = calculate_speed(distance, time)
    print(f"Speed: {speed} m/s")

    # Ask for inputs and calculate acceleration
    initial_velocity = float(input("Enter the initial velocity (u) in m/s: "))
    final_velocity = float(input("Enter the final velocity (v) in m/s: "))
    acceleration_time = float(input("Enter the time (t) in seconds for acceleration: "))
    acceleration = calculate_acceleration(initial_velocity, final_velocity, acceleration_time)
    print(f"Acceleration: {acceleration} m/s²")

    # Ask for inputs and calculate power (work and time)
    work = float(input("Enter the work done (W) in joules: "))
    power_time = float(input("Enter the time (t) in seconds for power calculation: "))
    power = calculate_power(work, power_time)
    print(f"Power: {power} watts")

    # Ask for inputs and calculate power (force and velocity)
    force = float(input("Enter the force (F) in newtons: "))
    velocity = float(input("Enter the velocity (v) in m/s for power calculation: "))
    power_from_force_velocity = calculate_power_from_force_velocity(force, velocity)
    print(f"Power (using force and velocity): {power_from_force_velocity} watts")

    # Ask for inputs and calculate momentum
    mass = float(input("Enter the mass (m) in kilograms: "))
    momentum_velocity = float(input("Enter the velocity (v) in m/s for momentum calculation: "))
    momentum = calculate_momentum(mass, momentum_velocity)
    print(f"Momentum: {momentum} kg·m/s")

    # Ask for inputs and calculate final velocity (first equation of motion)
    initial_velocity_motion = float(input("Enter the initial velocity (u) in m/s for equation of motion: "))
    acceleration_motion = float(input("Enter the acceleration (a) in m/s²: "))
    time_motion = float(input("Enter the time (t) in seconds for the equation of motion: "))
    final_velocity_motion = calculate_final_velocity(initial_velocity_motion, acceleration_motion, time_motion)
    print(f"Final velocity (v) using the first equation of motion: {final_velocity_motion} m/s")

# Run the main function
if __name__ == "__main__":
    main()
