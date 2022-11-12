import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_results(file_list, val_dim=3, val_lambdas=[7, 5, 3, 2, 1]):
    sns.set(font_scale=1, rc={'text.usetex': True})
    sns.set_theme(style='whitegrid')
    #sns.set_style(style='ticks')


    """
    Read CSV files and get a pandas dataframe for sufficient T.
    """
    dfs_global = []
    for file in file_list:
        df = pd.read_csv(file)
        #print(df)
        dfs_partial = []
        #seeds = df.seed.unique()
        for instance in range(10):
            # 1. Seeds
            df_seed = df[df['instance'] == instance]

            # 2. Dimensions
            df_dim = df_seed[df_seed['dim'] == val_dim]
        
            # 3. Lambdas
            lambdas = df_dim.lambda_d.unique()
            if set(lambdas) != set(val_lambdas):
                print(f'\tCaution: In {file}, instance: {instance}, there are these lambdas: {lambdas}')

            for lamb in lambdas:
                df_lambda = df_dim[df_dim['lambda_d'] == lamb]
  
                # 4. Optimal solutions
                df_optimal = df_lambda[df_lambda['is_upper_bound'] == True]
                #print(df_optimal)
                if df_optimal.size == 0:
                    print(f'\tCaution: In {file}, seed: {instance}, lambda: {lamb} there are not optimal solutions, i.e.: is_upper_bound is always False.')

                # 5. T sufficient
                t_sufficient = df_optimal['T'].min()
                df_sufficient = df_optimal[df_optimal['T'] == t_sufficient]

                t_sufficient = df_optimal['T']
                
                dfs_partial.append(df_sufficient)
        df_partial = pd.concat(dfs_partial, ignore_index=True)
        dfs_global.append(df_partial)
    df_global = pd.concat(dfs_global, ignore_index=True)
    df_global.rename(columns = {'num_nodes': 'Number of nodes',
                            'runtime': 'Running time (sec)',
                            'burnt_nodes': 'Initial fires',
                            'lambda_d': '$\lambda$',
                            'objective': 'Objective function (Burnt vertices)',
                            'T': 'Sufficient B',
                            'D': 'Defending Rounds D'}, inplace = True)

    #print(f'size of final dataframe: {df_global.size}')


    # Plotting num_nodes vs burnt_nodes
    ax = sns.relplot(data=df_global,
                x='Number of nodes',
                y='Objective function (Burnt vertices)',
                col='Initial fires',
                hue='$\lambda$',
                #style='lambda_d',
                palette='bright',
                kind='line',
                style="$\lambda$",
                markers={2: 'o', 7: 's'},
                dashes=False,
                ci=95);
    ax.set(xlim=(9.64, None))
    plt.xticks([10, 20, 30, 40])
    plt.savefig('img/num_nodes_vs_objective.png', dpi=300)

    # Plotting num_nodes vs running time for a sufficient T.
    ax = sns.relplot(data=df_global,
                x='Number of nodes',
                y='Running time (sec)',
                col='Initial fires',
                hue='$\lambda$',
                # style='lambda_d',
                palette='bright',
                kind='line',
                style="$\lambda$",
                markers={2: 'o', 7: 's'},
                dashes=False,
                ci=95).set(yscale="log")
    ax.set(xlim=(9.64, None))
    # specify positions of ticks on x-axis and y-axis
    plt.xticks([10, 20, 30, 40])
    plt.savefig('img/num_nodes_vs_runtime.png', dpi=300)


