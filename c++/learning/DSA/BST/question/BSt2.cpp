#include<iostream>
using namespace std;

struct Node{
    int data; Node *left, *right;
    Node(int value,Node* leftNode, Node* rightNode): data(value),left(leftNode),right(rightNode){}
};

Node* createNode(int value){
    return new Node(value, nullptr, nullptr);}

Node* insert(Node* root, int value){
    if (!root)return createNode(value);
    if (value < root->data) root->left= insert(root->left,value);
    if (value > root->data) root->right= insert(root->right,value);
    return root;
}

void inorder(Node* root){
    if(!root) return;
    inorder(root->left);
    cout<< root->data<<" ";
    inorder(root->right);
}
// le-ro-ri inn
// le-ri-ro poo
// ro-le-ri pre 

fn_ins:
    if x_ask="HASH":
       jump travesing; //B_Case

    no of child : x_ask
    for i in child :
        //ask to insert child  
        
return fn_ins 



int main(){
    Node* root = nullptr;
    int values[]={50,30,20,40,70,60,80};
    for(int value : values) root = insert(root,value);
    cout<<"inorder traversal of bst is :";
    inorder(root);
    return 0;
}