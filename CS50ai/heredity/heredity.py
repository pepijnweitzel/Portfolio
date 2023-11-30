import csv
import itertools
import sys
import math

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # Create list to store all probability values in
    joint_prob = 1

    # Iterate over every person in given dictionary
    for person in people:

        # Check how many copies of gene person has
        if person in one_gene:
            copies = 1
        elif person in two_genes:
            copies = 2
        else:
            copies = 0

        # Check whether person has trait or not
        has_trait = person in have_trait

        # Check whether they have parents or not
        if people[person]["mother"] == None:
            p_copies = PROBS["gene"][copies]
            p_trait = PROBS["trait"][copies][has_trait]
            joint_prob *= (p_copies * p_trait)
        else:

            # Get probability of parent given a copy to child
            # Get p of mother
            if people[person]["mother"] in two_genes:
                p_from_mother = 1 - PROBS['mutation']
            elif people[person]["mother"] in one_gene:
                p_from_mother = 0.5
            else:
                p_from_mother = PROBS['mutation']
            # Get p of father
            if people[person]["father"] in two_genes:
                p_from_father = 1 - PROBS['mutation']
            elif people[person]["father"] in one_gene:
                p_from_father = 0.5
            else:
                p_from_father = PROBS['mutation']

            # Case where child gets 0 copies from parents
            if copies == 0:
                joint_prob *= (1 - p_from_mother) * (1 - p_from_father)
            # Case where child gets 1 copy from parents
            elif copies == 1:
                joint_prob *= ((1 - p_from_mother) * p_from_father) + ((1 - p_from_father) * p_from_mother)
            # Case where child gets 2 copies from parents
            else:
                joint_prob *= p_from_mother * p_from_father

            # Add p of that trait into list of p values
            p_trait = PROBS["trait"][copies][has_trait]
            joint_prob *= (p_trait)

    return joint_prob


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    # Iterate over each person in the family
    for person in probabilities:

        # Get variables
        if person in one_gene:
            gene = 1
        elif person in two_genes:
            gene = 2
        else:
            gene = 0
        trait = person in have_trait

        # Update variables in distribution
        probabilities[person]["gene"][gene] += p
        probabilities[person]["trait"][trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # Iterate over each person in the family
    for person in probabilities:

        # Get sum of all gene probability values and the multiplier for new values
        sum_genes = sum(probabilities[person]["gene"].values())
        multiplier = 1.0 / sum_genes

        # Update probabilities
        for i in range(3):
            probabilities[person]["gene"][i] *= multiplier

        # Get sum of all trait probability values and the multiplier for new values
        sum_traits = sum(probabilities[person]["trait"].values())
        multiplier = 1.0 / sum_traits

        # Update probabilities
        for value in [True, False]:
            probabilities[person]["trait"][value] *= multiplier


if __name__ == "__main__":
    main()
