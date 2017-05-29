from collections import deque

from algorithm.parameters import params
from utilities.representation.python_filter import python_filter


class SGEMapper:
    def __init__(self):
        self.genome_mapping = None

    def set_genome_mapping(self, genome_mapping):
        self.genome_mapping = genome_mapping

    def mapper(self, genome, tree):
        phenotype, genome, tree, nodes, invalid, depth, \
        used_codons = self.map_ind_from_genome(genome)

        if params['BNF_GRAMMAR'].python_mode and not invalid:
            # Grammar contains python code
            phenotype = python_filter(phenotype)

        return phenotype, genome, tree, nodes, invalid, depth, used_codons

    def map_ind_from_genome(self, genome):
        bnf_grammar = params['BNF_GRAMMAR']
        # Depth, max_depth, and nodes start from 1 to account for starting root
        # Initialise number of wraps at -1 (since
        used_input, current_depth, max_depth, nodes, wraps = 0, 1, 1, 1, -1

        output = deque()

        positions = deque([0])
        unexpanded_symbols = deque([(bnf_grammar.start_rule, 1)])

        while len(unexpanded_symbols) > 0:
            current_item = unexpanded_symbols.popleft()
            current_symbol, current_depth = current_item[0], current_item[1]

            if max_depth < current_depth:
                # Set the new maximum depth.
                max_depth = current_depth

            # Set output if it is a terminal.
            if current_symbol["type"] != "NT":
                output.append(current_symbol["symbol"])
            else:
                current_pos = positions.popleft()

                # Current item is a new non-terminal. Find associated
                # production choices.
                production_choices = bnf_grammar.rules[current_symbol[
                    "symbol"]]["choices"]
                no_choices = bnf_grammar.rules[current_symbol["symbol"]][
                    "no_choices"]

                # Select a production based on the next available codon in the
                # genome.
                current_production = genome[current_pos] % no_choices

                # Use an input
                used_input += 1

                # Initialise children as empty deque list.
                children = deque()
                nt_count = 0

                for prod in production_choices[current_production]['choice']:
                    # iterate over all elements of chosen production rule.

                    child = [prod, current_depth + 1]

                    # Extendleft reverses the order, thus reverse adding.
                    children.appendleft(child)
                    if child[0]["type"] == "NT":
                        nt_count += 1

                # Add the new children to the list of unexpanded symbols.
                unexpanded_symbols.extendleft(children)

                positions.extendleft(reversed(
                    self.genome_mapping[current_pos][current_production]))

                if len([s for s in unexpanded_symbols if
                        s[0]['type'] == 'NT']) != len(positions):
                    print('asdf')

                if nt_count > 0:
                    nodes += nt_count
                else:
                    nodes += 1

        if len(unexpanded_symbols) != 0 or len(positions) != 0:
            print('asdf')

        # Generate phenotype string.
        output = "".join(output)
        return output, genome, None, nodes, False, max_depth, used_input
