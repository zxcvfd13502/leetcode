class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head==None: return head
        move =head
        fhs=ListNode(0)
        fhe=ListNode(0)
        ahs=ListNode(0)
        ahe=ListNode(0)
        flag1=True
        flag2=True
        while move!=None:
            if move.val<x:
                if flag1:
                    fhs.next=move
                    fhe.next=move
                    fhs=fhs.next
                    flag1=False
                else:
                    fhe.next=move
                fhe=fhe.next
            else:
                if flag2:
                    ahs.next=move
                    ahs=ahs.next
                    ahe.next=move
                    flag2=False
                else:
                    ahe.next=move
                ahe=ahe.next
            move=move.next
        ahe.next=None
        if flag1:return ahs
        if flag2:
            fhe.next=None
        else:
            fhe.next=ah