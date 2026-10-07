# NETNEXUS - NetExplain

## Problem Statement

PS-015 - Explainable Home and Last-Mile Connectivity Diagnosis

## Project Title

NetExplain - Explainable Connectivity Diagnostic System

## Overview

NetExplain is a desktop-based connectivity diagnostic prototype that performs guided network tests and explains connectivity problems using measurable evidence and deterministic decision rules.

The system evaluates:

- Gateway reachability
- DNS resolution
- External connectivity
- Latency
- Packet loss
- Throughput evidence
- Loaded-network conditions
- Inconclusive cases

## Controlled Fault Scenarios

The prototype evaluates six scenarios:

1. Normal Connection
2. Gateway Unreachable
3. DNS Failure
4. Induced Packet Loss
5. Network Congestion
6. Inconclusive

## Explainability

The diagnosis is generated from explicit evidence-based rules rather than an unexplained prediction.

For example:

- Gateway failure -> Gateway Unreachable
- DNS resolution failure -> DNS Failure
- Packet loss -> Packet Loss Detected
- Elevated latency -> Elevated Latency
- Insufficient evidence -> Inconclusive

For the congestion scenario, latency is evaluated together with controlled throughput evidence under a loaded condition.

## Architecture

User
|
v
Streamlit Dashboard
|
v
Diagnostic Engine
|
+-- Gateway Test
+-- DNS Test
+-- Internet Reachability Test
+-- Packet Loss Measurement
+-- Throughput Evidence
|
v
Decision Engine
|
v
Explainable Diagnosis
|
v
Evidence Timeline
|
v
Diagnostic Report

## Technology Stack

- Python
- Streamlit
- Pandas
- Psutil
- Plotly
- Pytest
- Windows networking utilities

## Controlled Laboratory Testing

The project includes controlled scenario evidence so that known network conditions can be evaluated repeatedly.

Throughput values used in controlled scenarios are explicitly identified as controlled laboratory simulation evidence and are not represented as Internet/WAN measurements.

## Limitations

The system does not claim:

- Physical cable damage
- ISP-internal root cause
- Wi-Fi interference without radio telemetry

The system returns an INCONCLUSIVE result when available evidence cannot isolate a specific cause.

## Evaluation

The automated evaluation covers all six supported scenarios.

Expected evaluation result:

6/6 scenarios passed.

## Running the Project

Create and activate the virtual environment, install the required dependencies, and run:

    $env:PYTHONPATH = (Get-Location).Path
    streamlit run .\app\main.py

Run automated tests with:

    $env:PYTHONPATH = (Get-Location).Path
    python -m pytest -q

Run scenario evaluation with:

    python .\app\tests\evaluation.py

## Team

NETNEXUS
