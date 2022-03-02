from LinkedList.Linkedlist import LinkedList
from LinkedList.node import  Node
if __name__=="__main__":
    list= LinkedList()
    '''n1=Node(10)
    n2=Node(20)'''
    #print("*")
    #print(n2.data)

    '''list.head=n1
    n1.next=n2'''
    #list.head=Node(0)
    for i in (1,4):
        if list.head==None:
            list.head=Node(i)
            k=list.head.next
        else:
            k=Node(i)







    curr=list.head
    while(curr!=None):
        print(curr.data)
        curr=curr.next
