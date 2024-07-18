# Classification Model Evaluation Metrics

## Confusion Matrix Metrics

### Metrics Overview

| Metric             | Formula                                      | Description                                                                                              | Example                               |
|--------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------|
| **True Positive (TP)** | $TP$                                     | Number of correctly predicted positive instances.                                                         | 100 (Predicted positive and actually positive) |
| **True Negative (TN)** | $TN$                                     | Number of correctly predicted negative instances.                                                         | 200 (Predicted negative and actually negative) |
| **False Positive (FP)**| $FP$                                     | Type I error: Number of incorrectly predicted positive instances (predicted positive but actually negative). | 10 (Predicted positive but actually negative) |
| **False Negative (FN)**| $FN$                                     | Type II error: Number of incorrectly predicted negative instances (predicted negative but actually positive). | 5 (Predicted negative but actually positive) |

### Derived Metrics

| Metric             | Formula                                      | Description                                                                                              | Example                               |
|--------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------|
| **Accuracy**       | $\frac{TP + TN}{TP + TN + FP + FN}$      | Overall proportion of correctly predicted instances out of total instances.                              | $\frac{100 + 200}{100 + 200 + 10 + 5} = \frac{300}{315} \approx 0.9524$ (or 95.24%) |
| **Precision**      | $\frac{TP}{TP + FP}$                     | Proportion of correctly predicted positive instances out of total predicted positive instances.          | $\frac{100}{100 + 10} = \frac{100}{110} \approx 0.9091$ (or 90.91%) |
| **Recall (Sensitivity)** | $\frac{TP}{TP + FN}$                  | Proportion of correctly predicted positive instances out of total actual positive instances.             | $\frac{100}{100 + 5} = \frac{100}{105} \approx 0.9524$ (or 95.24%) |
| **Specificity (True Negative Rate)** | $\frac{TN}{TN + FP}$              | Proportion of correctly predicted negative instances out of total actual negative instances.             | $\frac{200}{200 + 10} = \frac{200}{210} \approx 0.9524$ (or 95.24%) |
| **F1-Score**       | $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$ | Harmonic mean of precision and recall, balancing both metrics.                                           | $2 \times \frac{0.9091 \times 0.9524}{0.9091 + 0.9524} \approx 0.9305$ (or 93.05%) |

## Example Calculation for Derived Metrics

Suppose you have a binary classification model with the following outcomes based on 315 instances:

- TP (True Positives): 100
- TN (True Negatives): 200
- FP (False Positives): 10
- FN (False Negatives): 5

Using these numbers:

- **Accuracy:** $\frac{300}{315} \approx 0.9524$ (or 95.24%)
- **Precision:** $\frac{100}{110} \approx 0.9091$ (or 90.91%)
- **Recall (Sensitivity):** $\frac{100}{105} \approx 0.9524$ (or 95.24%)
- **Specificity (True Negative Rate):** $\frac{200}{210} \approx 0.9524$ (or 95.24%)
- **F1-Score:** $2 \times \frac{0.9091 \times 0.9524}{0.9091 + 0.9524} \approx 0.9305$ (or 93.05%)

## ROC and AUC Metrics

### Metrics Overview

- **ROC Curve:** A Receiver Operating Characteristic (ROC) curve is a graphical representation of a classifier's performance across all classification thresholds. It plots the True Positive Rate (TPR) against the False Positive Rate (FPR).

- **AUC (Area Under the ROC Curve):** The AUC measures the entire two-dimensional area underneath the entire ROC curve. It provides an aggregate measure of performance across all possible classification thresholds.

### Formulas

- **True Positive Rate (TPR) / Recall / Sensitivity:**
  $\[
  TPR = \frac{TP}{TP + FN}
  \]$

- **False Positive Rate (FPR):**
  $\[
  FPR = \frac{FP}{FP + TN}
  \]$

### Example Calculation

Using the same binary classification model with the following outcomes based on 315 instances:

- TP (True Positives): 100
- TN (True Negatives): 200
- FP (False Positives): 10
- FN (False Negatives): 5

Using these numbers:

- **True Positive Rate (TPR):** $\frac{100}{100 + 5} \approx 0.9524$ (or 95.24%)
- **False Positive Rate (FPR):** $\frac{10}{10 + 200} \approx 0.0476$ (or 4.76%)

The ROC curve would plot TPR against FPR at various threshold settings, and the AUC would measure the overall ability of the model to discriminate between positive and negative classes.

## Comparison: Confusion Matrix vs. ROC-AUC Metrics

| Aspect                            | Confusion Matrix Metrics                         | ROC-AUC Metrics                           |
|-----------------------------------|--------------------------------------------------|-------------------------------------------|
| **Overall Correctness**           | Accuracy: Measures the overall correctness.      | AUC: Provides an aggregate measure of performance across all thresholds. |
| **Positive Prediction Quality**   | Precision: Focuses on the quality of positive predictions. | ROC Curve: Visualizes trade-offs between TPR and FPR. |
| **Positive Instance Capture**     | Recall (Sensitivity): Captures all positive instances. | AUC: Single scalar value indicating discrimination ability. |
| **Negative Prediction Quality**   | Specificity (True Negative Rate): Measures correctly identified negatives. | - |
| **Balanced Performance**          | F1-Score: Balances precision and recall.         | - |
| **Comparison of Models**          | Useful for specific error analysis.              | Ideal for comparing different models.     |
| **Cost of Errors**                | Suitable for contexts with different costs for false positives and false negatives. | - |

These metrics provide a comprehensive view of how well the classification model is performing, especially in terms of correctly identifying positive and negative instances, and are essential for evaluating and fine-tuning the model's performance.
