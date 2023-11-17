import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | NP VP VP

NP -> NP NP| N | Det N | Det AD N | P NP | AD N | Conj NP
VP -> V | V NP | NP V | Adv VP | VP Adv | Conj VP
AD -> Adj | AD Adj
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    nltk.download('punkt')

    # Set regular expression for tokenizer to only allow words not punctuation or numbers
    tokenizer = nltk.RegexpTokenizer(r'\w*[a-zA-Z]+\w*')

    # Create list of every word
    tokens = tokenizer.tokenize(sentence)

    # Lowercase all words
    tokens = [token.lower() for token in tokens]

    return tokens


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Set list for all noun phrase chunks
    chunks = []

    # Iterate over all subtrees with label NP
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):

        # Check if subtree has subtree with label NP in itself
        subs_with_np = list(subtree.subtrees(filter=lambda t: t.label() == 'NP'))

        if len(subs_with_np) > 1:
            # Has other subtrees with label NP
            continue
        else:
            chunks.append(" ".join(subtree.leaves()))

    print(chunks)
    return []


if __name__ == "__main__":
    main()
