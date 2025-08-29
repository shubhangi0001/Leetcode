class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(-1);      // Dummy head
        ListNode* current = &dummy;

        // Traverse both lists
        while (list1 && list2) {
            if (list1->val <= list2->val) {
                current->next = list1;
                list1 = list1->next;
            } else {
                current->next = list2;
                list2 = list2->next;
            }
            current = current->next;
        }

        // Attach remaining part
        current->next = (list1) ? list1 : list2;

        return dummy.next;
    }
};
