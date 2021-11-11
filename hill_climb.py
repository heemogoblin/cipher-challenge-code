import ngram_score as ns
import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
quads = ns.ngram_score("english_quadgrams.txt")
quints = ns.ngram_score("english_quintgrams.txt")
def decipher(text, key):
    for char in text:
        print(char, ord(char))
        text.replace(char, key[ord(char)-97])
    return text

def hill_climb(text):
    text = text.replace(" ", "").replace(",", "").replace(".", "").replace("\n", "").lower()
    parent = alphabet
    prev = parent

    maxIters = 1
    prevFitnessQuads = 0
    prevFitnessQuints = 0
    curr_iters = 0
    counter = 0

    while counter < maxIters:
        text = decipher(text, parent)
        print(text)
        
        fitness_quads = quads.fitness(text)
        fitness_quints = quints.fitness(text)
        
        if fitness_quads < prevFitnessQuads:
            prevFitnessQuads = fitness_quads
            prev = parent
            n1 = random.randint(0, 25)
            parent = parent.replace


        counter += 1



if __name__ == "__main__":
    hill_climb("""
Jv asxv tztmd gqbtddyv, asd ydtxgsdqdy adua ndav ixaadq jwy ixaadq, asd hdz odtbrdv odaadq fwaxm dxasdq asd vbmfaxbw jggdjqv, bq, asd vbmfaxbw xv wba ibfwy. Xw asxv tjvd asd qfw sjv ijxmdy jwy rfva od qdgdjady pxas j yxiidqdwa vajqaxwn hdz. 
    """)
