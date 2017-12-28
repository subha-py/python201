from collections import ChainMap
import argparse
import os


def mix_args():
    app_defaults = dict(username='admin', password='admin')
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    arguments = {key: value for key, value in vars(parser.parse_args()).items() if value}

    chain = ChainMap(arguments, os.environ, app_defaults)
    print(chain['username'])


if __name__ == '__main__':
    mix_args()
    os.environ['username'] = 'test'
    mix_args()
