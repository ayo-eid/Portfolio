# Detection of Epileptic Seizures using Machine Learning Methods

Epileptic seizures occur as a result of brain functional dysfunction and can affect the health of the patient. Prediction of epileptic seizures before the onset is very useful for the prevention of seizures through medication. Electroencephalograms (EEG) signals are used to detect & predict epileptic seizures using machine learning techniques and feature extractions. Nevertheless, the pre-processing of EEG signals for noise removal and extraction of features are two major problems which have an adverse effect on both anticipation time and true positive prediction performance. Taking this into consideration, the proposed model will provide remarkable methods for both preprocessing and extraction of features. The model detects various brain states and accounts for both epileptic seizures detection and prediction. Using the EEG CHB-MIT dataset, the SVM model was trained, tested and compared, having a best true positive percentage of 0.91 for a single patient and 0.82 for multiple patients. The SVM algorithm was also compared to other machine learning ones, with its results being better than all used in comparison.

# Seizure Detection Procedure

    1. Combine all EEG signal channels using Averaging
    2 Filter using bass band filters for increasing SNR
    3. Feature extraction
    4. Normalization
    5. Balancing the Prevalence rate
    6. SVM Vs. KNN for classification
    7. Testing & validation using K-fold

Dataset Available at https://physionet.org/content/chbmit/1.0.0/
