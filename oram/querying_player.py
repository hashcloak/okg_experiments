import os
import sys
import argparse
import oram_utils

sys.path.append("./MP-SPDZ")

parser = argparse.ArgumentParser()
parser.add_argument("predicate", type=str, help="Takes in a predicate for a (subject, predicate, object) triple")
args = parser.parse_args()

query = oram_utils.string_to_int(args.predicate)
os.system("./real-bmr-party.x -I 0 okg ")