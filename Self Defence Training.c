#include <stdio.h>

int main(void) {
	// your code goes here
	int t,i; 
	scanf("%d",&t);
	while(t--){
	    int n,count=0;
	    scanf("%d",&n);
	    for ( i =0; i<n; i++){
	        int a;
	        scanf("%d",&a);
	        if(a >= 10 && a <= 60)
	            count++;
	    }
	    printf("%d\n",count);
	}
	return 0;
}
