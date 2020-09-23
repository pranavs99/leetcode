// helper function to get the length of a list, starting
// at ListNode* h
int getLength(ListNode* h)
{
    int result = 0;
    for (ListNode* p = h; p; p = p->next)
        result++;
    return result;
}

bool isPalindrome(ListNode* head)
{
    // push values onto a stack until you hit the middle,
    // then check to make sure that what pops off matches the next node 
    int length = getLength(head);
    
    // if the length is odd, then make sure you push length / 2 + 1 values
    // and then immediately pop off the top (because it's the unmatched
    // middle value)
    int midpoint;
    bool lengthIsOdd = false;
    if (length % 2)
    {
        midpoint = (length / 2) + 1;
        lengthIsOdd = true;
    }
    else
        midpoint = length / 2;
    
    // iterate through midpoint amount of nodes
    stack<int> values;
    ListNode* p = head;
    int i = 0;
    while (i < midpoint)
    {
        values.push(p->val);
        i++;
        p = p->next;
    }
    
    // if the length is odd, pop the top value off the stack
    // because we know it won't have a match
    if (lengthIsOdd)
        values.pop();
    
    // now, iterate through the rest of the list and make sure
    // that every new value matches the top of the stack
    while (!values.empty())
    {
        if (p->val != values.top())
            return false;
        values.pop();
        p = p->next;
    }
    
    return true;
}