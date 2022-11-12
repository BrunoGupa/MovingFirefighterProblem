import movingfp.gen as mfp
import json
from miqcp import mfp_constraints
from verify_function import verify
from convert_to_cvs import json_to_csv
from gens_for_paper import get_seed
import numpy as np

FIREFIGHTERS = 1


def find_B_suf(instance, n, p, dim, burnt_nodes, lambda_d, time, binary_dic, json_name_bin, cvs_name_bin,
               B, D, node_list=None, instances=None):
    # We start with B = 1

    print(
        f"-------Solving  for B = {B},  n = {n}, burnt = {burnt_nodes}, instance = {instance}, lambda = {lambda_d},  "
        f"D = {D} -------------------------------------------")

    objective, is_upper_bound, not_interrupted = run_and_save(instance, n, p, dim, burnt_nodes, lambda_d, D, B,
                                                              time,
                                                              binary_dic, json_name_bin, cvs_name_bin,
                                                              node_list=node_list, instances=instances)

    if not_interrupted:
        if not is_upper_bound:
            B += 1
            find_B_suf(instance, n, p, dim, burnt_nodes, lambda_d, time, binary_dic,
                       json_name_bin, cvs_name_bin, B, D, node_list=node_list, instances=instances)


def run_and_save(instance, n, p, dim, burnt_nodes, lambda_d, D, T, time, binary_dic, json_name_bin, cvs_name_bin,
                 D_max=None, node_list=None, instances=None):
    global FIREFIGHTERS, is_upper_bound

    ss = get_seed(nodes=n,
                  instance=instance,
                  instances=instances,
                  node_list=node_list
                  )
    generator = np.random.default_rng(ss)

    x = mfp.erdos_connected(n, p, dim, None, burnt_nodes, generator)
    # mfp.plot3d(x, plot_grid=True, plot_labels=True)

    x.D = x.D * lambda_d

    print("n=", n)
    print("T=", T)
    print("D=", D)
    print("p=", p)
    print("instance=", instance)
    print("lambda_d=", lambda_d)

    infeasible, runtime, not_interrupted, objective, defended_seq, distances = \
        mfp_constraints(D, T, n, x, time, FIREFIGHTERS)

    # Verify that the process finishes with that value of B
    _, burnt, B_veri = verify(n, instance, lambda_d, burnt_nodes, dim, defended_seq,
                               node_list=node_list, instances=instances)

    if objective == burnt:
        # L is an upper bound
        is_upper_bound = True
    else:
        # The process don't end and L is an lower bound
        is_upper_bound = False

    if D_max is None:
        D_max = D

    binary_dic[instance].append([[n, p, dim, burnt_nodes, instance, lambda_d],
                                 [D, T, infeasible, runtime, not_interrupted, objective, defended_seq,
                                  distances],
                                 [is_upper_bound, D_max]])

    # Saving data
    with open(f"./Runs/jsons/{json_name_bin}", "w") as binary:
        json.dump(binary_dic, binary)
    json_to_csv(f"./Runs/jsons/{json_name_bin}", f"./Runs/csv_s/{cvs_name_bin}")

    return objective, is_upper_bound, not_interrupted
