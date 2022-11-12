import utils

files = ['./Runs/csv_s/verify_10_1.csv',
         './Runs/csv_s/verify_10_3.csv',
         './Runs/csv_s/verify_20_1.csv',
         './Runs/csv_s/verify_20_3.csv',
         './Runs/csv_s/verify_30_1.csv',
         './Runs/csv_s/verify_30_3.csv',
         './Runs/csv_s/verify_40_1.csv',
         './Runs/csv_s/verify_40_3.csv',
         ]

utils.plot_results(files, val_lambdas=[7, 2])