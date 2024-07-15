# Classification Model Evaluation Metrics

## Confusion Matrix Metrics

### Metrics Overview

| Metric             | Formula                                      | Description                                                                                              | Example                               |
|--------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------|
| **True Positive (TP)** | \( TP \)                                     | Number of correctly predicted positive instances.                                                         | 100 (Predicted positive and actually positive) |
| **True Negative (TN)** | \( TN \)                                     | Number of correctly predicted negative instances.                                                         | 200 (Predicted negative and actually negative) |
| **False Positive (FP)**| \( FP \)                                     | Type I error: Number of incorrectly predicted positive instances (predicted positive but actually negative). | 10 (Predicted positive but actually negative) |
| **False Negative (FN)**| \( FN \)                                     | Type II error: Number of incorrectly predicted negative instances (predicted negative but actually positive). | 5 (Predicted negative but actually positive) |

### Derived Metrics

| Metric             | Formula                                      | Description                                                                                              | Example                               |
|--------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------|
| **Accuracy**       | \( \frac{TP + TN}{TP + TN + FP + FN} \)      | Overall proportion of correctly predicted instances out of total instances.                              | \( \frac{100 + 200}{100 + 200 + 10 + 5} = \frac{300}{315} \approx 0.9524 \) (or 95.24%) |
| **Precision**      | \( \frac{TP}{TP + FP} \)                     | Proportion of correctly predicted positive instances out of total predicted positive instances.          | \( \frac{100}{100 + 10} = \frac{100}{110} \approx 0.9091 \) (or 90.91%) |
| **Recall (Sensitivity)** | \( \frac{TP}{TP + FN} \)                  | Proportion of correctly predicted positive instances out of total actual positive instances.             | \( \frac{100}{100 + 5} = \frac{100}{105} \approx 0.9524 \) (or 95.24%) |
| **Specificity (True Negative Rate)** | \( \frac{TN}{TN + FP} \)              | Proportion of correctly predicted negative instances out of total actual negative instances.             | \( \frac{200}{200 + 10} = \frac{200}{210} \approx 0.9524 \) (or 95.24%) |
| **F1-Score**       | \( 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \) | Harmonic mean of precision and recall, balancing both metrics.                                           | \( 2 \times \frac{0.9091 \times 0.9524}{0.9091 + 0.9524} \approx 0.9305 \) (or 93.05%) |

## Example Calculation

Suppose you have a binary classification model with the following outcomes based on 315 instances:

- TP (True Positives): 100
- TN (True Negatives): 200
- FP (False Positives): 10
- FN (False Negatives): 5

Using these numbers:

- **Accuracy:** \( \frac{300}{315} \approx 0.9524 \) (or 95.24%)
- **Precision:** \( \frac{100}{110} \approx 0.9091 \) (or 90.91%)
- **Recall (Sensitivity):** \( \frac{100}{105} \approx 0.9524 \) (or 95.24%)
- **Specificity (True Negative Rate):** \( \frac{200}{210} \approx 0.9524 \) (or 95.24%)
- **F1-Score:** \( 2 \times \frac{0.9091 \times 0.9524}{0.9091 + 0.9524} \approx 0.9305 \) (or 93.05%)

These metrics provide a comprehensive view of how well the classification model is performing, especially in terms of correctly identifying positive and negative instances, and are essential for evaluating and fine-tuning the model's performance.
