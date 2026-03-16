class VM:
    PUSH,POP,ADD,SUB,MUL,DIV,MOD=0,1,2,3,4,5,6
    DUP,SWAP,PRINT=7,8,9
    JMP,JZ,JNZ=10,11,12
    HALT,STORE,LOAD=16,19,20
    def __init__(self): self.stack=[]; self.mem={}; self.out=[]
    def run(self, prog):
        ip=0
        while ip<len(prog):
            op=prog[ip]; ip+=1
            if op==self.PUSH: self.stack.append(prog[ip]); ip+=1
            elif op==self.POP: self.stack.pop()
            elif op==self.ADD: b,a=self.stack.pop(),self.stack.pop(); self.stack.append(a+b)
            elif op==self.SUB: b,a=self.stack.pop(),self.stack.pop(); self.stack.append(a-b)
            elif op==self.MUL: b,a=self.stack.pop(),self.stack.pop(); self.stack.append(a*b)
            elif op==self.DIV: b,a=self.stack.pop(),self.stack.pop(); self.stack.append(a//b)
            elif op==self.MOD: b,a=self.stack.pop(),self.stack.pop(); self.stack.append(a%b)
            elif op==self.DUP: self.stack.append(self.stack[-1])
            elif op==self.SWAP: self.stack[-1],self.stack[-2]=self.stack[-2],self.stack[-1]
            elif op==self.PRINT: self.out.append(self.stack.pop())
            elif op==self.JMP: ip=prog[ip]
            elif op==self.JZ: a=prog[ip]; ip+=1; (ip:=a) if self.stack.pop()==0 else None
            elif op==self.JNZ: a=prog[ip]; ip+=1; (ip:=a) if self.stack.pop()!=0 else None
            elif op==self.HALT: break
            elif op==self.STORE: a=prog[ip]; ip+=1; self.mem[a]=self.stack.pop()
            elif op==self.LOAD: a=prog[ip]; ip+=1; self.stack.append(self.mem[a])
        return self.out
if __name__ == "__main__":
    vm=VM(); V=vm
    prog=[V.PUSH,1,V.STORE,0,V.PUSH,10,V.STORE,1,
          V.LOAD,0,V.LOAD,1,V.MUL,V.STORE,0,
          V.LOAD,1,V.PUSH,1,V.SUB,V.DUP,V.STORE,1,V.JNZ,8,
          V.LOAD,0,V.PRINT,V.HALT]
    out=vm.run(prog)
    print(f"10! = {out[0]}")
    assert out[0]==3628800
    print("All tests passed!")
