from utils.parser import extract_score

feedback = """
# Overall Score

Score: 8.7/10

Strengths

Excellent report.
"""

score = extract_score(feedback)

print(score)