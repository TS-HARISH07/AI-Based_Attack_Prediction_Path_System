# 🛡️ AI-Based Attack Path Prediction System

## 📌 Overview

This project is an advanced cybersecurity system that models network environments as attack graphs and predicts potential attacker movement paths using AI-driven logic and graph analysis.

It simulates real-world Security Operations Center (SOC) behavior by:

* Constructing attack graphs
* Generating possible attack paths
* Scoring risks
* Predicting attacker next steps
* Visualizing attack flow
* Supporting real-time updates from scan data

---

## 🚀 Key Features

### 🔹 Attack Graph Modeling

* Represents hosts, vulnerabilities, and connections
* Uses directed graph (NetworkX)

### 🔹 Attack Path Generation

* Finds all possible attacker paths
* Based on entry points and critical assets

### 🔹 Risk Scoring Engine

* Assigns scores based on:

  * Criticality
  * Path length
  * Exposure

### 🔹 AI-Based Prediction

* Predicts attacker’s next move
* Uses rule-based intelligent decision logic

### 🔹 Real-Time Monitoring

* Detects data changes
* Updates graph, paths, and predictions dynamically

### 🔹 Visualization Engine

* Graphical representation of:

  * Attack paths
  * Predicted next node
* Built using Matplotlib + NetworkX

### 🔹 Structured Output Layer

* JSON-ready results
* Supports future ML and GUI integration

---

## 🧠 Architecture

```
Graph_Engine → Prediction_Engine → Output_Engine → Visualization_Engine
                         ↓
                 RealTime_Engine
```

---

## 📂 Project Structure

```
AI-AttackPredictionPathSystem/
│
├── Graph_Engine/
├── Prediction_Engine/
│   ├── Models/
│   ├── Feature_Engine/
│   └── Output_Engine/
│
├── RealTime_Engine/
├── Visualization_Engine/
│
├── data/raw/
├── main.py
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/AI-AttackPredictionPathSystem.git
cd AI-AttackPredictionPathSystem
```

### 2. Install Dependencies

```bash
pip install networkx matplotlib
```

---

## ▶️ Usage

Run the system:

```bash
python main.py
```

### What happens:

* Builds attack graph
* Generates attack paths
* Scores risk
* Predicts attacker movement
* Displays real-time updates
* Visualizes attack graph

---

## 🔐 Safe Lab Demonstration (Recommended)

Use:

* Kali Linux (VM) → attacker
* Windows Host → target

Example:

```bash
nmap -sV -O <target-ip> -oX scan.xml
```

Then integrate scan data into the system.

---

## 📊 Example Output

```
Path: H1 -> H2 -> H3
Risk: 105
Predicted Next: H3
```

---

## 🎯 Applications

* Cybersecurity research
* SOC simulation
* Attack path analysis
* Threat intelligence modeling
* Academic projects

---

## 🔮 Future Enhancements

* Machine Learning-based prediction
* GUI dashboard
* Live network ingestion
* SIEM integration

---

## 👨‍💻 Author

**Harish T S**
Cybersecurity Student & Developer

---

## 📜 License

This project is licensed under the MIT License.

