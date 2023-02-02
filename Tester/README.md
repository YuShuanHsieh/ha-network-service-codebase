# Tester

To test our server can work correctly and handle numerous requests in a short time, we leverage the power of [k6](https://k6.io/docs/), which is a load testing tool developed from Grafana Labs.

## 1. Installation

Before testing, please install k6 tool with following steps [installation guide](https://k6.io/docs/get-started/installation/).

## 2. Run Tester

You can run k6 tool using the sample scripts.
- config.js
- script.js

```bash
k6 run ./script.js
```

## References
1. [k6 tutorials](https://k6.io/docs/using-k6/http-requests/)
2. [k6 executor](https://k6.io/docs/using-k6/scenarios/executors/)