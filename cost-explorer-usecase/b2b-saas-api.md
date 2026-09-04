A realistic FinOps calculation for a small B2B SaaS company running a highly available web app.

Assume the company’s API is hosted on two standard, general-purpose EC2s running Linux in the `us-east-1`. 

They have analyzed their past 3 months in AWS Cost Explorer and confirmed these two instances run 24/7/365 to maintain uptime for their customers.

## The Baseline Resource

### Instance Type:
- `m6i.large` (2 vCPU, 8 GiB RAM)
- standard workhorse for backend apps and web servers

### Quantity: 
- 2 instances
- for High Availability across two AZs

### Hours per month:
- 730 hours
- industry standard average for a full month

## Current On-Demand Cost

On-Demand pricing means you pay exactly for the hours the instance is running, with no long-term commitment.

* **On-Demand Rate:** $0.0960 per hour
* **Cost per Instance:** $0.0960 × 730 hours = **$70.08 / month**
* **Total Current Cost (2 instances):** $70.08 × 2 = **$140.16 / month**

## Reserved Instance (RI) Pricing

Since the instances run continuously, the company decides to look into a **1-Year Standard Reserved Instance with a "No Upfront" payment option**. 

This means they pay nothing today, but they sign a contract agreeing to pay a lower hourly rate for every hour of the next 12 months, regardless of whether the instances are actually running.

* **1-Year RI Rate (No Upfront):** $0.0670 per hour
* **Cost per Instance:** $0.0670 × 730 hours = **$48.91 / month**
* **Total Projected Cost (2 instances):** $48.91 × 2 = **$97.82 / month**

## Analyze the Savings and Breakeven Risk

Now we compare the numbers to see if locking in the 1-year contract makes sense.

| Metric | Amount |
| --- | --- |
| **Current Monthly Cost (On-Demand)** | $140.16 |
| **New Monthly Cost (1-Year RI)** | $97.82 |
| **Monthly Savings** | **$42.34 (30% reduction)** |
| **Annual Savings** | **$508.08** |


## Verdict
For a production app with a stable customer base that definitely needs to stay online for the next year, committing to the RI is an easy decision. 

They immediately cut their compute bill by 30% without paying a dime upfront.