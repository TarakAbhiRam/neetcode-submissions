class MinStack {
private:
    stack<int> stk;
    stack<int> mini;
public:
    
    MinStack() {}
    
    void push(int val) {
        stk.push(val);
        if (mini.empty()){
            mini.push(val);
        }
        else{
            val = std::min(val,mini.top());
            mini.push(val);
        }
    }
    
    void pop() {
        stk.pop();
        mini.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return mini.top();
    }
    
};
