# Teen Mental Health Analysis using Hadoop MapReduce

## Project Overview
This project analyzes a Teen Mental Health dataset using Hadoop MapReduce.  
The objective is to process the dataset in a distributed environment and identify depression patterns among teenagers based on mental health indicators.

The project uses:
- HDFS for distributed storage
- Hadoop Streaming for MapReduce execution
- Python for Mapper and Reducer implementation

---

## Problem Statement
With increasing social media usage among teenagers, concerns have risen about its impact on stress, sleep, addiction, and depression.

This project uses Hadoop MapReduce to analyze teen mental health data and count depressed and non-depressed students using the Depression Label attribute.

---

## Objectives
- Store dataset in HDFS
- Process data using MapReduce
- Count depression cases
- Analyze mental health trends using Big Data tools

---

## Dataset
Dataset File:

Teen_Mental_Health_Dataset.csv

Sample attributes:
- Student ID
- Social Media Usage Hours
- Stress Level
- Sleep Hours
- Anxiety Level
- Addiction Level
- Depression Label

---

## Project Files
Repository contains:

- Project-Report.pdf
- mapper.py
- reducer.py
- Teen_Mental_Health_Dataset.csv
- README.md

---

## Mapper Logic
The mapper reads each record and emits:

(depression_label,1)

Example:

Yes 1  
No 1  
Yes 1

---

## Reducer Logic
Reducer aggregates counts for each depression label.

Example output:

Yes Total_Count  
No Total_Count

---

## HDFS Commands
Create HDFS directory:

```bash
hdfs dfs -mkdir /mentalhealth****
