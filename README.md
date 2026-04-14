# HDP (Hypertensive Disorders of Pregnancy) Risk Prediction System

A comprehensive machine learning system for predicting maternal health risks and birth weight outcomes using advanced classification models with interpretability analysis.

## Overview

This system includes:
- **Maternal Health Risk Classification**: Predicts high-risk vs. low-risk pregnancies (98.15% accuracy)
- **Birth Weight Prediction**: Classifies normal vs. low birth weight outcomes (87.50% accuracy)
- **Interpretability Analysis**: LIME and SHAP explanations for model decisions
- **Fairness Analysis**: Demographic disparities detection across age, education, and income groups
- **Real-time Dashboard**: Streamlit-based interactive prediction interface
- **Firebase Integration**: Cloud-based data persistence and patient management

## Features

### Models
- Random Forest Classifiers with balanced class weights
- Gradient Boosting for comparison
- 10-epoch training with 5-fold cross-validation
- Chi-square statistical significance testing
- ROC-AUC and Cohen's Kappa metrics

### Visualizations
- 20+ publication-quality charts (300 DPI PNG)
- Confusion matrices, ROC curves, precision-recall plots
- Feature importance rankings (both models)
- Learning curves across epochs
- Fairness disparities by demographic groups
- Error distribution and confidence analysis

### Interpretability
- **LIME**: Local explanations for individual predictions (4 HTML files)
- **SHAP**: Game-theoretic feature importance summaries
- Per-prediction breakdown of feature contributions

### Data
- `Maternal_Risk.csv`: 808 maternal health records (6 features)
- `birth_weight_dataset.csv`: 200 birth weight records (14 features)

## Installation

```bash
# Clone repository
git clone https://github.com/GraceKaimburi/HEALTH.git
cd HEALTH

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

## Deployment

### Option 1: Deploy to Vercel (Docker)
1. Update `.env` with Firebase credentials:
   ```bash
   FIREBASE_SERVICE_ACCOUNT_BASE64=<your-base64-encoded-service-account>
   ```

2. Push to GitHub and connect to Vercel:
   ```bash
   git push origin main
   ```
   Vercel will automatically detect the Dockerfile and deploy

3. Set environment variables in Vercel Project Settings

### Option 2: Deploy to Streamlit Cloud
```bash
streamlit run app.py
# Then use "Deploy" button in Streamlit Cloud
```

### Option 3: Deploy to Railway/Render
1. Connect GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `streamlit run app.py`
4. Add Firebase environment variables

## Configuration

### Firebase Setup
1. Create Firebase project at https://console.firebase.google.com
2. Download service account JSON
3. Encode to Base64:
   ```bash
   cat firebase-service-account.json | base64
   ```
4. Set as environment variable: `FIREBASE_SERVICE_ACCOUNT_BASE64`

### Streamlit Configuration
- Located in `.streamlit/config.toml`
- Customize theme colors and settings

## Models & Performance

### Maternal Health Risk Classification
- **Accuracy**: 98.15%
- **ROC-AUC**: 0.9968
- **Cohen's Kappa**: 0.9614
- **Features**: Blood sugar, systolic BP, age, etc.
- **Dataset**: 808 maternal health records
- **Top Predictor**: Blood Sugar (47.2% importance)

### Birth Weight Prediction
- **Accuracy**: 82.50% (Random Forest), 87.50% (Gradient Boosting)
- **ROC-AUC**: 0.9648
- **Cross-Validation**: 83.75% ± 1.25%
- **Features**: Hemoglobin, prenatal visits, gestational age, etc.
- **Dataset**: 200 birth weight records
- **Top Predictor**: Hemoglobin Level (16.3% importance)

## Fairness Analysis

### Demographic Disparities
- **Age Groups**: 14% variance across 18-36+ age groups
- **Education Levels**: 3-7% differences across education categories
- **Income Groups**: 3-4% differences across income levels

⚠️ **Known Bias**: Low birth weight class has 87.5% error rate (7/8 misclassified). Model performs well on normal weight (0% error).

## Directory Structure

```
HEALTH/
├── app.py                              # Main Streamlit dashboard
├── train_classification_model.py       # Maternal health classifier training
├── train_birth_weight_model.py         # Birth weight predictor training
├── Dockerfile                          # Docker configuration for Vercel
├── vercel.json                         # Vercel deployment config
├── .streamlit/config.toml             # Streamlit configuration
├── requirements.txt                    # Python dependencies
├── Maternal_Risk.csv                   # Maternal health dataset
├── birth_weight_dataset.csv            # Birth weight dataset
├── artifacts/                          # Trained model files
└── visualizations/
    ├── classification/                 # Maternal health visualizations (10)
    │   ├── 01_confusion_matrix.png
    │   ├── 02_roc_curve.png
    │   ├── ... (8 more)
    │   └── ANALYSIS_REPORT.txt
    └── birth_weight/                   # Birth weight visualizations (15+)
        ├── 01_confusion_matrix.png
        ├── 02_roc_curve.png
        ├── 04_feature_importance_rf.png
        ├── 10_fairness_disparities.png
        ├── 13_shap_summary.png
        ├── lime_explanations/          # 4 LIME HTML files
        └── ... (more visualizations)
```

## Usage

### Dashboard Features
1. **Patient Enrollment**: Add new patients with health metrics
2. **Risk Prediction**: Get high/low risk classification
3. **Time-to-Event**: Predict weeks until complications
4. **Historical Tracking**: Monitor multiple visits per patient
5. **Firebase Sync**: Auto-save to cloud database

### Model Training
```bash
# Train maternal health risk classifier
python train_classification_model.py

# Train birth weight predictor
python train_birth_weight_model.py
```

### Generating Reports
- Automatic analysis reports in `visualizations/*/ANALYSIS_REPORT.txt`
- 16+ high-resolution visualizations for publication
- LIME/SHAP explanations in HTML format

## Performance Metrics

### Classification Metrics
- **Accuracy**: Percentage of correct predictions
- **Precision**: True positives / (true positives + false positives)
- **Recall**: True positives / (true positives + false negatives)
- **F1-Score**: Harmonic mean of precision and recall
- **Cohen's Kappa**: Agreement beyond chance
- **MCC**: Balanced accuracy metric for imbalanced data
- **ROC-AUC**: Area under the receiver operating characteristic curve

### Statistical Tests
- **Chi-Square**: Tests association between predicted and actual values
- **Cross-Validation**: 5-fold stratified for stable estimates
- **Confidence Intervals**: Derived from CV standard deviations

## Troubleshooting

### Firebase Not Initializing
- Verify `FIREBASE_SERVICE_ACCOUNT_BASE64` environment variable is set
- Check Firebase service account JSON is valid
- Reload app with Ctrl+R

### Models Not Found
- Run training scripts to generate models:
  ```bash
  python train_classification_model.py
  python train_birth_weight_model.py
  ```

### Vercel Deployment Issues
- Ensure all environment variables are set
- Check Docker build logs in Vercel dashboard
- Verify Python version compatibility (3.11+)

## Environment Variables

Required for Firebase:
```
FIREBASE_SERVICE_ACCOUNT_BASE64=<base64-encoded-service-account-json>
```

Optional:
```
STREAMLIT_THEME=light  # or 'dark'
VERCEL_ENV=production
```

## Dependencies

See `requirements.txt`:
- numpy, pandas, scikit-learn
- streamlit, altair
- firebase-admin
- lime, shap (interpretability)
- scipy (statistical tests)

## Bibliography

- Random Forests: Breiman, L. (2001)
- Gradient Boosting: Friedman, J. H. (2001)
- LIME: Ribeiro et al. (2016) - "Why Should I Trust You?"
- SHAP: Lundberg & Lee (2017) - "A Unified Approach to Interpreting Model Predictions"

## License

MIT License - See LICENSE file

## Contact

**Author**: Grace Kaimburi  
**GitHub**: https://github.com/GraceKaimburi/HEALTH  
**Repository**: https://github.com/GraceKaimburi/HEALTH.git

---

**Last Updated**: April 15, 2026  
**Version**: 1.0 (Production Ready)
