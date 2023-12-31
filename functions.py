def mrad_to_moa(mrad):
    """
    Converts MRAD to MOA.

    :param mrad: The value in MRAD.
    :type mrad: int or float

    :return: The value in MOA.
    :rtype: float
    """
    return f"{mrad} MRAD = {round(mrad * 3.4377492368197, 2)} MOA"


def moa_to_mrad(moa):
    """
    Converts MOA to MRAD.

    :param moa: The value in MOA.
    :type moa: int or float

    :return: The value in MRAD.
    :rtype: float
    """
    return f"{moa} MOA = {round(moa * 0.290888, 2)} MRAD"


def calculate_distance_to_target(target_height_in_cm, focal_height, mrad_moa=None):
    """
    Calculates the distance to a target by providing the height of a target in centimeters, its height on a focal
    plane of a scope, and units of angle measurement (MRAD or MOA).

    :param target_height_in_cm: The height of a target in centimeters.
    :type target_height_in_cm: int or float

    :param focal_height: The height of a target on a focal plane of a scope.
    :param mrad_moa: int or float

    :return: The distance to a target in meters.
    :rtype: float
    """
    if mrad_moa == 'moa':
        distance = target_height_in_cm * 34.377492368197 / focal_height
        return f"The distance is {round(distance, 2)} meters (MOA)"

    else:
        distance = target_height_in_cm * 10 / focal_height
        return f"The distance is {round(distance, 2)} meters (MRAD)"


def zeroing_mrad_10_meters(vertical=str(0), horizontal=str(0)):
    """
    Do the first shot at 10 meters and enter the result to calculate vertical and horizontal adjustments
    to zero the scope.
    If no vertical or horizontal adjustments required, type '00' in the corresponding argument value.

    :param vertical: Must include the number of centimeters from the center of the target on the vertical axis
    and the direction. For example, if you hit the target 4 centimeters above the center, you must enter '4u' or '4U'.
    On the contrary, if you hit the target 4 centimeters below the center, you must enter '4d' or '4D'.
    :type vertical: str

    :param horizontal: Must include the number of centimeters from the center of the target on the horizontal axis
    and the direction. For example, if you hit the target 7 centimeters to the left from the center,
    you must enter '7l' or '7L'. On the contrary, if you hit the target 7 centimeters to the right
    from the center, you must enter '7r' or '7R'.
    :type horizontal: str

    :return: The report that contains the adjustments you need to make to zero your scope for shooting at 100 meters.
    ":rtype: str
    """
    try:
        normal_10_meters_hit = 4.5  # at 10 meters, the bullet hits the target lower than the center

        vertical_hit = float(vertical[:-1])
        vertical_direction = vertical[-1]
        horizontal_hit = float(horizontal[:-1])
        horizontal_direction = horizontal[-1]

        vertical_adjustment_direction = 'UP' if vertical_direction == 'd' or vertical_direction == 'D' else 'DOWN'
        horizontal_adjustment_direction = 'RIGHT' if horizontal_direction == 'l' or horizontal_direction == 'L' else 'LEFT'

        one_mrad_to_distance = 1  # centimeters

        if vertical_direction == 'u' or vertical_direction == 'U':
            vertical_adjustment_in_mrad = abs(round(vertical_hit / one_mrad_to_distance + normal_10_meters_hit, 2))

        elif vertical_direction == 'd' or vertical_direction == 'D':
            vertical_adjustment_in_mrad = abs(round(vertical_hit / one_mrad_to_distance - normal_10_meters_hit, 2))
            if vertical_hit < normal_10_meters_hit:
                vertical_adjustment_direction = 'DOWN'

        else:
            vertical_adjustment_in_mrad = 0.0

        horizontal_adjustment_in_mrad = abs(round(horizontal_hit / one_mrad_to_distance, 2))

        report = f"Adjust the scope {vertical_adjustment_in_mrad} MRAD {vertical_adjustment_direction} " \
                 f"and {horizontal_adjustment_in_mrad} MRAD {horizontal_adjustment_direction}\n" \
                 f"Make {int(vertical_adjustment_in_mrad * 10)} clicks {vertical_adjustment_direction}\n" \
                 f"Make {int(horizontal_adjustment_in_mrad * 10)} clicks to the {horizontal_adjustment_direction}\n"

    except (ValueError, UnboundLocalError):
        report = f"Incorrect input!\nType your shot deviations in the following manner:\n" \
                 f"First - vertical deviations, second - horizontal deviations. Font case doesn't matter. E.g:\n" \
                 f"'4u', '2.5r', where '4u' is 4 cm above, and '2.5r' is 2.5 cm to the right from the center.\n" \
                 f"Or '7D', '3L', where '7D' is 7 cm below, and '3L' is 3 cm to the left from the center.\n"

    return report


def adjustments_mrad(distance, vertical=str(), horizontal=str()):
    """
    Do the first shot at 100 meters and enter the result to calculate vertical and horizontal adjustments to the scope.
    If no vertical or horizontal adjustments required, type '00' in the corresponding argument value.

    :param distance: The distance in meters at which you want to shoot.
    :type distance: int

    :param vertical: Must include the number of centimeters from the center of the target on the vertical axis
    and the direction. For example, if you hit the target 4 centimeters above the center, you must enter '4u' or '4U'.
    On the contrary, if you hit the target 4 centimeters below the center, you must enter '4d' or '4D'.
    :type vertical: str

    :param horizontal: Must include the number of centimeters from the center of the target on the horizontal axis
    and the direction. For example, if you hit the target 7 centimeters to the left from the center,
    you must enter '7l' or '7L'. On the contrary, if you hit the target 7 centimeters to the right
    from the center, you must enter '7r' or '7R'.
    :type horizontal: str

    :return: The report that contains the adjustments you need to make to your scope for long range shooting.
    ":rtype: str
    """
    try:
        vertical_hit = float(vertical[:-1])
        vertical_direction = vertical[-1]
        horizontal_hit = float(horizontal[:-1])
        horizontal_direction = horizontal[-1]

        vertical_adjustment_direction = 'UP' if vertical_direction == 'd' or vertical_direction == 'D' else 'DOWN'
        horizontal_adjustment_direction = 'RIGHT' if horizontal_direction == 'l' or horizontal_direction == 'L' else 'LEFT'

        one_mrad_in_cm_to_distance = round(distance / 10, 2)  # centimeters

        vertical_adjustment_in_mrad = abs(round(vertical_hit / one_mrad_in_cm_to_distance, 2))
        horizontal_adjustment_in_mrad = abs(round(horizontal_hit / one_mrad_in_cm_to_distance, 2))

        report = f"To hit the target at {distance} meters, " \
                 f"adjust the scope {vertical_adjustment_in_mrad} MRAD {vertical_adjustment_direction} " \
                 f"and {horizontal_adjustment_in_mrad} MRAD {horizontal_adjustment_direction}\n" \
                 f"Make {int(vertical_adjustment_in_mrad * 10)} clicks {vertical_adjustment_direction}\n" \
                 f"Make {int(horizontal_adjustment_in_mrad * 10)} clicks to the {horizontal_adjustment_direction}\n"

    except (ValueError, UnboundLocalError):
        report = f"Incorrect input!\nType your shot deviations in the following manner:\n" \
                 f"First - vertical deviations, second - horizontal deviations. Font case doesn't matter. E.g:\n" \
                 f"'4u', '2.5r', where '4u' is 4 cm above, and '2.5r' is 2.5 cm to the right from the center.\n" \
                 f"Or '7D', '3L', where '7D' is 7 cm below, and '3L' is 3 cm to the left from the center.\n"

    return report


def bullet_time_of_flight(distance, muzzle_velocity=800):
    """
    This function calculates and plot the bullet drop depending on the distance, bullet weight, and muzzle velocity.

    :param distance: The distance to a target in meters.
    :type distance: float

    :param muzzle_velocity: The muzzle velocity. By default, it equals 800 meters per second.
    :type muzzle_velocity: float

    :return: The time of bullet flight to a target in seconds
    :rtype: float
    """

    time_of_flight = round(float((distance * 2) / muzzle_velocity), 2)

    return f"The bullet will hit the target in {time_of_flight} seconds at {distance}-meter distance."


def bullet_drop(distance, muzzle_velocity=800, gravity=9.81):
    """
    This function calculates and plot the bullet drop depending on the distance, bullet weight, and muzzle velocity.

    :param distance: The distance to a target in meters.
    :type distance: float

    :param muzzle_velocity: The muzzle velocity. By default, it equals 800 meters per second.
    :type muzzle_velocity: float

    :param gravity: The constant gravity parameter. By default, it equals 9.81 but can be changed.
    :type gravity: float

    :return: The time of bullet flight to a target in seconds
    :rtype: float
    """

    time_of_flight = round(float((distance * 2) / muzzle_velocity), 2)
    drop = round(float(0.5 * gravity * (time_of_flight ** 2)), 2)

    return f"The bullet will drop {drop} meters on the {distance}-meter distance."
