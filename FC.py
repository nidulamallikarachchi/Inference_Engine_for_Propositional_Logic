class ForwardChaining:
    def __init__(self, kb):
        self.kb = kb
        self.agenda = []
        self.inferred = {}
        self.count = {}

    def fc_entails(self, query):
        for clause in sorted(self.kb.get_clauses()):  # Sort clauses for consistent processing
            if '=>' in clause:
                premise, conclusion = clause.split('=>')
                premises = premise.split('&')
                self.count[clause] = len(premises)
                if conclusion not in self.inferred:
                    self.inferred[conclusion] = False
            else:
                self.agenda.append(clause)

        inferred_order = []  # To keep track of the order of inferred symbols

        while self.agenda:
            self.agenda.sort()  # Sort agenda for consistent processing
            p = self.agenda.pop(0)  # Process agenda in a consistent order
            if p == query:
                return True, inferred_order
            if not self.inferred.get(p, False):
                self.inferred[p] = True
                inferred_order.append(p)
                for clause in sorted(self.kb.get_clauses()):  # Sort clauses for consistent processing
                    if '=>' in clause:
                        premise, conclusion = clause.split('=>')
                        premises = premise.split('&')
                        if p in premises:
                            self.count[clause] -= 1
                            if self.count[clause] == 0:
                                self.agenda.append(conclusion)
        return False, inferred_order
