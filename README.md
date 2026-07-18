# satellite-change-detection
Deep Learning pipeline for satellite image change detection using the OSCD dataset, PyTorch, and Streamlit.
# Satellite Change Detection using Deep Learning

## Overview

This project aims to build an end-to-end satellite image change detection system using the Onera Satellite Change Detection (OSCD) dataset.

The objective is to detect changes between two satellite images captured at different times using deep learning.

This project is being developed as a learning and portfolio project inspired by real-world Earth observation and remote sensing applications.

---

## Features

- Data preprocessing pipeline
- Multi-temporal satellite image loading
- Patch (chip) generation
- Siamese U-Net implementation
- Binary segmentation for change detection
- Evaluation using IoU, Dice Score, Precision, Recall and F1
- Interactive Streamlit dashboard
- Future extension for change captioning

---

## Tech Stack

- Python
- PyTorch
- OpenCV
- NumPy
- Rasterio
- Streamlit

---

## Current Progress

- [x] Dataset downloaded
- [x] Dataset exploration
- [ ] Data preprocessing
- [ ] Dataset loader
- [ ] Model implementation
- [ ] Model training
- [ ] Evaluation
- [ ] Dashboard
- [ ] Documentation

---

## Dataset

Onera Satellite Change Detection Dataset (OSCD)

https://rcdaudt.github.io/oscd/

---

## Project Structure

```text
data/
src/
models/
dashboard/
outputs/
README.md
```

---

## Goals

- Learn remote sensing workflows
- Learn semantic segmentation
- Understand Siamese architectures
- Build an end-to-end computer vision project
- Explore AI for Earth Observation

---

## Status

🚧 Work in Progress
