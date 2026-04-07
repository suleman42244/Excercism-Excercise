"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # minutes per layer


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on number of layers.
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - preparation time (in minutes).
    """
    return number_of_layers * PREPARATION_TIME


def bake_time_remaining(time_in_oven):
    """Calculate the bake time remaining.
    
    :param time_in_oven: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - time_in_oven


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes).
    """
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time


# Test calls
preparation_time_in_minutes(4)
bake_time_remaining(15)
elapsed_time_in_minutes(3, 20)