import numpy as np
def gauss_seidel_calc(self,entries,epsilon,x1,x2,x3):
        a=np.zeros((3,3+1))
        k=0
        iterations='i \t x1 \t\t x2 \t\t x3 \t\n'
        for i in range(3):
            for j in range(3+1):
                try:
                    a[i][j]=float(entries[k])
                    k+=1
                except:
                    self.popupmsg("Please Insert Numerical Values In All Spaces!")
        x0,y0,z0=0,0,0
        iterations += '%d \t [%.6f \t %.6f\t %.6f]\n' % (0,x1,x2,x3)
        x1,x2,x3=0,0,0
        for i in range(1,51):
            x1=(a[0][3]-a[0][1]*x2-a[0][2]*x3)/a[0][0]
            x2=(a[1][3]-a[1][0]*x1-a[1][2]*x3)/a[1][1]
            x3=(a[2][3]-a[2][0]*x1-a[2][1]*x2)/a[2][2]
            e1=abs((x1-x0)/x1)
            e2=abs((x2-y0)/x2)
            e3=abs((x3-z0)/x3)
            x0,y0,z0=x1,x2,x3
            if e1<epsilon and e2<epsilon and e3<epsilon:
                break
            iterations += '%d \t [%.6f \t %.6f\t %.6f]\n' % (i,x1,x2,x3)
        return iterations
def gauss_elimination_calc(self,entries,n):
        a=np.zeros((n,n+1))
        k=0
        for i in range(n):
            for j in range(n+1):
                try:
                    a[i][j]=float(entries[k])
                    k+=1
                except:
                    self.popupmsg("Please Insert Numerical Values In All Spaces!")
        for i in range(n):
            for j in range(i+1, n):
                ratio = a[j][i]/a[i][i]
                
                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
        x = np.zeros(n)
        x[n-1] = a[n-1][n]/a[n-1][n-1]

        for i in range(n-2,-1,-1):
            x[i] = a[i][n]
            
            for j in range(i+1,n):
                x[i] = x[i] - a[i][j]*x[j]
            
            x[i] = x[i]/a[i][i]
        return x
