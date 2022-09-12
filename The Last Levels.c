#include <stdio.h>

int main(void) {
	// your code goes here
	int t,total=0,divi=0;
	scanf("%d",&t);
	while(t--){
	    int x,y,z;
	    scanf("%d %d %d",&x,&y,&z);
	    if(x <= 3)
	        printf("%d\n",x*y);
	   else{
	        int sum = (x*y);
	        divi = x/3;
	        total = x - divi*3;
	        if(total == 0){
	            printf("%d\n",(divi-1)*z + sum);
	        }
	        else printf("%d\n",divi*z+sum);
	   }
	}
	return 0;
}
