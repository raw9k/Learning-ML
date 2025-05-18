import pandas as pd

# Load the dataset from CSV
data = pd.read_csv(r"C:\Users\rauna\Downloads\enjoysport.csv")

# Extract features and labels
X = data.iloc[:, :-1].values  # Features (sky, airtemp, humidity, wind, water, forecast)
y = data.iloc[:, -1].values   # Labels (enjoysport)

# Initialize the most general and most specific hypotheses
def initialize_hypotheses(features):
    num_features = features.shape[1]
    G = [['?' for _ in range(num_features)]]  # Most general hypothesis
    S = [['∅' for _ in range(num_features)]]  # Most specific hypothesis
    return G, S

# Check if a hypothesis is consistent with an example
def is_consistent(hypothesis, example, label):
    for i in range(len(hypothesis)):
        if hypothesis[i] != '?' and hypothesis[i] != example[i]:
            return False
    return True

# Candidate Elimination Algorithm
def candidate_elimination(X, y):
    G, S = initialize_hypotheses(X)
    for i in range(len(X)):
        example = X[i]
        label = y[i]
        if label == 'yes':  # Positive example
            # Update G: Remove inconsistent hypotheses
            G = [h for h in G if is_consistent(h, example, label)]
            # Update S: Generalize to cover the example
            for j in range(len(S[0])):
                if S[0][j] != example[j]:
                    S[0][j] = '?'
        else:  # Negative example
            # Update S: No change (already specific)
            # Update G: Specialize to exclude the example
            new_G = []
            for h in G:
                if not is_consistent(h, example, label):
                    new_G.append(h)
                else:
                    # Specialize h to exclude the example
                    for j in range(len(h)):
                        if h[j] == '?':
                            new_h = h.copy()
                            new_h[j] = example[j]
                            if is_consistent(new_h, example, label):
                                new_G.append(new_h)
            G = new_G
        print(f"Step {i+1}:")
        print(f"G: {G}")
        print(f"S: {S}")
        print()
    return G, S

# Run the algorithm
G, S = candidate_elimination(X, y)

# Final output
print("Final General Hypothesis (G):", G)
print("Final Specific Hypothesis (S):", S)