#include <iostream>
using namespace std;

struct Node{
    int data;
    Node* next;
    Node(int data, Node* next=NULL){
        this->data = data;
        this->next = NULL;
    }
};

int main(){
    struct Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);

    int n=0; 
    
    Node *cur = head;
    while(cur){
        cout << cur->data<<" ";
        cur = cur->next;
    }
    return 0;
}