dict = {
    "AUG":"Methionine",
    "UUU":"Phenylalanine",
    "UUC":"Phenylalanine",
    "UUA":"Leucine",
    "UUG":"Leucine",
    "UCU":"Serine", 
    "UCC":"Serine",
    "UCA":"Serine",
    "UCG":"Serine",
    "UAU":"Tyrosine",
    "UAC":"Tyrosine",
    "UGU":"Cysteine",
    "UGC":"Cysteine",
    "UGG":"Tryptophan",
    "UAA":"STOP",
    "UAG":"STOP",
    "UGA":"STOP"
}

def proteins(strand):
    arr = []
    for i in range(0,len(strand),3):
        curr_protein = strand[i:3+i]
        if(dict[curr_protein] == "STOP"):
            break
        arr.append(dict[curr_protein])
    return arr