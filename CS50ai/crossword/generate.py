import sys
import copy
from collections import deque


from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # Create copy of set to iterate over
        iter_domain = copy.deepcopy(self.domains)

        # Iterate over all variables in crossword puzzle and remove words with the wrong length
        for domain in self.domains:
            for word in iter_domain[domain]:
                if len(word) != domain.length:
                    self.domains[domain].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # Set revised to false
        revised = False

        # Get the index of what characters should match in the words if there is, otherwise return False
        if self.crossword.overlaps[x, y] == None:
            return revised
        else:
            i, j = self.crossword.overlaps[x, y]

        # Create copy of set to iterate over
        iter_domain = copy.deepcopy(self.domains[x])

        # Iterate over all words in x's domain
        for v1 in iter_domain:

            # Set variable to see whether word in x's domain has possible options in y's domain
            possible_y_words = 0

            # Iterate over all words in y's domain to check if y's word can be used if x's word is used
            for v2 in self.domains[y]:
                # If word is possible add 1 to count
                if v1[i] == v2[j]:
                    possible_y_words += 1

            # If no possible matches in y for x's word remove the word
            if possible_y_words == 0:
                self.domains[x].remove(v1)
                # Set revised to True since a revision has been made
                revised = True
            # Otherwise set possible_y_words back to 0 and keep x's word
            else:
                possible_y_words = 0

        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # Create the queue from given arcs or otherwise all arcs in the problem
        if arcs == None:
            queue = deque()
            for x in self.domains:
                for y in self.crossword.neighbors(x):
                    queue.append((x, y))
        else:
            queue = deque
            for arc in arcs:
                queue.append(arc)


        # Loop over all arcs
        while len(queue) != 0:

            # Dequeue first arc
            x, y = queue.popleft()

            # Make arc arc consistent
            if self.revise(x, y):

                # Check if x still has possible variables
                if len(self.domains[x]) == 0:
                    return False
                # Add neighbors of variable x to the queue to check if they can still be arc consistent but dont add y
                for z in self.crossword.neighbors(x):
                    if z == y:
                        continue
                    queue.append((z, x))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # Check whether length is the same
        if len(self.domains) == len(assignment):

            # Iterate over all keys and check if its value is not None
            for key in assignment:
                if assignment[key]:
                    continue
                else:
                    return False
            return True

        else:
            return False

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # Check for duplicates
        # Get list of all words
        values = [word for word in assignment.values()]

        # Check for duplicates in list, if so return False
        for i in range(len(values)):
            if values.count(values[i]) != 1:
                return False

        # Check whether length of words match length of variable
        for variable in assignment:
            if variable.length != len(assignment[variable]):
                return False

        # Check the overlaps of all variables words
        # Iterate over all variables in assignment
        for variable in assignment:

            # Iterate over all neighbors of variable
            for neighbor in self.crossword.neighbors(variable):

                # Get overlapping characters
                i, j = self.crossword.overlaps[variable, neighbor]

                # Check whether overlapping characters match
                if assignment[variable][i] != assignment[neighbor][j]:
                    return False

        return True



    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        values = list(self.domains[var])
        return values

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # Get list of already assigned variables
        used_variables = []
        for variable in assignment:
            used_variables.append(variable)

        # Get list of all variables
        variables = []
        for variable in self.domains:
            variables.append(variable)


    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
