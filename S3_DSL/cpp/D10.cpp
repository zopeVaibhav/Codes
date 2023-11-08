#include <iostream>
using namespace std;
int stack[100], n = 100;
int top = -1;
void push(int val){
    if (top >= n - 1)
        cout << "stack overflow" << endl;
    else{
        top++;
        stack[top] = val;
    }
}
void pop(){
    if (top <= -1)
        cout << "stack underflowed" << endl;
    else{
        cout << "the popped element is " << stack[top] << endl;
        top--;
    }
}
void display(){
    if (top >= 0){
        cout << "stack elements are:";
        for (int i = top; i >= 0; i--){
            cout << stack[i] << "";
            cout << endl;
        }
    }
    else
        cout << "stack is empty";
}
void isfull(){
    if (top >= n - 1)
        cout << "stack is full" << endl;
    else
        cout << "stack is not full" << endl;
}
void isempty(){
    if (top <= -1)
        cout << "stack is empty" << endl;
    else
        cout << "stack is not empty" << endl;
}
int main()
{
    int ch, val;
    do{
        cout << "1. push in stack" << endl;
        cout << "2. pop in stack" << endl;
        cout << "3. display in stack" << endl;
        cout << "4. check if stack is full" << endl;
        cout << "5. check if stack is empty" << endl;
        cout << "6. exit" << endl;
        cout << "enter the choice:" << endl;
        cin >> ch;
        switch (ch){
        case 1:
        {
            cout << "enter the value to be pushed:" << endl;
            cin >> val;
            push(val);
            break;
        }
        case 2:
        {
            pop();
            break;
            }
        case 3:
        {
            display();
            break;
        }
        case 4:
        {
            isfull();
            break;
        }
        case 5:
        {
            isempty();
            break;
        }
        case 6:
        {
            cout << "exit" << endl;
            break;
        }
        default:
        {
            cout << "invalid choice" << endl;
        }
        }
    } while (ch != 6);
    return 0;
}