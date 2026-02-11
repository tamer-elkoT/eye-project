import splitfolders

splitfolders.ratio(
    "data/Eye dataset",                   # input folder
    output="data_split",     # output folder
    seed=41,                # same split every time
    ratio=(0.7, 0.15, 0.15) # train, val, test
)