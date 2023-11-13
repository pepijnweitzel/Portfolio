import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # Create list of evidence and labels
    evidence = []
    labels = []

    # Floats and Ints and Months
    floats = ["Administrative_Duration", "Informational_Duration", "ProductRelated_Duration", "BounceRates", "ExitRates", "PageValues", "SpecialDay"]
    ints = ["Administrative", "Informational", "ProductRelated", "OperatingSystems", "Browser", "Region", "TrafficType"]
    months = ["Jan", "Feb", "Mar", "Apr","May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Open given csv file
    with open(filename) as file:
        reader = csv.DictReader(file)

        # Iterate over every row in the file
        for row in reader:

            # Convert values required to be floats to floats
            for key in floats:
                row[key] = float(row[key])

            # Convert values required to be ints to ints
            for key in ints:
                row[key] = int(row[key])

            # Convert month to int:
            month = row["Month"]
            for i in range(12):
                if month == months[i]:
                    row["Month"] = i
                    break

            # Convert VisitorType to int
            if row["VisitorType"] == "Returning_Visitor":
                row["VisitorType"] = 1
            else:
                row["VisitorType"] = 0

            # Convert Weekend to int
            if row["Weekend"] == "True":
                row["Weekend"] = 1
            else:
                row["Weekend"] = 0

            # Convert Revenue to int
            if row["Revenue"] == "True":
                row["Revenue"] = 1
            else:
                row["Revenue"] = 0

            # Remove label from values and add to list of labels
            label = row.pop("Revenue")
            labels.append(label)

            # Create list of values for in evidence
            users_evidence = list(row.values())

            # Add list to evidence
            evidence.append(users_evidence)

    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # Create model based on KNeighborsClassifier with k=1
    model = KNeighborsClassifier(n_neighbors=1)

    # Train the model on the given test evidence and labels
    model.fit(evidence, labels)

    # Return model
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
