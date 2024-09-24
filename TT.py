class TruthTable:
    def __init__(self, kb):
        self.kb = kb
        self.models_count = 0

    def is_true(self, symbol, model):
        return model.get(symbol, False)

    def is_satisfied(self, clause, model):
        clause = clause.replace(' ', '')

        if '=>' in clause:
            premise, conclusion = clause.split('=>')
            return not self.is_satisfied(premise, model) or self.is_satisfied(conclusion, model)
        elif '&' in clause:
            conjuncts = clause.split('&')
            return all(self.is_satisfied(conj, model) for conj in conjuncts)
        elif '|' in clause:
            disjuncts = clause.split('|')
            return any(self.is_satisfied(disj, model) for disj in disjuncts)
        elif clause[0] == '~':
            return not self.is_satisfied(clause[1:], model)
        else:
            return self.is_true(clause, model)

    def check_all(self, symbols, model):
        if not symbols:
            # If all symbols have been assigned in the model, check if the KB is satisfied
            if all(self.is_satisfied(clause, model) for clause in self.kb.get_clauses()):
                # If KB is satisfied, check if the query is also satisfied
                if self.is_satisfied(self.query, model):
                    self.models_count += 1  # Increment models_count if the model satisfies the query
                    return True
                else:
                    return False
            else:
                return True  # If KB is not satisfied, this branch is irrelevant
        else:
            rest = symbols.copy()
            symbol = rest.pop()
            model_true = model.copy()
            model_true[symbol] = True
            model_false = model.copy()
            model_false[symbol] = False
            return self.check_all(rest, model_true) and self.check_all(rest, model_false)

    def tt_entails(self, query):
        self.query = query
        symbols = set()
        for clause in self.kb.get_clauses():
            symbols.update({char for char in clause if char.isalpha()})

        # Include the query symbols in the symbols set
        symbols.update({char for char in query if char.isalpha()})

        result = self.check_all(list(symbols), {})
        return result

