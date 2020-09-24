void printLinkedListInReverse(ImmutableListNode* head) 
    {
        // initialize a stack of ImmutableListNode pointers
        std::stack<ImmutableListNode*> s;
        
        // iterate through the list and push a pointer to each
        // object onto the stack
        ImmutableListNode* p = head;
        while (p)
        {
            // push the current pointer onto the stack and then 
            s.push(p);
            // set p to the next node
            p = p->getNext();
        }
        
        // print everything as you pop them off the stack
        while (!s.empty())
        {
            ImmutableListNode* top = s.top();
            top->printValue();
            s.pop();
        }
    }