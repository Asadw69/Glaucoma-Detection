# Glaucare

**An open-source full stack AI system for early glaucoma detection from retinal fundus images, designed for mobile access and low-resource clinical environments.**

---

## Key Features

- AI-based glaucoma prediction using a lightweight neural network  
- Fundus image upload through a modern web interface  
- Backend built with FastAPI for preprocessing, training, and inference  
- Optimized for energy efficiency and low hardware requirements  
- Modular architecture suitable for research and deployment  
- Docker support for easy setup  

---

## Project Overview

**Glaucare** is a full-stack medical AI project focused on early glaucoma screening using retinal fundus images.

The system is divided into two major components:

- **Glaucare API** – A FastAPI-based backend responsible for image processing, feature extraction, and prediction  
- **Glaucare UI** – A frontend application built with Next.js for uploading images and viewing results  

The project is intended for academic use, experimentation, and prototype-level clinical support tools.

---

## System Architecture

Retinal Fundus Image
↓
Feature Extraction (CNN Backbone)
↓
2048-Dimensional Feature Vector
↓
MLP Classifier
↓
Prediction Output
(Glaucoma / Normal)


---

## Processing Pipeline

Raw Images
↓
Data Augmentation
↓
Feature Extraction
↓
Feature Scaling
↓
Class Balancing
↓
Model Training
↓
Trained Prediction Model


---

## Folder Structure

Glaucare/
├── glaucare-api/ # FastAPI backend
├── glaucare-ui/ # Next.js frontend
├── README.md # Project documentation


Each submodule contains its own setup instructions and configuration details.

---

## Quick Start Guide

### Backend (API)

cd glaucare-api
pip install -r requirements.txt
python app.py


## API documentation will be available at:
http://localhost:8236/docs

## Frontend (UI)
cd glaucare-ui
npm install
npm run dev

## Access the application at:

http://localhost:3000

## Local Prediction (Without UI)
cd glaucare-api
pip install -r requirements.txt
python predict.py


This script loads a sample feature vector and outputs a glaucoma prediction result.

## Use Cases

Academic research and experimentation

Learning project for medical AI pipelines

Prototype screening tool for ophthalmology studies

Demonstration of full-stack AI deployment

## ⚠️ This project is not intended for direct clinical diagnosis without professional medical validation.

Contributors / Owners

Asad Siddiqui 

Mohd Sameer

Mohd Akib

Contact - asadsiddiqui7865@gmail.com
