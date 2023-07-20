import numpy as np
import pandas as pd
#%% filt NaN
def filtnan(tabmut,filtcoef=0.05): 
    #drop les colonnes ayant plus que (coeff * nb de ligne) de nan (0 très strigent, 1 pas du tout)
    # Autrement dit, garde les colonne avec un proportion de NA inférieur à filtcoef
    filt_nan = len(tabmut)*filtcoef
    return tabmut.loc[:,(tabmut.isna().sum() <= filt_nan)] 

def impute_sample(chridseries,random_st = None):
        nullindex = chridseries.isnull()
        chridseries.loc[nullindex] = chridseries.dropna().sample(nullindex.sum(),random_state = random_st).values
        return chridseries
    
def clean_NA_duplicate_input(df_X,filtcoef=0.05):
    # print(df_X.shape)
    df_X = filtnan(df_X,filtcoef=filtcoef)
    
    # print("The raw_dataset contains {0} feature (MS) with proportion of NA > {2} over {1} features".format(N-df_X.shape[1], N,filtcoef)) #0 null values
    
    # Removing duplicates if there exist
    df_X = df_X.T.drop_duplicates(keep='first').T
    # print(df_X.shape)
    # print("The raw_dataset contains {} duplicates".format(N_dupli))

    # Extracting the features
    features = np.setdiff1d(df_X.columns, [ 'Row.names', 'Cohort'] ).tolist()
    
    X=df_X[features]
    
    X = X.apply(impute_sample,random_st=0)
    df_X = pd.merge(X,df_X[['Cohort']],left_index=True,right_index=True)
    # Iterative imputation
    ## ExtraTree

    return df_X,features
