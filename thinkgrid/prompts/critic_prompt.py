CRITIC_PROMPT = """
You are an expert research reviewer.

Review the following report.

Report:
{report}

Evaluate:

1. Accuracy
2. Completeness
3. Depth
4. Clarity
5. Logical Consistency
6. Structure

Return:

# Overall Score

Score: X/10

# Strengths

- ...

# Weaknesses

- ...

# Missing Information

- ...

# Recommendations

- ...

# Final Verdict

Short evaluation.
"""