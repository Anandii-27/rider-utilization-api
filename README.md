# Rider Utilization Analysis

## Overview

This project analyzes rider utilization at two levels:

1. **City-Level Utilization (Bangalore)**
2. **Area-Level Utilization using Uber H3 Geospatial Indexing**

The goal is to identify rider availability, rider occupancy, and utilization patterns across Bangalore and within specific operational areas.

---

## Problem Statement

A single city-wide utilization percentage provides only a high-level view of rider activity.

To identify localized demand and supply patterns, utilization is also calculated at the H3 hexagon level, enabling area-wise operational analysis.

---

## Objectives

* Calculate Bangalore-wide rider utilization.
* Calculate area-wise rider utilization using H3 hexagons.
* Identify areas with high rider occupancy.
* Identify areas with available rider capacity.
* Provide a foundation for future real-time analytics and operational decision-making.

---

## Data Used

### Rider Dataset

The analysis uses the following fields:

* delivery_partner_id
* pickup_cluster
* pickup_latitude
* pickup_longitude
* occupied_flag

Where:

* occupied_flag = 1 → Busy Rider
* occupied_flag = 0 → Free Rider

### Cluster Mapping Dataset

The following fields are used:

* parent_geozone_id
* geozone_name

This mapping converts cluster IDs into readable area names.

---

## Bangalore-Level Utilization

### Metrics Calculated

* Busy Riders
* Free Riders
* Total Riders
* Utilization Percentage

### Formula

Utilization (%) = (Busy Riders / Total Riders) × 100

This provides an overall utilization percentage for Bangalore.

---

## H3-Based Area Utilization

### Why H3?

Traditional cluster-level analysis provides only broad area insights.

Uber's H3 indexing system divides the city into hexagonal geographic cells, allowing more granular operational analysis.

### H3 Resolution

This project uses:

**H3 Resolution = 6**

Resolution 6 provides larger operational zones suitable for city-wide utilization monitoring and area-level analysis.

### Methodology

#### Step 1

Convert pickup latitude and longitude into H3 cells.

#### Step 2

Map pickup clusters to cluster names.

#### Step 3

Group riders by:

* H3 Cell
* Cluster Name

#### Step 4

Calculate:

* Busy Riders
* Free Riders
* Total Riders
* Utilization Percentage

for each H3 area.

---

## Sample Output

| H3 Cell         | Cluster Name | Busy Riders | Free Riders | Utilization (%) |
| --------------- | ------------ | ----------- | ----------- | --------------- |
| 86618927fffffff | HSR          | 120         | 30          | 80.00           |
| 86618925fffffff | Koramangala  | 95          | 45          | 67.86           |
| 86618924fffffff | Whitefield   | 140         | 20          | 87.50           |

---

## Technologies Used

* Python
* Pandas
* H3
* PostgreSQL
* FastAPI
* Git
* GitHub

---

## Future Enhancements

* Direct PostgreSQL integration
* Real-time utilization API using FastAPI
* MCP Tool integration
* LLM-powered operational queries
* H3 heatmap visualization
* Live rider monitoring dashboard

---

## Repository Structure

```text
rider-utilization/
│
├── main.py
├── h3_utilization.py
├── requirements.txt
├── README.md
└── .gitignore
```

---


