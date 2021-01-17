import csv
import errno
import json
import logging
import os.path
import sys

import readchar as readchar
from termcolor import colored

from Entities.Animal import distance, Animal
from Entities.Sheep import Sheep
from Entities.Wolf import Wolf
from chase.Parser import init_parser, init_config


def count_living():
    logging.debug('countLiving()')
    summary = 0
    for sh in sheeps:
        if sh.lives:
            summary += 1
    logging.debug('returns ' + str(summary))
    return summary


args = init_parser().parse_args()
output_dir = './'
if args.dir:
    output_dir += args.dir + '/'

try:
    os.makedirs(output_dir)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

if args.log:
    logging.basicConfig(filename=output_dir + 'chase.log', level=args.log, filemode='w')
if args.config:
    config = init_config(args.config)
    Animal.init_pos_limit = float(config['Terrain']['InitPosLimit'])
    if Animal.init_pos_limit <= 0:
        logging.error('ValueError: Wrong Animal.init_pos_limit configuration: ' + str(Animal.init_pos_limit) +
                      ' (Should be higher than 0)')
        raise ValueError('Wrong Animal.init_pos_limit configuration: ' + str(Animal.init_pos_limit) +
                         ' (Should be higher than 0)')
    Sheep.sheep_move_dist = float(config['Movement']['SheepMoveDist'])
    if Sheep.sheep_move_dist <= 0:
        logging.error('ValueError: Wrong Sheep.sheep_move_dist configuration: ' + str(Sheep.sheep_move_dist) +
                      ' (Should be higher than 0)')
        raise ValueError('Wrong Sheep.sheep_move_dist configuration: ' + str(Sheep.sheep_move_dist) +
                         ' (Should be higher than 0)')
    Wolf.wolf_move_dist = float(config['Movement']['WolfMoveDist'])
    if Wolf.wolf_move_dist <= 0:
        logging.error('ValueError: Wrong Wolf.wolf_move_dist configuration: ' + str(Wolf.wolf_move_dist) +
                      ' (Should be higher than 0)')
        raise ValueError('Wrong Wolf.wolf_move_dist configuration: ' + str(Wolf.wolf_move_dist) +
                         ' (Should be higher than 0)')

rounds_number = 50
sheeps_Number = 15

if args.rounds or args.rounds == 0:
    if args.rounds <= 0:
        logging.critical("Round number: " + str(args.rounds))
        raise ValueError("Round number should be higher than 0")
    rounds_number = args.rounds

if args.sheep or args.sheep == 0:
    if args.sheep <= 0:
        logging.critical("Sheep number: " + str(args.sheep))
        raise ValueError("Sheep number should be higher than 0")
    sheeps_Number = args.sheep

sheeps = list()
for x in range(1, sheeps_Number + 1):
    sheepName = 'Sheep {}'.format(str(x))
    sheeps.append(Sheep(name=sheepName))

wolf = Wolf()

data = {'rounds': []}
csv_data = list()

for round_no in range(1, rounds_number + 1):
    if count_living() == 0:
        logging.warning("All sheeps have beed killed")
        break
    print("ROUND " + str(round_no))
    for sh in sheeps:
        if sh.lives:
            sh.move()
    closestSheep = None
    minDistance = sys.float_info.max
    for sh in sheeps:
        if sh.lives and (distance(sh.x, wolf.x, sh.y, wolf.y) < minDistance):
            minDistance = distance(sh.x, wolf.x, sh.y, wolf.y)
            closestSheep = sh

    if wolf.move(closestSheep.x, closestSheep.y):
        closestSheep.lives = False
        logging.info(str(closestSheep) + ' has been killed')
        print(colored(str(closestSheep) + " KILLED", 'red'))
    print(str(wolf))
    print("Living sheeps: " + str(count_living()))
    print("\n--------------------------------------")
    sheepsInfo = []

    for sh in sheeps:
        if sh.lives:
            sheepsInfo.append(sh.position())
        else:
            sheepsInfo.append(tuple({None, None}))

    data['rounds'].append({
        'round_no': str(round_no),
        'wolf_pos': wolf.position(),
        'sheep_pos': sheepsInfo
    })
    csv_data.append([str(round_no), str(count_living())])
    if args.wait:
        print("Press any key")
        print("--------------------------------------\n")
        readchar.readchar()

with open(output_dir + 'pos.json', 'w') as file:
    file.write(json.dumps(data, indent=4))

with open(output_dir + 'alive.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in csv_data:
        writer.writerow(row)
