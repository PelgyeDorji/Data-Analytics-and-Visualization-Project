# Task 1: Columns Layout for Bar + Line (30 min):

Why: Side-by-side for navigation (brief p.2 usability).
Build: Wrap bar/line in st.columns(2) after KPIs.
Code: See full below; test: Responsive on mobile.

# Task 2: Alert Filter Widget (30 min):

Why: Extra interactivity (filter by alert level).
Build: Add st.sidebar.selectbox("Alert Level", ["All", "green", "yellow", "orange", "red"]); apply in filtered_df.
Code: See full; test: "Red" → only majors.

# Task 3: Map Drill-Down Feedback (45 min):

Why: Click events for exploration (brief p.2 filters).
Build: fig1.update_traces(clickmode='event+select'); session_state for success message.
Code: See full; test: Click point → "Selected 1—updating."

# Task 4: Expander for Insights (30 min):

Why: Hidden navigation for recommendations (brief p.2 suggestions).
Build: with st.expander("Dive Deeper"): st.write("Trends: Asia 60%...").
Code: See full; test: Expand/collapse.

# Task 5: Spinner & Annotations (30 min):

Why: Loading feel + chart notes (user polish).
Build: with st.spinner("Updating..."): around visuals; add fig.add_annotation.
Code: See full; test: Filter → spinner shows.