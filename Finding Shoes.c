#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int a,b;
	    scanf("%d %d",&a,&b);
	    if(a>b){
	        int sum = a-b;
	        printf("%d\n",sum+a);
	    }
	    else{
	        printf("%d\n",a);
	    }
	}
	return 0;
}
