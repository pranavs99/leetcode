bool hasCycle(ListNode* head)
{
    // approach:
    // use two pointers than vary in SPEED
    // we'll have a slow pointer that iterates through every node, one at a time
    // and we'll have a fast pointer jumps a node in between every time it increments
    // the idea is that if the fast pointer ever catches up to the slow pointer, it HAD to
    // have hit a node whose next pointer went back into an earlier node in the list
    // however, if the fast pointer ends up falling off the edge of the list, that
    // means that there's no cycle (because there is an "ending" node)

    if (!head || !head->next)
        return false;
    
    ListNode* slow = head;
    ListNode* fast = head->next;
    
    while (slow != fast)
    {
        if (!fast || !fast->next)
            return false;
        
        slow = slow->next;
        fast = fast->next->next;
    }
    
    return true;
}