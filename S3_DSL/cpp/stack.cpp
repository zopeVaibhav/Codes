// C++ program to reverse a string using stack
#include <bits/stdc++.h>
using namespace std;

class STACK {
public:
	int top;
	int size;
	char* array;
};

STACK* createStack(int size){
	STACK* stack = new STACK();
	stack->size = size;
	stack->top = -1;
	stack->array = new char[(stack->size * sizeof(char))];
	return stack;
}
int isFull(STACK* stack){
	return stack->top == stack->size - 1;
}

int isEmpty(STACK* stack) { return stack->top == -1; }

void push(STACK* stack, char item){
	if (isFull(stack))
		return;
	stack->array[++stack->top] = item;
}

char pop(STACK* stack){
	if (isEmpty(stack))
		return -1;
	return stack->array[stack->top--];
}

string reverse(string str){
	int n = str.length();
    // dynamic allocation
	STACK* stack = createStack(n);
    // push in stack
	for (int i = 0; i < n; i++)
		push(stack, str[i]);
    // pop of stack
	for (int i = 0; i < n; i++)
		str[i] = pop(stack);
    return str;
}

int main(){
	string str = "madam";
	cout << str << endl;
    string rev = reverse(str);
    cout << rev << endl;

    if(rev == str){
        cout << "Palindrome" << endl;
    }
    else    
        cout << "Not a Palindrome" << endl;


	return 0;
}
