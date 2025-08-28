// DAY 27/08/2025
/* 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
*/

/* 
MY SOLUTION
Dummy Pointer
Intuition: Create a dummy node to make it easier to assemble the list, we use a pointer (current) that points to the next smallest node between list1 and list2. We move forward in the list from where the node was removed. At the end, we link current.next to the rest of non-exhausted list. Return dummy.next.
*/

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode dummy;
    struct ListNode* current = &dummy;
    dummy.next = NULL;

    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            current->next = list1;
            list1 = list1->next;
        } else {
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }

    if (list1 != NULL) {
        current->next = list1;
    } else {
        current->next = list2;
    }

    return dummy.next;
}
