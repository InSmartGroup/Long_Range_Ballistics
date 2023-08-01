def mrad_to_moa(mrad):
    return f"{mrad} MRAD = {round(mrad * 3.4377492368197, 2)} MOA"


def moa_to_mrad(moa):
    return f"{moa} MOA = {round(moa * 0.290888, 2)} MRAD"


def calculate_distance_to_target(target_height_in_cm, focal_height, mrad_moa=None):
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
    normal_10_meters_hit = 4.5  # at 10 meters, the bullet hits the target lower than the center

    vertical_hit = float(vertical[:-1])
    vertical_direction = vertical[-1]
    horizontal_hit = float(horizontal[:-1])
    horizontal_direction = horizontal[-1]

    vertical_adjustment_direction = 'UP' if vertical_direction == 'd' or vertical_direction == 'D' else 'DOWN'
    horizontal_adjustment_direction = 'RIGHT' if horizontal_direction == 'l' or horizontal_direction == 'L' else 'LEFT'

    one_mrad_to_distance = 1  # centimeters

    vertical_adjustment_in_mrad = round(vertical_hit / one_mrad_to_distance - normal_10_meters_hit, 2)
    horizontal_adjustment_in_mrad = round(horizontal_hit / one_mrad_to_distance, 2)

    report = f"Adjust the scope {vertical_adjustment_in_mrad} MRAD {vertical_adjustment_direction} " \
             f"and {horizontal_adjustment_in_mrad} MRAD {horizontal_adjustment_direction}\n" \
             f"Make {int(vertical_adjustment_in_mrad * 10)} clicks {vertical_adjustment_direction}\n" \
             f"Make {int(horizontal_adjustment_in_mrad * 10)} clicks to the {horizontal_adjustment_direction}\n"

    return report


def adjustments_mrad(distance, vertical=str(0), horizontal=str(0)):
    """
    Do the first shot at 100 meters and enter the result to calculate vertical and horizontal adjustments to the scope.

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
    vertical_hit = float(vertical[:-1])
    vertical_direction = vertical[-1]
    horizontal_hit = float(horizontal[:-1])
    horizontal_direction = horizontal[-1]

    vertical_adjustment_direction = 'UP' if vertical_direction == 'd' or vertical_direction == 'D' else 'DOWN'
    horizontal_adjustment_direction = 'RIGHT' if horizontal_direction == 'l' or horizontal_direction == 'L' else 'LEFT'

    one_mrad_in_cm_to_distance = round(distance / 10, 2)  # centimeters

    vertical_adjustment_in_mrad = round(vertical_hit / one_mrad_in_cm_to_distance, 2)
    horizontal_adjustment_in_mrad = round(horizontal_hit / one_mrad_in_cm_to_distance, 2)

    report = f"To hit the target at {distance} meters, " \
             f"adjust the scope {vertical_adjustment_in_mrad} MRAD {vertical_adjustment_direction} " \
             f"and {horizontal_adjustment_in_mrad} MRAD {horizontal_adjustment_direction}\n" \
             f"Make {int(vertical_adjustment_in_mrad * 10)} clicks {vertical_adjustment_direction}\n" \
             f"Make {int(horizontal_adjustment_in_mrad * 10)} clicks to the {horizontal_adjustment_direction}\n"

    return report


# print(zeroing_mrad_10_meters('8D', '3L'))
# print(adjustments_mrad(124, '10u', '7r'))

# print(adjustments_mrad(100, '13U', '7l'))
# print(adjustments_mrad(278, '21d', '53R'))