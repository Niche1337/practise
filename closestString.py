# =============================================================================
# In theoretical computer science, the closest string is an NP-hard computational problem, 
# which tries to find the geometrical center of a set of input strings. To understand the word "center", 
# it is necessary to define a distance between two strings.
# Usually, this problem is studied with the Hamming distance in mind. 
# This center must be one of the input strings.
# 
# In bioinformatics, 
# the closest string problem is an intensively studied facet of the problem of finding signals in DNA. 
# In keeping with the bioinformatics utility, we'll use DNA sequences as examples.
# 
# Consider the following DNA sequences:
# 
# ATCAATATCAA
# ATTAAATAACT
# AATCCTTAAAC
# CTACTTTCTTT
# TCCCATCCTTT
# ACTTCAATATA
# Using the Hamming distance (the number of different characters between two sequences of the same length), 
# the all-pairs distances of the above 6 sequences puts ATTAAATAACT at the center.
# 
# Input Description
# You'll be given input with the first line an integer N telling you how many lines to read for the input, 
# then that number of lines of strings. All strings will be the same length. Example:
# 
# 4
# CTCCATCACAC
# AATATCTACAT
# ACATTCTCCAT
# CCTCCCCACTC
# Output Description
# Your program should emit the string from the input that's closest to all of them. Example:
# 
# AATATCTACAT
# Challenge Input
# 11
# AACACCCTATA
# CTTCATCCACA
# TTTCAATTTTC
# ACAATCAAACC
# ATTCTACAACT
# ATTCCTTATTC
# ACTTCTCTATT
# TAAAACTCACC
# CTTTTCCCACC
# ACCTTTTCTCA
# TACCACTACTT
# 
# 21
# ACAAAATCCTATCAAAAACTACCATACCAAT
# ACTATACTTCTAATATCATTCATTACACTTT
# TTAACTCCCATTATATATTATTAATTTACCC
# CCAACATACTAAACTTATTTTTTAACTACCA
# TTCTAAACATTACTCCTACACCTACATACCT
# ATCATCAATTACCTAATAATTCCCAATTTAT
# TCCCTAATCATACCATTTTACACTCAAAAAC
# AATTCAAACTTTACACACCCCTCTCATCATC
# CTCCATCTTATCATATAATAAACCAAATTTA
# AAAAATCCATCATTTTTTAATTCCATTCCTT
# CCACTCCAAACACAAAATTATTACAATAACA
# ATATTTACTCACACAAACAATTACCATCACA
# TTCAAATACAAATCTCAAAATCACCTTATTT
# TCCTTTAACAACTTCCCTTATCTATCTATTC
# CATCCATCCCAAAACTCTCACACATAACAAC
# ATTACTTATACAAAATAACTACTCCCCAATA
# TATATTTTAACCACTTACCAAAATCTCTACT
# TCTTTTATATCCATAAATCCAACAACTCCTA
# CTCTCAAACATATATTTCTATAACTCTTATC
# ACAAATAATAAAACATCCATTTCATTCATAA
# CACCACCAAACCTTATAATCCCCAACCACAC
# Challenge Output
# ATTCTACAACT
# 
# TTAACTCCCATTATATATTATTAATTTACCC
# =============================================================================
dna = []
distance = []

def hamming_distance(string1, string2):
    string1 = string1
    string2 = string2
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance

def clostestString():
    value = 0
    
    for x in range(loops):
        strDna = input("Enter the DNA string  ")
        dna.append(strDna)
               
    for x in range(loops):
        for y in range(loops):
            value += hamming_distance(dna[x], dna[y])
        distance.append(value)
        value = 0
    closest = dna[distance.index(min(distance))]    
    print(f"The closest String is {closest}")
    
loops = int(input("How many strings are there?  "))
clostestString()























