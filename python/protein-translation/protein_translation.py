protein = {
    'Methionine': ["AUG"],
    'Phenylalanine': ['UUU', 'UUC'],
    'Leucine': ['UUA', 'UUG'],
    'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
    'Tyrosine': ['UAU', 'UAC'],
    'Cysteine': ['UGU', 'UGC'],
    'Tryptophan': ['UGG'],
    'STOP': ['UAA', 'UAG', 'UGA']
}

def proteins(strand):
    res = []
    prots = [strand[i:i+3] for i in range(0, len(strand), 3)]
    for prot in prots:
        if prot in protein['STOP']:
            break
        else:
            for key, val in protein.items():
                if prot in val and not key in res:
                    res.append(key)
    return res
