from recursive_function import find_B_suf
from get_D_value import start_recursion


instances = 10 # num. of total instances with the same global seed
n_list = [10, 20, 30, 40]
p_list = None  # ex. prob of each edge = 0.5
pn_list = [2.5]  # ex.: prob of each edge = 2.5/n
d_list = [2, 7] # the lambda value to be multiplied by the distance matrix
B_base = 1 # The recursion starts from this value of B until solve the instance
dim_list = [3]  # dimensions
bn_list = [1, 3]  # num init fires

fighter_pos = None
threshold_time = None
FIREFIGHTERS = 1 # Num. of total firefighters. Must be 1 as default.


proportional = False
if pn_list is not None:
    proportional = True

count = 0
for n in n_list:
    if proportional:
        p_list = []
        for p in pn_list:
            p_list.append(p / n)

    for burnt_nodes in bn_list:
        if threshold_time is None:
            json_name = f'D2_verify_{n}_{burnt_nodes}_2.json'
            cvs_name = f"D2_verify_{n}_{burnt_nodes}_2.csv"
        else:
            json_name = f'instances{instances}_{n}_{burnt_nodes}_{threshold_time}.json'
            cvs_name = f"instances{instances}_{n}_{burnt_nodes}_{threshold_time}.csv"

        binary_dic = {}
        for i in range(instances):
            binary_dic[i] = []

        for instance in range(instances):
            for p in p_list:
                for dim in dim_list:
                    for lambda_d in d_list:
                        D, _ = start_recursion(n,
                                               p,
                                               dim,
                                               burnt_nodes,
                                               fighter_pos,
                                               lambda_d,
                                               instance,
                                               instances=instances,
                                               node_list=n_list)

                        print("n=", n, "p=", p, "dim=", dim, "burnt_nodes=", burnt_nodes,
                              "instance", instance, "lambda", lambda_d, "D", D)

                        # We solve finding the minimum B for which the process finishes
                        find_B_suf(instance, n, p, dim, burnt_nodes, lambda_d, threshold_time, binary_dic,
                                   json_name, cvs_name, B_base, D, node_list=n_list, instances=instances)


