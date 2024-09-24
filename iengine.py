import sys
from FileReader import FileReader
from KnowledgeBase import KnowledgeBase
from TT import TruthTable
from FC import ForwardChaining
from BC import BackwardChaining

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python iengine.py [test_text_file] [Method]")
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2].upper()  # Convert the method to uppercase

    tell, ask = FileReader.read(filename)
    kb = KnowledgeBase()
    kb.tell(tell)

    if method == 'TT':
        tt = TruthTable(kb)
        result = tt.tt_entails(ask)
        if result:
            print("YES")
        else:
            print("NO")
    elif method == 'FC':
        fc = ForwardChaining(kb)
        result, inferred_symbols = fc.fc_entails(ask)
        if result:
            print(f"YES: {', '.join(sorted(inferred_symbols))}")
        else:
            print("NO")
    elif method == 'BC':
        bc = BackwardChaining(kb)
        result = bc.bc_entails(ask)
        if result:
            # Remove duplicates and maintain order
            final_proven = list(dict.fromkeys(bc.proven))
            print(f"YES: {', '.join(final_proven)}")
        else:
            print("NO")
    else:
        print("Unknown method. Use TT, FC, or BC.")
        sys.exit(1)
