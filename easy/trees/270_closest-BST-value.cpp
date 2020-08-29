#include <iostream>
#include <stdlib.h>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// closer()
// input: double target, integer n1, integer n2
// Returns the integer that has a smaller difference between itself
// and target.
int closer(double target, int n1, int n2)
{
    if (abs(n1 - target) > abs(n2 - target))
        return n2;
    else
        return n1;
}

int helper(TreeNode* root, double target, int closest)
{
    // base case: if there are no children, you have to return closest
    if (!root)
        return closest;
    
    /* inductive step: recurse on the correct subtree
    Because we're working with a binary SEARCH tree, we can guarantee that the values
    in the left subtree are ALL less than the root, while the values in the right subtree
    are all GREATER than the root. Therefore, the closest BST value is either in the root,
    or in the correct subtree.

    For example, let's say this is our tree with a target of 3.1:
            4
        2       5
      1   3

    When we're first considering the root value of 4, we assume that it's the closest BST value
    by default. Next, when considering subtrees, we know that no value greater than 4 can be closer
    to 3.1 than 4 (or any value LOWER than 4), so it makes sense to only consider the left subtree
    when looking for the closest BST value.
    */
    if (target < root->val)
        return helper(root->left, target, closer(target, root->val, closest));
    else
        return helper(root->right, target, closer(target, root->val, closest));
}

int closestValue(TreeNode* root, double target)
{
    std::cout << closer(5, 1, 2) << std::endl;
    return helper(root, target, root->val);
}