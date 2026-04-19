# Real-time Network Stability & Latency QA Suite

## Context & Motivation
In high-stakes industrial environments, such as **Blast Furnace Control Rooms**network reliability is a safety-critical factor. Even a few hundred milliseconds of latency can delay emergency sensor data. This project demonstrates an automated QA approach to monitoring and validating network stability for real-time applications.

## Tech Stack
* **Language:** Python 3.x
* **Framework:** PyTest
* **Library:** Ping3 (ICMP-based latency tracking)
* **Concepts:** Real-time Monitoring, Threshold Validation, Stability Assertions.

## Test Scenarios
1. **Connectivity Check:** Ensures the mission-critical host is reachable.
2. **Latency Threshold Test:** Validates that response times stay below the industrial standard (100ms).
3. **Stability Logic:** Verifies the monitoring system's ability to distinguish between minor jitters and critical instability.

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/Rasoul394/Realtime-Network-Stability-QA.git](https://github.com/Rasoul394/Realtime-Network-Stability-QA.git)