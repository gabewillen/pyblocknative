
networks = dict(bitcoin={'1': 'main', '2': 'testnet'},
                ethereum={
                    '1': 'main',
                    '3': 'ropsten',
                    '4': 'rinkeby',
                    '5': 'goerli',
                    '42': 'kovan',
                    '56': 'bsc-main',
                    '100': 'xdai',
                    '137': 'matic-main'
                })

DEFAULT_RATE_LIMIT_RULES = dict(points=150, duration=1)
QUEUE_LIMIT = 10000