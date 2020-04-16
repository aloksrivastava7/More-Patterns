'''

Enter Height : 10

         **
        *  *
       *    *
      *      *
     *        *
    *          *
   *            *
  *              *
 *                *
*                  *
*                   *
 *                 *
  *               *
   *             *
    *           *
     *         *
      *       *
       *     *
        *   *
         * *

'''

#PROGRAM

n = int(input('Enter Height : '))
print()
for i in range(1,n+1):
    h = 1
    print(' '*(n-i)+'*',end = '')
    while h!=2*i-1:
        print(' ',end='')
        h = h + 1    
    print('*')
for j in range(0,n):
    print(' '*j+'*',end = '')
    for k in range(j,(2*n)-j-1):
        print(' ',end='')
    print('*')

    
    
    
    
    
