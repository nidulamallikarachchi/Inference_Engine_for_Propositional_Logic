class BackwardChaining:
    def __init__(self, kb):
        self.kb = kb
        self.agenda = []  # To keep track of goals
        self.inferred = {}  # To keep track of inferred propositions
        self.proven = []  # To keep track of proven propositions in order

    def bc_entails(self, query):
        self.agenda = [query]
        self.inferred = {symbol: False for symbol in self.get_all_symbols()}
        self.inferred[query] = False  # Ensure the query symbol is included

        while self.agenda:
            q = self.agenda.pop()
            if not self.inferred[q]:
                self.inferred[q] = True
                if not self.bc_or(q):
                    return False
        return True

    def bc_or(self, goal):
        for clause in self.kb.get_clauses():
            clause = clause.strip()
            if '=>' in clause:
                premise, conclusion = clause.split('=>')
                conclusion = conclusion.strip()
                if conclusion == goal:
                    premises = [p.strip() for p in premise.split('&')]
                    if self.bc_and(premises):
                        self.proven.append(goal)  # Track proven goals here
                        return True
            elif clause.strip() == goal:
                self.proven.append(goal)  # Track proven known facts
                return True
        return False

    def bc_and(self, goals):
        for goal in goals:
            if goal not in self.inferred:
                self.inferred[goal] = False  # Ensure all goals are in the inferred dictionary
            if not self.inferred[goal]:
                if not self.bc_or(goal):  # Recursively prove each goal
                    return False
        return True

    def get_all_symbols(self):
        symbols = set()
        for clause in self.kb.get_clauses():
            clause = clause.replace(' ', '')
            if '=>' in clause:
                premise, conclusion = clause.split('=>')
                symbols.update({char for char in premise if char.isalpha()})
                symbols.update({char for char in conclusion if char.isalpha()})
            else:
                symbols.update({char for char in clause if char.isalpha()})
        return symbols
