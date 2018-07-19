def solution(A):
    SymbolStack = [] 
    PositionStack = []
    CurrentPosition = 0

    for i in A:
        if i == "{":
            SymbolStack.append(i)
            PositionStack.append(CurrentPosition)
        elif i == "}":
            if len(SymbolStack) > 0 and SymbolStack[-1] == "{":
                SymbolStack.pop()
                PositionStack.pop()
            else:
                return CurrentPosition
        CurrentPosition += 1
    
    if not SymbolStack:
        return -1
    else: 
        return PositionStack[0]