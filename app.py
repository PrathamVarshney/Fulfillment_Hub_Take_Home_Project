import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Fulfillment Hub",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS — CLEAN + MODERN + ANIMATED
# ============================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f7fb;
}

/* -----------------------------
   Main container
----------------------------- */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

/* -----------------------------
   Sidebar
----------------------------- */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #172033 55%, #0f172a 100%);
    border-right: 1px solid rgba(255,255,255,0.06);
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

section[data-testid="stSidebar"] .stRadio label {
    border-radius: 10px;
    padding: 8px 10px;
    transition: all 0.2s ease;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.08);
    transform: translateX(3px);
}

.sidebar-logo {
    text-align: center;
    padding: 10px 0 22px 0;
}

.sidebar-icon {
    font-size: 42px;
    animation: floatBox 3s ease-in-out infinite;
}

.sidebar-title {
    font-size: 23px;
    font-weight: 800;
    color: white;
    margin-top: 5px;
}

.sidebar-subtitle {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 3px;
}

.sidebar-footer {
    margin-top: 30px;
    padding: 12px;
    border-radius: 10px;
    background: rgba(255,255,255,0.05);
    font-size: 11px;
    color: #94a3b8;
}

/* -----------------------------
   Header
----------------------------- */

.main-title {
    font-size: 34px;
    font-weight: 800;
    color: #111827;
    letter-spacing: -1px;
    margin-bottom: 4px;
}

.main-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 24px;
}

.live-indicator {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    font-size: 12px;
    color: #15803d;
    font-weight: 600;
    margin-bottom: 8px;
}

.live-dot {
    width: 8px;
    height: 8px;
    background: #22c55e;
    border-radius: 50%;
    display: inline-block;
    box-shadow: 0 0 0 0 rgba(34,197,94,0.6);
    animation: pulse 2s infinite;
}

/* -----------------------------
   Hero
----------------------------- */

.hero {
    position: relative;
    overflow: hidden;
    padding: 25px 28px;
    border-radius: 18px;
    margin-bottom: 22px;
    background: linear-gradient(135deg, #1d4ed8, #2563eb 55%, #4f46e5);
    color: white;
    box-shadow: 0 12px 35px rgba(37,99,235,0.20);
    animation: fadeUp 0.55s ease-out;
}

.hero::before {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    right: -80px;
    top: -130px;
    background: rgba(255,255,255,0.10);
}

.hero::after {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    right: 100px;
    bottom: -120px;
    background: rgba(255,255,255,0.07);
}

.hero h2 {
    margin: 0;
    font-size: 25px;
    font-weight: 800;
    position: relative;
    z-index: 2;
}

.hero p {
    margin: 7px 0 0;
    color: rgba(255,255,255,0.85);
    font-size: 13px;
    position: relative;
    z-index: 2;
}

/* -----------------------------
   KPI cards
----------------------------- */

.kpi-card {
    background: white;
    border: 1px solid #e8edf4;
    border-radius: 15px;
    padding: 18px;
    min-height: 105px;
    box-shadow: 0 4px 15px rgba(15,23,42,0.04);
    transition: all 0.25s ease;
    animation: fadeUp 0.55s ease-out;
}

.kpi-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 28px rgba(15,23,42,0.10);
    border-color: #d7e1ef;
}

.kpi-icon {
    font-size: 21px;
    margin-bottom: 7px;
}

.kpi-label {
    color: #64748b;
    font-size: 12px;
    font-weight: 600;
}

.kpi-value {
    color: #0f172a;
    font-size: 27px;
    font-weight: 800;
    margin-top: 3px;
}

/* -----------------------------
   Section headers
----------------------------- */

.section-title {
    font-size: 18px;
    font-weight: 800;
    color: #111827;
    margin: 20px 0 12px 0;
}

.section-subtitle {
    color: #64748b;
    font-size: 12px;
    margin-top: -7px;
    margin-bottom: 13px;
}

/* -----------------------------
   Panels
----------------------------- */

.panel {
    background: white;
    border: 1px solid #e8edf4;
    border-radius: 15px;
    padding: 18px;
    box-shadow: 0 4px 15px rgba(15,23,42,0.035);
    animation: fadeUp 0.5s ease-out;
}

.panel:hover {
    box-shadow: 0 8px 22px rgba(15,23,42,0.06);
}

/* -----------------------------
   Info strip
----------------------------- */

.info-strip {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 12px;
    padding: 12px 15px;
    color: #1e40af;
    font-size: 13px;
    margin-bottom: 15px;
}

/* -----------------------------
   Alert cards
----------------------------- */

.alert-card {
    border-radius: 12px;
    padding: 12px 14px;
    margin: 7px 0;
    border-left: 4px solid #ef4444;
    background: #fef2f2;
    color: #991b1b;
    transition: all 0.2s ease;
}

.alert-card:hover {
    transform: translateX(4px);
}

.alert-warning {
    border-left-color: #f59e0b;
    background: #fffbeb;
    color: #92400e;
}

.alert-success {
    border-left-color: #22c55e;
    background: #f0fdf4;
    color: #166534;
}

/* -----------------------------
   Status badges
----------------------------- */

.badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
}

.badge-new {
    background: #f1f5f9;
    color: #475569;
}

.badge-processing {
    background: #dbeafe;
    color: #1d4ed8;
}

.badge-picking {
    background: #ede9fe;
    color: #6d28d9;
}

.badge-packing {
    background: #fef3c7;
    color: #92400e;
}

.badge-staged {
    background: #e0f2fe;
    color: #0369a1;
}

.badge-shipped {
    background: #dcfce7;
    color: #166534;
}

.badge-blocked {
    background: #fee2e2;
    color: #991b1b;
}

/* -----------------------------
   Streamlit buttons
----------------------------- */

.stButton > button {
    border-radius: 9px;
    border: none;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 7px 16px rgba(37,99,235,0.20);
}

/* -----------------------------
   Inputs
----------------------------- */

.stSelectbox > div > div,
.stMultiSelect > div > div,
.stTextInput > div > div {
    border-radius: 9px;
}

/* -----------------------------
   Tables
----------------------------- */

div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #e5e7eb;
}

/* -----------------------------
   Metrics
----------------------------- */

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e8edf4;
    padding: 12px;
    border-radius: 12px;
}

/* -----------------------------
   Divider
----------------------------- */

hr {
    border: none;
    height: 1px;
    background: #e5e7eb;
    margin: 22px 0;
}

/* -----------------------------
   Footer
----------------------------- */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 11px;
    padding: 20px 0 5px;
}

/* -----------------------------
   Animations
----------------------------- */

@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(34,197,94,0.55);
    }
    70% {
        box-shadow: 0 0 0 8px rgba(34,197,94,0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(34,197,94,0);
    }
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes floatBox {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-5px);
    }
}

/* -----------------------------
   Mobile
----------------------------- */

@media (max-width: 768px) {

    .block-container {
        padding-top: 1rem;
    }

    .main-title {
        font-size: 26px;
    }

    .hero h2 {
        font-size: 21px;
    }

    .kpi-card {
        margin-bottom: 10px;
    }
}

</style>
""")


# ============================================================
# DATA PATHS
# ============================================================

DATA = Path(__file__).parent / "data"

ORDERS = DATA / "orders.csv"
INVENTORY = DATA / "inventory.csv"
EXCEPTIONS = DATA / "exceptions.csv"
COURIERS = DATA / "couriers.csv"

STATUSES = [
    "New",
    "Processing",
    "Picking",
    "Packing",
    "Staged",
    "Shipped",
    "Blocked"
]


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    orders = pd.read_csv(
        ORDERS,
        parse_dates=[
            "order_time",
            "ship_deadline",
            "shipped_at"
        ]
    )

    inventory = pd.read_csv(INVENTORY)

    exceptions = pd.read_csv(
        EXCEPTIONS,
        parse_dates=[
            "created_at",
            "resolved_at"
        ]
    )

    couriers = pd.read_csv(COURIERS)

    return orders, inventory, exceptions, couriers


def save_data(orders, inventory, exceptions):

    orders.to_csv(
        ORDERS,
        index=False,
        date_format="%Y-%m-%d %H:%M:%S"
    )

    inventory.to_csv(
        INVENTORY,
        index=False
    )

    exceptions.to_csv(
        EXCEPTIONS,
        index=False
    )


orders, inventory, exceptions, couriers = load_data()

now = pd.Timestamp.now().floor("min")


# ============================================================
# DERIVED FIELDS
# ============================================================

orders["is_priority"] = orders["priority"].eq("Priority")

orders["is_open"] = ~orders["status"].eq("Shipped")

orders["deadline_risk"] = (
    orders["is_open"] &
    (
        orders["ship_deadline"]
        <= now + pd.Timedelta(hours=2)
    )
)

orders["age_hours"] = (
    (
        now - orders["order_time"]
    )
    .dt.total_seconds()
    / 3600
).clip(lower=0).round(1)


# ============================================================
# INVENTORY LOOKUP
# ============================================================

inv_lookup = (
    inventory
    .set_index(
        ["sku", "warehouse"]
    )["available_qty"]
    .to_dict()
)

orders["available_qty"] = orders.apply(
    lambda r: inv_lookup.get(
        (r["sku"], "Main"),
        0
    ),
    axis=1
)

orders["stock_issue"] = (
    orders["available_qty"]
    < orders["qty"]
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def status_badge(status):

    css_class = status.lower()

    return f"""
    <span class="badge badge-{css_class}">
        {status}
    </span>
    """

def get_greeting():
    hour = datetime.now().hour
    minute = datetime.now().minute

    if hour < 6:
        return "🌙 Good night"
    elif hour < 12:
        return "🌅 Good morning"
    elif hour == 12 and minute == 0:
        return "☀️ Good noon"
    elif hour < 17:
        return "🌤️ Good afternoon"
    elif hour < 21:
        return "🌆 Good evening"
    else:
        return "🌙 Good night"

def page_header(title, subtitle):

    st.html(
        f"""
        <div class="live-indicator">
            <span class="live-dot"></span>
            LIVE OPERATIONS
        </div>

         <div class="main-title">
            {get_greeting()}, Pratham 👋

        </div>

        <div class="main-subtitle">
            {subtitle}
        </div>
        """
    )

def kpi_card(icon, label, value):

    return f"""
    <div class="kpi-card">
        <div class="kpi-icon">{icon}</div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html(
        """
        <div class="sidebar-logo">

            <div class="sidebar-icon">
                📦
            </div>

            <div class="sidebar-title">
                Fulfillment Hub
            </div>

            <div class="sidebar-subtitle">
                Operations Control Tower
            </div>

        </div>
        """
    )

    st.divider()

    st.markdown("### Navigation")

    page = st.radio(
        "Go to",
        [
            "Control Tower",
            "Orders",
            "Inventory",
            "Exceptions",
            "Courier Pickup"
        ],
        label_visibility="collapsed"
    )

    # st.html(
    #     """
    #     <div class="sidebar-footer">
    #         <b>Demo Environment</b><br><br>
    #         Sample operational data<br>
    #         Built for fulfillment workflow<br><br>
    #         📊 Control Tower<br>
    #         📦 Order Management<br>
    #         🏬 Inventory<br>
    #         🚨 Exceptions<br>
    #         🚚 Courier Pickup
    #     </div>
    #     """
    # )


# ============================================================
# CONTROL TOWER
# ============================================================

if page == "Control Tower":

    page_header(
        "Fulfillment Control Tower",
        "A real-time operational view of orders, inventory risks, exceptions and courier readiness."
    )

    st.html(
        """
        <div class="hero">

            <h2>
                📦 Keep every order moving
            </h2>

            <p>
                Monitor fulfillment bottlenecks, prioritize urgent orders,
                catch stock issues early and prevent missed courier pickups.
            </p>

        </div>
        """
    )

    # -----------------------------
    # KPIs
    # -----------------------------

    open_orders = int(
        orders["is_open"].sum()
    )

    priority_open = int(
        (
            orders["is_open"]
            &
            orders["is_priority"]
        ).sum()
    )

    at_risk = int(
        orders["deadline_risk"].sum()
    )

    stock_issues = int(
        orders["stock_issue"].sum()
    )

    unresolved = int(
        (
            exceptions["status"]
            == "Open"
        ).sum()
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.html(
            kpi_card(
                "📦",
                "Open Orders",
                open_orders
            )
        )

    with c2:
        st.html(
            kpi_card(
                "⚡",
                "Priority Open",
                priority_open
            )
        )

    with c3:
        st.html(
            kpi_card(
                "⏰",
                "Deadline Risk",
                at_risk
            )
        )

    with c4:
        st.html(
            kpi_card(
                "📉",
                "Stock Issues",
                stock_issues
            )
        )

    with c5:
        st.html(
            kpi_card(
                "🚨",
                "Open Exceptions",
                unresolved
            )
        )

    st.divider()

    # -----------------------------
    # ACTION QUEUE + CHART
    # -----------------------------

    left, right = st.columns(
        [1.45, 1]
    )

    with left:

        st.html(
            '<div class="section-title">🚨 Action Queue</div>'
        )

        st.html(
            '<div class="section-subtitle">Orders requiring immediate attention</div>'
        )

        action = orders[
            orders["is_open"]
            &
            (
                orders["is_priority"]
                |
                orders["deadline_risk"]
                |
                orders["stock_issue"]
            )
        ].copy()

        action["Reason"] = action.apply(
            lambda r:
                "Stock unavailable"
                if r["stock_issue"]
                else
                "Priority order"
                if r["is_priority"]
                else
                "Deadline within 2 hours",
            axis=1
        )

        action = action.sort_values(
            [
                "stock_issue",
                "is_priority",
                "ship_deadline"
            ],
            ascending=[
                False,
                False,
                True
            ]
        )

        if len(action):

            st.dataframe(
                action[
                    [
                        "order_id",
                        "sku",
                        "variant",
                        "qty",
                        "status",
                        "priority",
                        "ship_deadline",
                        "Reason"
                    ]
                ],
                width="stretch",
                hide_index=True
            )

        else:

            st.html(
                """
                <div class="alert-success">
                    ✓ No urgent orders currently require attention.
                </div>
                """
            )

    with right:

        st.html(
            '<div class="section-title">📊 Orders by Status</div>'
        )

        st.html(
            '<div class="section-subtitle">Current fulfillment pipeline</div>'
        )

        status_counts = (
            orders["status"]
            .value_counts()
            .reindex(
                STATUSES,
                fill_value=0
            )
        )

        # Do NOT use width="stretch" here.
        # This keeps compatibility with your local Streamlit version.
        st.bar_chart(
            status_counts,
            height=310
        )

    st.html(
        '<div class="section-title">🚚 Courier Pickup Board</div>'
    )

    pickup = couriers.copy()

    pickup["pickup_status"] = (
        pickup["pickup_status"]
        .fillna("Pending")
    )

    st.dataframe(
        pickup[
            [
                "courier",
                "pickup_time",
                "pickup_status",
                "orders_ready",
                "contact"
            ]
        ],
        width="stretch",
        hide_index=True
    )


# ============================================================
# ORDERS
# ============================================================

elif page == "Orders":

    page_header(
        "Order Queue",
        "Search, filter and update fulfillment orders from one operational queue."
    )

    # -----------------------------
    # Filters
    # -----------------------------

    f1, f2, f3, f4 = st.columns(4)

    status_filter = f1.multiselect(
        "Status",
        STATUSES,
        default=STATUSES
    )

    priority_filter = f2.selectbox(
        "Priority",
        [
            "All",
            "Priority",
            "Regular"
        ]
    )

    risk_filter = f3.selectbox(
        "Deadline",
        [
            "All",
            "At risk",
            "On track"
        ]
    )

    search = f4.text_input(
        "Search order / SKU",
        placeholder="e.g. ORD-1006"
    )

    view = orders.copy()

    view = view[
        view["status"].isin(
            status_filter
        )
    ]

    if priority_filter != "All":

        view = view[
            view["priority"]
            == priority_filter
        ]

    if risk_filter == "At risk":

        view = view[
            view["deadline_risk"]
        ]

    elif risk_filter == "On track":

        view = view[
            ~view["deadline_risk"]
        ]

    if search:

        view = view[
            view["order_id"]
            .str.contains(
                search,
                case=False,
                na=False
            )
            |
            view["sku"]
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.html(
        f"""
        <div class="info-strip">
            🔎 Showing <b>{len(view)}</b> matching order(s)
            from the fulfillment queue.
        </div>
        """
    )

    # -----------------------------
    # Order table
    # -----------------------------

    st.dataframe(
        view[
            [
                "order_id",
                "order_time",
                "customer",
                "sku",
                "product",
                "variant",
                "qty",
                "priority",
                "status",
                "ship_deadline",
                "available_qty",
                "stock_issue"
            ]
        ],
        width="stretch",
        hide_index=True
    )

    st.divider()

    # -----------------------------
    # Update status
    # -----------------------------

    st.html(
        '<div class="section-title">✏️ Update Order Status</div>'
    )

    if len(view):

        order_options = view[
            "order_id"
        ].tolist()

    else:

        order_options = orders[
            "order_id"
        ].tolist()

    order_id = st.selectbox(
        "Order",
        order_options
    )

    current = orders.loc[
        orders["order_id"] == order_id,
        "status"
    ].iloc[0]

    new_status = st.selectbox(
        "New status",
        STATUSES,
        index=STATUSES.index(
            current
        )
    )

    if st.button(
        "💾 Save Status",
        type="primary"
    ):

        orders.loc[
            orders["order_id"]
            == order_id,
            "status"
        ] = new_status

        if new_status == "Shipped":

            orders.loc[
                orders["order_id"]
                == order_id,
                "shipped_at"
            ] = pd.Timestamp.now()

        save_data(
            orders,
            inventory,
            exceptions
        )

        st.cache_data.clear()

        st.success(
            f"{order_id} moved from "
            f"{current} → {new_status}."
        )

        st.rerun()


# ============================================================
# INVENTORY
# ============================================================

elif page == "Inventory":

    page_header(
        "Inventory & Replenishment",
        "Track warehouse availability and move stock from overflow before orders get blocked."
    )

    inv = inventory.copy()

    inv["stock_status"] = inv.apply(
        lambda r:
            "Out of stock"
            if r["available_qty"] <= 0
            else
            "Low stock"
            if r["available_qty"]
            <= r["reorder_level"]
            else
            "Healthy",
        axis=1
    )

    total_skus = len(
        inv["sku"].unique()
    )

    low_stock = len(
        inv[
            inv["stock_status"]
            == "Low stock"
        ]
    )

    out_stock = len(
        inv[
            inv["stock_status"]
            == "Out of stock"
        ]
    )

    healthy = len(
        inv[
            inv["stock_status"]
            == "Healthy"
        ]
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.html(
            kpi_card(
                "📦",
                "Total SKUs",
                total_skus
            )
        )

    with c2:
        st.html(
            kpi_card(
                "🟡",
                "Low Stock",
                low_stock
            )
        )

    with c3:
        st.html(
            kpi_card(
                "🔴",
                "Out of Stock",
                out_stock
            )
        )

    with c4:
        st.html(
            kpi_card(
                "🟢",
                "Healthy",
                healthy
            )
        )

    st.divider()

    st.html(
        '<div class="section-title">🏬 Warehouse Inventory</div>'
    )

    st.dataframe(
        inv,
        width="stretch",
        hide_index=True
    )

    low = inv[
        inv["stock_status"]
        != "Healthy"
    ]

    st.html(
        '<div class="section-title">⚠️ Items Requiring Attention</div>'
    )

    if len(low):

        for _, row in low.iterrows():

            if row["stock_status"] == "Out of stock":

                st.html(
                    f"""
                    <div class="alert-card">
                        <b>🔴 {row['sku']}</b> —
                        {row['product']} ({row['variant']})
                        <br>
                        <small>
                        Warehouse: {row['warehouse']} |
                        Available: {row['available_qty']} |
                        Reorder level: {row['reorder_level']}
                        </small>
                    </div>
                    """
                )

            else:

                st.html(
                    f"""
                    <div class="alert-card alert-warning">
                        <b>🟡 {row['sku']}</b> —
                        {row['product']} ({row['variant']})
                        <br>
                        <small>
                        Warehouse: {row['warehouse']} |
                        Available: {row['available_qty']} |
                        Reorder level: {row['reorder_level']}
                        </small>
                    </div>
                    """
                )

    else:

        st.html(
            """
            <div class="alert-card alert-success">
                ✓ No inventory alerts. All stock levels are healthy.
            </div>
            """
        )

    st.divider()

    # -----------------------------
    # Stock movement
    # -----------------------------

    st.html(
        '<div class="section-title">🔄 Move Stock from Overflow</div>'
    )

    st.html(
        """
        <div class="section-subtitle">
            Transfer available units from the nearby overflow warehouse
            into the main warehouse.
        </div>
        """
    )

    sku = st.selectbox(
        "SKU",
        inventory["sku"].unique()
    )

    qty = st.number_input(
        "Quantity to move",
        min_value=1,
        value=1
    )

    if st.button(
        "🔄 Create Stock Move",
        type="primary"
    ):

        main_rows = inventory[
            (inventory["sku"] == sku)
            &
            (
                inventory["warehouse"]
                == "Main"
            )
        ]

        overflow_rows = inventory[
            (inventory["sku"] == sku)
            &
            (
                inventory["warehouse"]
                == "Overflow"
            )
        ]

        if len(main_rows) == 0:

            st.error(
                "Main warehouse record not found."
            )

        elif len(overflow_rows) == 0:

            st.error(
                "Overflow warehouse record not found."
            )

        else:

            main_idx = main_rows.index[0]

            overflow_idx = overflow_rows.index[0]

            if (
                inventory.loc[
                    overflow_idx,
                    "available_qty"
                ]
                < qty
            ):

                st.error(
                    "Not enough stock in Overflow."
                )

            else:

                inventory.loc[
                    overflow_idx,
                    "available_qty"
                ] -= qty

                inventory.loc[
                    main_idx,
                    "available_qty"
                ] += qty

                save_data(
                    orders,
                    inventory,
                    exceptions
                )

                st.cache_data.clear()

                st.success(
                    f"✓ Moved {qty} unit(s) of "
                    f"{sku} from Overflow → Main."
                )

                st.rerun()


# ============================================================
# EXCEPTIONS
# ============================================================

elif page == "Exceptions":

    page_header(
        "Exception Management",
        "Capture operational problems in one place so issues are visible, owned and resolved."
    )

    open_count = int(
        (
            exceptions["status"]
            == "Open"
        ).sum()
    )

    resolved_count = int(
        (
            exceptions["status"]
            == "Resolved"
        ).sum()
    )

    high_count = int(
        (
            (
                exceptions["severity"]
                == "High"
            )
            &
            (
                exceptions["status"]
                == "Open"
            )
        ).sum()
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.html(
            kpi_card(
                "🚨",
                "Open",
                open_count
            )
        )

    with c2:
        st.html(
            kpi_card(
                "🔴",
                "High Severity",
                high_count
            )
        )

    with c3:
        st.html(
            kpi_card(
                "✅",
                "Resolved",
                resolved_count
            )
        )

    st.divider()

    st.html(
        '<div class="section-title">📋 Exception Log</div>'
    )

    st.html(
        '<div class="section-subtitle">Operational issues requiring visibility and ownership</div>'
    )

    open_only = st.checkbox(
        "Show open exceptions only",
        value=True
    )

    if open_only:

        view = exceptions[
            exceptions["status"]
            == "Open"
        ]

    else:

        view = exceptions

    st.dataframe(
        view[
            [
                "exception_id",
                "order_id",
                "type",
                "severity",
                "description",
                "owner",
                "status",
                "created_at"
            ]
        ],
        width="stretch",
        hide_index=True
    )

    st.divider()

    st.html(
        '<div class="section-title">✓ Resolve an Exception</div>'
    )

    ex_id = st.selectbox(
        "Exception",
        exceptions[
            "exception_id"
        ].tolist()
    )

    selected_ex = exceptions[
        exceptions["exception_id"]
        == ex_id
    ].iloc[0]

    if selected_ex["status"] == "Resolved":

        st.html(
            """
            <div class="alert-card alert-success">
                ✓ This exception has already been resolved.
            </div>
            """
        )

    else:

        st.html(
            f"""
            <div class="info-strip">
                <b>{selected_ex['type']}</b>
                &nbsp; • &nbsp;
                Order: <b>{selected_ex['order_id']}</b>
                &nbsp; • &nbsp;
                Severity: <b>{selected_ex['severity']}</b>
            </div>
            """
        )

        if st.button(
            "✓ Mark Resolved",
            type="primary"
        ):

            exceptions.loc[
                exceptions["exception_id"]
                == ex_id,
                "status"
            ] = "Resolved"

            exceptions.loc[
                exceptions["exception_id"]
                == ex_id,
                "resolved_at"
            ] = pd.Timestamp.now()

            save_data(
                orders,
                inventory,
                exceptions
            )

            st.cache_data.clear()

            st.success(
                f"{ex_id} resolved successfully."
            )

            st.rerun()


# ============================================================
# COURIER PICKUP
# ============================================================

elif page == "Courier Pickup":

    page_header(
        "Courier Pickup Board",
        "Make packed-box handover visible and reduce missed or forgotten courier pickups."
    )

    st.html(
        """
        <div class="info-strip">
            🚚 <b>Operational control:</b>
            Confirm that packed boxes are staged and handed over
            before the courier leaves.
        </div>
        """
    )

    # -----------------------------
    # Courier KPIs
    # -----------------------------

    total_couriers = len(couriers)

    ready_count = int(
        (
            couriers["pickup_status"]
            == "Ready"
        ).sum()
    )

    pending_count = int(
        (
            couriers["pickup_status"]
            == "Pending"
        ).sum()
    )

    missed_count = int(
        (
            couriers["pickup_status"]
            == "Missed"
        ).sum()
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.html(
            kpi_card(
                "🚚",
                "Couriers",
                total_couriers
            ),
        )

    with c2:
        st.html(
            kpi_card(
                "🟢",
                "Ready",
                ready_count
            ),
        )

    with c3:
        st.html(
            kpi_card(
                "🟡",
                "Pending",
                pending_count
            ),
        )

    with c4:
        st.html(
            kpi_card(
                "🔴",
                "Missed",
                missed_count
            ),
        )

    st.divider()

    st.html(
        '<div class="section-title">🚚 Pickup Schedule</div>'
    )

    st.dataframe(
        couriers,
        width="stretch",
        hide_index=True
    )

    st.divider()

    st.html(
        '<div class="section-title">🔄 Update Pickup Status</div>'
    )

    courier = st.selectbox(
        "Courier",
        couriers[
            "courier"
        ].tolist()
    )

    status = st.selectbox(
        "Pickup status",
        [
            "Pending",
            "Ready",
            "Collected",
            "Missed"
        ]
    )

    if st.button(
        "💾 Update Pickup",
        type="primary"
    ):

        couriers.loc[
            couriers["courier"]
            == courier,
            "pickup_status"
        ] = status

        couriers.to_csv(
            COURIERS,
            index=False
        )

        st.cache_data.clear()

        st.success(
            f"{courier} pickup marked as {status}."
        )

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">
        📦 Fulfillment Hub &nbsp;•&nbsp;
        Operations Control Tower &nbsp;•&nbsp;
        Demo Application &nbsp;•&nbsp;
        Sample Data
    </div>
    """
)