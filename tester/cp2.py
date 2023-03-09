test = {
    'name': 'checkpoint-2',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems YT is undefined. Have you defined it correctly?
                    >>> # I.e. YT = ...
                    >>> 'YT' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # The dimensions of YT are not correct.
                    >>> # Remember that dimensions of YT are the same as those of XT.
                    >>> YT.shape == XT.shape
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
