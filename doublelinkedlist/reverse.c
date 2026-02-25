// struct node *reverse(struct node *head)
// {
//     struct node *current = head;
//     struct node *temp = NULL;
//     if(head = NULL)
//     {
//         return NULL;

//     }
//     while(current != NULL)
//     {
//         temp = current -> prev;
//         current -> prev = current -> next;
//         current -> next = temp;
//         current = current -> next;
//     }
//     if(temp != NULL)
//     {
//         head = temp -> prev;
//     }
//     return head;
// }