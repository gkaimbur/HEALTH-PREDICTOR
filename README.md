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

### ✅ RECOMMENDED: Streamlit Cloud (Official)

**Fastest & simplest deployment:**

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and sign in with GitHub
2. Click **"New app"**
3. Select:
   - Repository: `GraceKaimburi/HEALTH`
   - Branch: `main`
   - Main file path: `app.py`
4. Click **"Advanced settings"**
5. Add your Firebase credentials to **"Secrets"** section:
   ```toml
   [firebase]
   type = "service_account"
   project_id = "your-project-id"
   private_key_id = "..."
   private_key = "..."
   client_email = "..."
   client_id = "..."
   auth_uri = "https://accounts.google.com/o/oauth2/auth"
   token_uri = "https://oauth2.googleapis.com/token"
   ```
6. Click **"Deploy"**

**Get Firebase service account:**
- Firebase Console → Project Settings → Service Accounts → Generate New Private Key
- Copy the JSON content into secrets above

**Pros:** Built for Streamlit, free tier, 1-click deployment, auto-updates on `git push`

---

### Alternative 1: Render.com (Free Tier)

**Full control with native Docker support:**

1. Go to [https://render.com](https://render.com) and connect GitHub
2. Click **"New +"** → **"Web Service"**
3. Select `GraceKaimburi/HEALTH` repository
4. Configure:
   - **Name**: `health-hdp-predictor`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=10000 --server.address=0.0.0.0`
5. Add environment variable:
   - **Key**: `FIREBASE_SERVICE_ACCOUNT_BASE64`
   - **Value**: Your base64-encoded service account JSON
   
   *Encode your service account:*
   ```bash
   # On Windows PowerShell:
   [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes((Get-Content firebase-service-account.json -Raw)))
   ```

6. Click **"Create Web Service"**

**deployment auto-starts immediately on push**

**Pros:** Docker-native, persistent disk storage, free tier with $0.10/GB credit, auto-deploys on `git push`

---

### Alternative 2: Railway.app

1. Go to [https://railway.app](https://railway.app) and connect GitHub
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select `GraceKaimburi/HEALTH`
4. Railway auto-detects `Dockerfile` and deploys
5. Add environment variable in Dashboard:
   - `FIREBASE_SERVICE_ACCOUNT_BASE64` = base64-encoded service account
6. Deploy triggers automatically

**Pros:** Excellent Docker support, $5/month free credit, GitHub auto-sync

---

### Comparison Table

| Feature | Streamlit Cloud | Render | Railway |
|---------|-----------------|--------|---------|
| **Setup Time** | 2 minutes | 5 minutes | 5 minutes |
| **Free Tier** | ✅ Yes | ✅ Yes | ✅ Yes ($5 credit) |
| **Persistence** | ❌ Restarts | ✅ 1 GB disk | ✅ Ephemeral |
| **Python Support** | ✅ Native | ✅ Native | ✅ Docker |
| **Auto-Deploy** | ✅ On git push | ✅ On git push | ✅ On git push |
| **Custom Domain** | ✅ Pro plan | ✅ Yes | ✅ Yes |
| **Firebase Ready** | ✅ Built-in secrets | ✅ Env vars | ✅ Env vars |

**Recommendation:** Start with **Streamlit Cloud** (official, simplest). Use **Render** if you need persistent storage beyond Streamlit's ephemeral filesystem.

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
