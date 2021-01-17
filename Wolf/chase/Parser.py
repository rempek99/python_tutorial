import argparse
import configparser
import logging


def init_parser():
    parser = argparse.ArgumentParser(description="Wolf hunting simulation")
    parser.add_argument('-c', '--config', type=str, help='Config file path', metavar='FILE')
    parser.add_argument('-d', '--dir', type=str, help='Output files subdirectory', metavar='DIR')
    parser.add_argument('-l', '--log', type=str, choices=["DEBUG", 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Save events to journalist', metavar='LEVEL')
    parser.add_argument('-r', '--rounds', type=int, help='Number of rounds (50 if not given)')
    parser.add_argument('-s', '--sheep', type=int, help='Number of sheeps (15 if not given)')
    parser.add_argument('-w', '--wait', help='Waits for input in each round', action="store_true")
    return parser


def init_config(config_file_name):
    logging.debug('init_config(config_file_name=' + config_file_name + ')')
    config = configparser.ConfigParser()
    config.read(config_file_name)
    logging.debug('returns' + str(config))
    return config
