import copy
import numpy as np
import movingfp.gen as mfp
from gens_for_paper import get_seed

# To get the max_path in start_recursion
D_path = {}
D_path_n = {}
for i in range(10):
    D_path[i] = []
    D_path_n[i] = []


def start_recursion(n, p, dim, num_fires, fighter_pos, lambda_d, instance, instances=None, node_list=None):
    global D_path, D_path_n
    ss = get_seed(nodes=n,
                  instance=instance,
                  instances=instances,
                  node_list=node_list
                  )
    generator = np.random.default_rng(ss)

    graph = mfp.erdos_connected(n, p, dim, fighter_pos, num_fires, generator)
    burned = set(graph.burnt_nodes)

    # Quit all burnt nodes
    all_nodes = [node for node in range(n + 1) if node not in burned]

    # also quit the anchor point n
    # Note that if anchor n is in the best path = [n, a, b, ...] the length of the path will be
    # smaller by removing n, path' = [a, b, ...], and the nodes to generate D will be the same.
    all_nodes.remove(n)

    graph.D = graph.D * lambda_d

    # Considering all paths that don't contain the anchor point
    D_small = recursion_D(graph.D, all_nodes, length_path=0, path=None, available_nodes=None)
    # Considering all paths starting with "a"
    D_small_n = recursion_D_fixing_n(graph.D, all_nodes, n, length_path=0, path=None, available_nodes=None)
    # If the path start with the anchor point, we must subtract one unit from the result
    D_small_n = D_small_n - 1

    D = max(D_small, D_small_n)
    if D == D_small:
        max_path = D_path[D_small][0]
    else:
        max_path = D_path_n[D_small_n][0]

    return D, max_path


def recursion_D(distance, all_nodes, length_path=0, path=None, available_nodes=None):
    global D_path

    if path is None:
        path = []

    if available_nodes is None:
        available_nodes = [node for node in all_nodes if node not in path]

    # base case
    if length_path > 1:
        # We have added a one node more
        D = len(path) - 1
        return D
    if len(available_nodes) == 0:
        D = len(path)
        D_path[D].append(path)
        return D

    if len(available_nodes) > 0:
        node = available_nodes[0]

        new_path = copy.deepcopy(path)
        new_path.append(node)
        new_available_nodes = copy.deepcopy(available_nodes)
        new_available_nodes.remove(node)

        new_length_path = copy.deepcopy(length_path)
        if len(new_path) > 1:
            new_length_path += distance[new_path[-1], new_path[-2]]

        return max(recursion_D(distance, all_nodes, length_path, path, new_available_nodes),
                   recursion_D(distance, all_nodes, new_length_path, new_path, available_nodes=None))

    else:
        # This D is the D in the previous level.
        D = len(path)
        D_path[D].append(path)
        return D


def recursion_D_fixing_n(distance, all_nodes, n, length_path=0, path=None, available_nodes=None):
    global D_path_n

    if path is None:
        # We force the anchor point "n" is always at the beginning of the path
        path = [n]

    if available_nodes is None:
        available_nodes = [node for node in all_nodes if node not in path]

    # base case
    if length_path > 1:
        # We have added a one node more
        D = len(path) - 1
        return D

    if len(available_nodes) == 0:
        D = len(path)
        D_path_n[D].append(path)
        return D

    if len(available_nodes) > 0:
        node = available_nodes[0]

        new_path = copy.deepcopy(path)
        new_path.append(node)
        new_available_nodes = copy.deepcopy(available_nodes)
        new_available_nodes.remove(node)

        new_length_path = copy.deepcopy(length_path)
        if len(new_path) > 1:
            new_length_path += distance[new_path[-1], new_path[-2]]

        return max(recursion_D_fixing_n(distance, all_nodes, n, length_path, path, new_available_nodes),
                   recursion_D_fixing_n(distance, all_nodes, n, new_length_path, new_path, available_nodes=None))

    else:
        # This D is the D in the previous level.
        D = len(path)
        D_path_n[D].append(path)
        return D
