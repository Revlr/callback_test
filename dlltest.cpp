#include "dlltest.h"
#include <iostream>

using namespace std;

extern "C"{
__declspec(dllexport) void foo(void(*func_ptr)(int, int), int a, int b){
    cout << "run foo" << endl;
    func_ptr(a, b);
}

}
