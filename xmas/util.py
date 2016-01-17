def normalize(values, gammas):
    """Adjust a list of brightness values according to a list of gamma values.

    Given a list of light brightness values from 0.0 to 1.0, adjust the value
    according to the corresponding maximum brightness in the gamma list. For
    example::

        >>> gammas = [0.3, 1.0]
        >>> values = [1.0, 1.0]
        >>> normalize(values, gammas)
        [0.3, 1.0]

        >>> values = [0.5, 0.5]
        >>> normalize(values, gammas)
        [0.15, 0.5]

        >>> values = [0.1, 0.0]
        >>> normalize(values, gammas)
        [0.03, 0.0]

    """

    return [value * gamma for value, gamma in zip(values, gammas)]
