# Fulfillment Hub —  Take-Home Project

## 1. What this project solves

The brief describes a spreadsheet/shared-folder fulfillment process where the main problems are:
- order status is hard to see
- delays can go unnoticed
- priority orders can miss same-day deadlines
- inventory mismatches block packing
- wrong products/variants can be shipped
- staged boxes can be misplaced or missed by couriers
- operational issues are handled informally

This prototype focuses on visibility and exception management rather than trying to automate every step.

## 2. Solution

The application is a lightweight **Fulfillment Control Tower** with five areas:

1. **Control Tower** — KPIs and an action queue for priority, deadline-risk and stock-problem orders.
2. **Orders** — searchable/filterable order queue and status updates.
3. **Inventory** — main/overflow stock visibility and a simple stock-move action.
4. **Exceptions** — a persistent issue log with owner, severity and resolution.
5. **Courier Pickup** — pickup board to reduce missed handovers.

## 3. Why these features

The highest-value problems in the brief are the ones that can cause an order to miss its promised shipment or become untraceable. The control tower therefore surfaces:
- Priority orders
- Deadline risk
- Stock mismatches
- Open exceptions
- Courier pickup state

The UI deliberately uses tables, filters and buttons rather than complex automation because the warehouse team is described as experienced but not very comfortable with technology.

## 4. Run locally

### Windows / Mac / Linux

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Mac/Linux:
```bash
source .venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
streamlit run app.py
```

The app opens in your browser.

## 5. Demo flow

Use these sample scenarios:
1. Open Control Tower and point out the action queue.
2. Open Orders and filter to Priority.
3. Open ORD-1006: it is blocked because Main stock is below the order quantity.
4. Open Inventory and move mouse stock from Overflow to Main.
5. Return to Orders and show that the stock issue changes.
6. Open Exceptions and resolve an issue.
7. Open Courier Pickup and change a pickup from Pending to Collected.


## 6. Important prototype limitation

This is a take-home prototype using CSV files as lightweight storage. In a production system, these would be replaced with a database and role-based permissions, with integrations to marketplace orders, courier APIs, barcode scanning and inventory transactions.
