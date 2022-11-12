import json
import pandas as pd


def json_to_csv(json_name, cvs_name):
    with open(json_name, 'r') as a_file:
        moving = a_file.read()
        moving = json.loads(moving)


    num_nodes = []
    p = []
    dim = []
    burnt_nodes = []
    instance = []
    lambda_d = []

    D = []
    T = []
    infeasible = []
    runtime = []
    not_interrupted = []
    objective = []
    defended_seq = []
    distances = []

    algorithm = []

    is_upper_bound = []
    D_max = []
    total_nodes = []
    interpoints = []

    for key in moving.keys():
        for n in range(len(moving[key])):
            algorithm.append("moving")

            x = moving[key][n][0][0]
            num_nodes.append(x)

            x = moving[key][n][0][1]
            p.append(x)

            x = moving[key][n][0][2]
            dim.append(x)

            x = moving[key][n][0][3]
            burnt_nodes.append(x)

            x = moving[key][n][0][4]
            instance.append(x)

            x = moving[key][n][0][5]
            lambda_d.append(x)

            x = moving[key][n][1][0]
            D.append(x)

            x = moving[key][n][1][1]
            T.append(x)

            x = moving[key][n][1][2]
            infeasible.append(x)

            x = moving[key][n][1][3]
            runtime.append(x)

            x = moving[key][n][1][4]
            not_interrupted.append(x)

            x = moving[key][n][1][5]
            objective.append(x)

            x = moving[key][n][1][6]
            defended_seq.append(x)

            x = moving[key][n][1][7]
            distances.append(x)

            x = moving[key][n][2][0]
            is_upper_bound.append(x)

            x = moving[key][n][2][1]
            D_max.append(x)


    results = {}

    results["num_nodes"] = num_nodes
    results["p"] = p
    results["dim"] = dim
    results["burnt_nodes"] = burnt_nodes
    results["instance"] = instance
    results["lambda_d"] = lambda_d

    results["D"] = D
    results["T"] = T

    results["algorithm"] = algorithm

    results["infeasible"] = infeasible
    results["runtime"] = runtime
    results["not_interrupted"] = not_interrupted
    results["objective"] = objective
    results["is_upper_bound"] = is_upper_bound
    results["D_max"] = D_max
    results["defended_seq"] = defended_seq
    results["distances"] = distances


    df = pd.DataFrame(results)
    df.to_csv(cvs_name)
