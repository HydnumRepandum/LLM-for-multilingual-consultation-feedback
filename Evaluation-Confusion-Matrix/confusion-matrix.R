library(caret)
library(knitr)
library(kableExtra)

M <- matrix(
  c(2, 22, 0,
    0, 1, 1,
    0, 0, 13),
  nrow = 3, byrow = TRUE,
  dimnames = list(
    Reference  = c("Negatif","Neutral","Positif"),
    Prediction = c("Negatif","Neutral","Positif")
  )
)

cm <- confusionMatrix(M, mode = "prec_recall")

accuracy             <- cm$overall["Accuracy"]
precision_by_class   <- cm$byClass[ , "Precision"]
recall_by_class      <- cm$byClass[ , "Recall"]
precision_macro      <- mean(precision_by_class, na.rm = TRUE)
recall_macro         <- mean(recall_by_class,    na.rm = TRUE)

print(cm)
cat("\nAccuracy         :", round(accuracy, 3), "\n")
cat("Precision (by class):\n"); print(round(precision_by_class, 3))
cat("Recall    (by class):\n"); print(round(recall_by_class,    3))
cat("\nMacro Precision :", round(precision_macro, 3), "\n")
cat("Macro Recall    :", round(recall_macro,    3), "\n")

