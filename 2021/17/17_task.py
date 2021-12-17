def step(x_pos, y_pos, x_vel, y_vel):
    """
    Perform one step in simulation and update positions and velocities
    Args:
        x_pos: X position
        y_pos: Y position
        x_vel: X velocity
        y_vel: Y velocity

    Returns: Updated positions and velocities
    """
    x_pos = x_pos + x_vel
    y_pos = y_pos + y_vel
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
    y_vel -= 1
    return x_pos, y_pos, x_vel, y_vel

# Ocean trench to hit
target_x0, target_x1, target_y0, target_y1 = 56, 76, -162, -134

# Variables to store highest y value for all tries and number of starting velocities that give a hit
highest_y_total = 0
hit_count = 0

# Run simulation for set of starting velocities
for x_vel_start in range(target_x1 + 1):
    for y_vel_start in range(target_y0, abs(target_y0)):

        # Set initial conditions, as well as variable to track if we hit ocean trench and highest y position for these
        # conditions
        x, y, x_vel, y_vel = 0, 0, x_vel_start, y_vel_start
        hit = False
        highest_y_single = 0

        # Run simulation steps only while we are above minimal y value and have not hit target yet
        while y >= target_y0 and not hit:

            # Update initial conditions for each step
            x, y, x_vel, y_vel = step(x, y, x_vel, y_vel)

            # Update highest y val for these initial conditions, and check if we have hit the target
            highest_y_single = max(y, highest_y_single)
            if target_x0 <= x <= target_x1 and target_y0 <= y <= target_y1:
                hit = True

        # If we hit the target, update highest y val for all simulations, and hit count
        if hit:
            highest_y_total = max(highest_y_single, highest_y_total)
            hit_count += 1

print(f'Highest y position of all trajectories = {highest_y_total}')
print(f'Number of trajectories resulting in a hit = {hit_count}')
