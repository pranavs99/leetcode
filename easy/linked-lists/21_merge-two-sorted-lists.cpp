struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
{
    // creating a dummy node with a known sentinel value
    ListNode* dummy = new ListNode(-1);
    
    // creating a pointer to actually traverse the created list
    ListNode* p = dummy;
    
    // while both of the lists are live, compare the values
    // that are being pointed to
    while (l1 && l2)
    {
        int v1 = l1->val;
        int v2 = l2->val;
        
        // if v1 is less than or equal to v2, then add v1 to the list
        if (v1 <= v2)
        {
            p->next = l1;
            l1 = l1->next;
        }
        // if v2 is strictly less than v1, then add v2 first
        else
        {
            p->next = l2;
            l2 = l2->next;
        }
        
        p = p->next;
    }
    
    // add the remaining parts of a list wasn't processed already
    if (l1)
        p->next = l1;
    else if (l2)
        p->next = l2;
    
    return dummy->next;
}