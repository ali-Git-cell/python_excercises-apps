# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive function calls
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)


disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
#function call
hanoi(disks, 'A', 'B', 'C')