class KnowledgeBase:
    def __init__(self):
        self.clauses = set()

    def add_clause(self, clause):
        self.clauses.add(clause)

    def tell(self, knowledge):
        for clause in knowledge:
            self.add_clause(clause)

    def get_clauses(self):
        return self.clauses
