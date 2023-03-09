test = {
    'name': 'checkpoint-1',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems CC1TheSame is undefined. Have you defined it correctly?
                    >>> # I.e. CC1TheSame = ...
                    >>> 'CC1TheSame' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your value for CC1TheSame is incorrect.
                    >>> # Remember that CC1TheSame is a boolean.
                    >>> CC1TheSame == True
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
