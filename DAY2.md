## Task 1: KPIs (30 min):

Why: Quick overview stats (brief p.3 trends).
Build: Insert after filters: 3-column metrics (total events, avg mag, high-risk count).
Code: See previous snippet; test: Filter → numbers update.

## Task 2: Line Chart - Temporal Trends (45 min):

Why: Shows monthly mag patterns (proposal temporal Q).
Build: Group by month, px.line with markers.
Code: After bar; test: Continent filter → line reshapes.

## Task 3: Heatmap - Correlations (45 min):

Why: Mag vs. lat/lon relationships (brief advanced analytics).
Build: corr() matrix, px.imshow with RdBu scale.
Code: After line; test: High mag → warmer colors.

## Task 4: Gutenberg Plot (60 min):

Why: Hypothesis validation (proposal Gutenberg law).
Build: Histogram bins, log scatter + linregress fit line.
Code: After heatmap; test: Filter → b-value changes (~1.0 default).

## Task 5: Narrative Polish (30 min):

Why: Explains results + suggestions (brief p.2).
Build: Markdown insights/subheaders at end.
Code: Separators + "Insight: ... Suggestion: ML forecasts".