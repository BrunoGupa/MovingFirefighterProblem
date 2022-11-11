import numpy as np


# Create seed sequence for paper experiments
def get_seed(nodes, instance, instances=None, node_list=None):
    global_seed = 6845406670007309403110730420044295152

    if node_list is None:
        node_list = [10, 20, 30, 40]

    if instances is None:
        instances = 10

    ss_global = np.random.SeedSequence(global_seed)

    # Spawn off 4 child SeedSequences (for 10, 20, 30 and 40 nodes)
    ss_child = ss_global.spawn(len(node_list))

    # Spawn off 10 grandchildren SeedSequences to pass to each generator.
    node_idx = node_list.index(nodes)
    ss_instances = ss_child[node_idx].spawn(instances)

    ss = ss_instances[instance]
    return ss
