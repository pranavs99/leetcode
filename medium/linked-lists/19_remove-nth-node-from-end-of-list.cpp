struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* removeNthFromEnd(ListNode* head, int n) 
{
    /* one-pass, two-pointer method
        1) pFar is the pointer that is farther along the list
        2) pClose is the pointer that will actually hit the node
            to be deleted
        3) move pFar n + 1 nodes out
        4) now that pFar is n + 1 nodes away from pClose, move them both
            along until pFar falls off the edge
        5) now pClose is pointing to the node right BEFORE the one
            we want to delete
        6) stitch pClose to whatever follows the target node
        7) delete the target node
    */
    
    // create a dummy node, in case we need to delete the first
    // node
    ListNode* dummy = new ListNode;
    dummy->next = head;
    
    ListNode* pFar = dummy;
    ListNode* pClose = dummy;
    
    // moving pFar to be n + 1 nodes away from pClose
    for (int i = 0; i < n + 1; i++)
        pFar = pFar->next;
    
    // moving both pFar and pClose along until pFar falls off
    // the edge
    while (pFar)
    {
        pFar = pFar->next;
        pClose = pClose->next;
    }
    
    // now, kill the node following pClose
    ListNode* target = pClose->next;
    pClose->next = target->next;
    delete target;
    
    return dummy->next;
}