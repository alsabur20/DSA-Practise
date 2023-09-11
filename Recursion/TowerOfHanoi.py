#Tower of hanoi solution using recursion
def TowerOfHanoi(n , source, destination, helper):
    if n==1:
        print ("Move disk 1 from ",source,"to ",destination)
        return
    TowerOfHanoi(n-1, source, helper, destination)
    print ("Move disk",n,"from ",source,"to ",destination)
    TowerOfHanoi(n-1, helper, destination, source)

TowerOfHanoi(3,'S','D','H')