#  File: Poly.py

#  Description: Program to take the sum and product of two polynomials

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 04/5

#  Date Last Modified: 04/7

import sys

class Link(object):
    def __init__(self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next
    
    def __str__(self):
        return '(' + str(self.coeff) + ', ' + str(self.exp) + ')'
    
class LinkedList(object):
    def __init__(self):
        self.first = None

    # keep Links in descending order of exponents
    # use this in main in insert values into the list
    def insert_in_order(self,coeff,exp):
        current = self.first
        if current == None:
            # new link
            new = Link(coeff,exp)
            # set next link at first
            # set first one as new
            self.first = new     

        while current != None:
            if current.exp < exp: #case it goes in front
                new = Link(coeff,exp)
                new.next = current
                self.first = new
                break
            elif current.exp > exp:
                if current.next == None: #belongs at the end
                    new = Link(coeff,exp)
                    current.next = new
                    break
                elif current.next.exp < exp:
                    new = Link(coeff,exp)
                    new.next = current.next
                    current.next = new
                    break
                else: #smaller exp than current and current.next
                    current = current.next
            elif current.exp == exp:
                current.coeff = current.coeff + coeff
                break


    # add polynomial p to this polynomial and return the sum
    def add(self,p):
        # loop through q and check with p val
        qval = self.first
        pval = p.first
        while pval != None:
            test = False
            qval = self.first
            while qval != None:
                if qval.exp == pval.exp:
                    newcoeff = qval.coeff + pval.coeff
                    # set p list value with next coeff
                    qval.coeff = newcoeff
                    # go to next value
                    pval = pval.next
                    qval = self.first
                    test = True
                    break
                qval = qval.next
                    
            if not test:
                # take qval and add it to p
                #new = Link(qval.coeff, qval.exp)
                #p.first = new
                self.insert_in_order(pval.coeff, pval.exp)
                # move on to next q value
                #qval = qval.next
                pval = pval.next

        finalsum = LinkedList()
        qval = self.first
        while qval != None:
            if qval.coeff != 0:
                finalsum.insert_in_order(qval.coeff, qval.exp)
                qval = qval.next
            else:
                qval = qval.next

        return finalsum

    # multiply polynomial p to this polynomial and return the product
    def mult(self, p):
        selfval = self.first
        pval = p.first
        sums = []
        #print(self)
        #print(p)
        # n number linked lists for each diff multipulcation
        while pval != None:
            # linked list create
            if pval == None:
                break 
            else:
                sum = LinkedList()
                selfval = self.first
                while selfval != None:
                    if selfval == None:
                        break
                    else:
                        newcoeff = pval.coeff * selfval.coeff
                        newexp = pval.exp + selfval.exp
                        # new = Link(newcoeff, newexp)
                        # set new node to head of sums list
                        sum.insert_in_order(newcoeff, newexp)
                        # move on to next selfval
                        selfval = selfval.next
                        # keep same pval to be mulitplied across all selfvals
                sums.append(sum)
            # move on to next pval
            pval = pval.next
        #print(sums[0])#, sums[1])
        # when end of list approaches
        # sum up the lists
        for x in range(1, len(sums)):
            #print(sums[x])
            sums[0].add(sums[x])

        finalsum = LinkedList()
        qval = sums[0].first
        while qval != None:
            if qval.coeff != 0:
                finalsum.insert_in_order(qval.coeff, qval.exp)
                qval = qval.next
            else:
                qval = qval.next

        return finalsum

        #eturn sums[0]

    # create a string representation of the polynomial
    def __str__(self):
        current = self.first
        string = ""
        while current != None:
            string += current.__str__()
            string += ' + '
            current = current.next
        return string[:-3]

def main():
    # read data from file poly.in from stdin
    line = sys.stdin.readline()
    line = line.strip()
    # number of poly
    n = int (line)
    p = LinkedList()
    p1 = LinkedList()
    # create polynomial p
    for i in range(n):
        o = sys.stdin.readline()
        o = o.strip()
        z = o.split()
        p.insert_in_order(int(z[0]),int(z[1]))
        p1.insert_in_order(int(z[0]),int(z[1]))
    #print(p)

    # read middle space line
    sys.stdin.readline()

    # create polynomial q
    line = sys.stdin.readline()
    line = line.strip()
    # number of poly
    m = int (line)
    #print(m)
    q = LinkedList()
    q1 = LinkedList()
    for i in range(m):
        #print(i)
        l = sys.stdin.readline()
        l = l.strip()
        v = l.split()
        q.insert_in_order(int(v[0]),int(v[1]))
        q1.insert_in_order(int(v[0]),int(v[1]))
    #print(q)

    # get sum of p and q and print sum
    print(q.add(p))
    
    # get product of p and q and print product
    print(q1.mult(p1))

if __name__ == "__main__":
    main()