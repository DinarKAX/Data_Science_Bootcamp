# Configuration parameters
num_of_steps = 3
report_template = """Report:
We made {observations} observations from tossing a coin: {tails} of them were tails, {heads} of them were heads. 
The probabilities are {tails_pct:.2f}% and {heads_pct:.2f}% respectively. 
Our forecast: the next {num_predictions} observations will be: {predictions_str}.
"""