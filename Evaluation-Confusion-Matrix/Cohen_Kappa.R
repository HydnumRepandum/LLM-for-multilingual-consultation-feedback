library(DescTools)
library(dplyr)


#R script to calculate Cohen's Kappa with pairwise complete observations
#Rater1 -> L
#Rater2 -> E
df_interest_Gemma<- data.frame(
  Rater1 = c("1", "3", "0", "3", "0", "1", "1", "3", "2", "1", "3", "1", "0", "3", "0", "0", "0", "3", "0", "1", "3", "3", "1", "1", "3", "3", "3", "3", "3", "0", "0", "3", "3"),
  Rater2 = c("3", "3", "3", "3", "0", "1", "1", "3", "2", "1", "3", "1", "1", "0", "0", "3", "1", "3", "0", "1", "3", "0", "1", "3", "1", "3", "0", "1", "1", "0", "0", "1", "3")
)

df_impresctibility_Gemma<- data.frame(
  Rater1 = c("1", "1","1", "3", "0", "0", "0", "3"),
  Rater2 = c("1", "1","1", "3", "0", "0", "0", "3")
)

df_douane_Gemma<- data.frame(
  Rater1 = c("3", "1", "1", "1", "1", "3", "1", "1", "1", "1", "1", "1", "1", "0", "3", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "0", "0", "1", "1", "3", "0", "0", "3", "3", "1", "1", "3", "1", "0", "1", "1", "1", "1"),
  Rater2 = c("3", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "3", "1", "1", "0", "1", "3", "1", "3", "0", "0", "0", "0", "0", "1", "1", "3", "0", "0", "3", "1", "1", "1", "3", "1", "1", "1", "1", "1", "1")
)


#############

df_interest_GPT<- data.frame(
  Rater1 = c("1", "3", "3", "3","0", "1", "1", "1", "3", "1", "1", "1", "1", "3", "3", "1","1", "1", "1","1", "3", "3", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1","3"),
  Rater2 = c("1", "3", "3", "1","0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "3", "1", "1","1", "1", "1", "3", "3", "1", "1", "3", "1", "1", "1", "1", "3", "1", "1","1")
)

df_impresctibility_GPT<- data.frame(
  Rater1 = c("1","1", "1", "1", "0", "1", "1"),
  Rater2 = c("1","1", "1", "1", "3", "1", "3")
)

df_douane_GPT<- data.frame(
  Rater1 = c("1", "3", "1", "1", "0", "1", "1", "1", "1", "3", "1", "1", "1", "1", "1", "1", "1", "3", "1", "1","1", "1", "3", "1", "0", "1", "1", "1", "0", "0","0", "0", "1", "1", "3", "1", "1", "1", "1", "1", "1", "3", "1", "1", "1", "1", "3", "1"),
  Rater2 = c("1", "3", "1", "1", "3", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "3", "1", "1","1", "1", "3", "1", "3", "1", "1", "1", "0", "3","0", "0", "1", "1", "3", "1", "1", "1", "1", "1", "1", "3", "1", "1", "1", "1", "1", "1")
)

############
# View the data frame
print(df_interest_Gemma)
print(df_impresctibility_Gemma)
print(df_douane_Gemma)


###############
k_interest_Gemma <- PairApply(df_interest_Gemma, FUN=CohenKappa, symmetric=TRUE)
k_impress_Gemma  <- PairApply(df_impresctibility_Gemma, FUN=CohenKappa, symmetric=TRUE)
k_douane_Gemma   <- PairApply(df_douane_Gemma, FUN=CohenKappa, symmetric=TRUE)
##############
k_interest_GPT <- PairApply(df_interest_GPT, FUN=CohenKappa, symmetric=TRUE)
k_impress_GPT  <- PairApply(df_impresctibility_GPT, FUN=CohenKappa, symmetric=TRUE)
k_douane_GPT   <- PairApply(df_douane_GPT, FUN=CohenKappa, symmetric=TRUE)
##############
# Print the results
print(k_interest_Gemma)
print(k_impress_Gemma)
print(k_douane_Gemma)
print(k_interest_GPT)
print(k_impress_GPT)
print(k_douane_GPT)
##############
extract_kappa <- function(kmat) {
  round(kmat[1, 2], 3)
}
kappa_results <- data.frame(
  Category = c("Interest", "Impressctibility", "Douane"),
  Gemma_Kappa = c(extract_kappa(k_interest_Gemma),
                  extract_kappa(k_impress_Gemma),
                  extract_kappa(k_douane_Gemma)),
  GPT_Kappa = c(extract_kappa(k_interest_GPT),
                extract_kappa(k_impress_GPT),
                extract_kappa(k_douane_GPT))
)
print(kappa_results)



