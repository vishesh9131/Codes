// short code pro level
#include <iostream>
template <typename T>
class Queue
{
private:
    struct Node
    {
        T data;
        Node* next;
        Node(const T &value):data(value),next(nullptr){}
    };
    Node *frontNode, *rearNode;
public:
    Queue(): frontNode(nullptr),rearNode(nullptr){}
    void enqueue(const T &value){
        Node* Newnode= new Node(value);
        rearNode?rearNode=rearNode->next=Newnode : frontNode=rearNode=Newnode;
    }
    void dequeue(){
        // frontNode? Node* temp=frontNode; 
        // frontNode=frontNode->next; delete temp;
        if (frontNode)
        {
            Node* temp = frontNode;
            frontNode = frontNode->next;
            delete temp;
        }
    }
    ~Queue(){
        while (frontNode)
        {
           Node* temp = frontNode;
           frontNode=frontNode->next;
           delete temp;
        }
        
    }
    T front ()const 
    {
        return frontNode? frontNode->data : T();
    }
    size_t size() const{
        size_t count = 0;
        for(Node* current=frontNode; current!=nullptr; current=current->next, ++count);
        return count;
    }

    T display() const


    bool isEmpty()const{
        return !frontNode;
        // return (frontNode == nullptr);
    }

};
int main(){
    Queue<int> MQ;

    MQ.enqueue(1);
    MQ.enqueue(34);
    std::cout<<MQ.front()<<std::endl;

    // std::cout << "Is the queue empty? " << (myQueue.isEmpty() ? "Yes" : "No") << std::endl;
    // myQueue.dequeue();
}