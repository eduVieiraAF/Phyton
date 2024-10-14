
#* help() function shows the documentation of a function

# help(print)

# write a function to calculate area of a circle

def area(r):
    """
    Calculates the area of a circle given its radius.

    Parameters
    ----------
    r : float
        The radius of the circle

    Returns
    -------
    float
        The area of the circle
    """
    area = 3.14 * r * r
    return area

help(area)