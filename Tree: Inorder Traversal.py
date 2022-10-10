void inOrder( struct node *root) {

    struct node *head=root;

    if (head!=NULL) {

        inOrder(head->left);

        printf("%d ",head->data);

        inOrder(head->right);

    }

}
