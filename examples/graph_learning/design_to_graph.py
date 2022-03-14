import ast
import csv
import numpy as np

from Preprocessor import Preprocessor
import pyrobotdesign as rd
from design_search import build_normalized_robot, make_initial_graph
from load_log_file import load_terminal_design_data, load_partial_design_data

import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--task_name", type=str)
    parser.add_argument("--grammar_file", type=str, help="Grammar file (.dot)")
    parser.add_argument("--input_sequence_file", type=str,
                      help="File to save input sequence to (.csv)")
    parser.add_argument("--save_npz_dir", type=str,
                      help="Directory to save .npz files to")
    args = parser.parse_args()

    # for the link features matrix, each row (link) contains
    # [one hot of link type
    #  joint pos
    #  joint quaternion for rotation
    #  joint axis
    #  one hot of link shape
    #  length
    #  radius
    #  density
    #  friction
    #  joint_kp
    #  joint_kd
    #  joint_torque
    #  one hot of control mode
    #  ]
    all_link_features_pad, all_adj_matrix_pad, all_masks, all_results = load_terminal_design_data(args.input_sequence_file, args.grammar_file)

    np.savez_compressed(os.path.join(args.save_npz_dir, args.task_name), link_features=np.array(all_link_features_pad), adj_matrices=np.array(all_adj_matrix_pad), masks=np.array(all_masks), rewards=np.array(all_results), task=np.array([args.task_name]))