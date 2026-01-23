#!/usr/bin/env python3
"""Quick test script to verify the backend setup"""
import sys
import os

print("Testing Glaucoma Detection API Setup...")
print("=" * 50)

# Test imports
print("\n1. Testing Python imports...")
try:
    import fastapi
    print("   ✓ FastAPI imported")
except ImportError as e:
    print(f"   ✗ FastAPI import failed: {e}")
    sys.exit(1)

try:
    import uvicorn
    print("   ✓ Uvicorn imported")
except ImportError as e:
    print(f"   ✗ Uvicorn import failed: {e}")
    sys.exit(1)

try:
    import tensorflow as tf
    print(f"   ✓ TensorFlow imported (version: {tf.__version__})")
except ImportError as e:
    print(f"   ✗ TensorFlow import failed: {e}")
    sys.exit(1)

# Test config
print("\n2. Testing configuration...")
try:
    os.chdir("glaucoscan-API")
    from app import load_config
    config = load_config()
    print(f"   ✓ Config loaded - Server port: {config['server']['port']}")
except Exception as e:
    print(f"   ✗ Config load failed: {e}")
    sys.exit(1)

# Test model files
print("\n3. Testing model files...")
model_files = [
    "models/glaucoma_mlp_model.pkl",
    "models/scaler.joblib",
    "models/feature_selector.joblib",
    "models/class_mapping.pkl"
]
all_exist = True
for model_file in model_files:
    if os.path.exists(model_file):
        print(f"   ✓ {model_file} exists")
    else:
        print(f"   ✗ {model_file} MISSING")
        all_exist = False

if not all_exist:
    print("\n⚠ Warning: Some model files are missing!")
    sys.exit(1)

print("\n" + "=" * 50)
print("✓ All checks passed! Backend should be ready to run.")
print("\nTo start the backend, run:")
print("  cd glaucoscan-API")
print("  python app.py")
print("\nThe API will be available at: http://localhost:8236")

