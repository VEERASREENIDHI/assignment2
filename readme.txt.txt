TEAM DETAILS:

*VEERA SREENIDHI.R                  1KS18CS113
*KRITHIKA K.N                       1KS18CS034
*SUBRAMANYA                         1KS18CS100

TEAM CONTRIBUTION:

*VEERA                           LOGIC AND DEBUGGING FOR BETTER CODE
*SUBRAMANYA                      CODE MODIFICATION
*KRITHIKA                        LOGIC AND CODING

INSTRUCTIONS:

*First after compiling,we shud attatch a file,as we have generally given as a command.
*after the file attatchment with the input,we run it.
*For the inputs,we shud enter both positive and negative numbers.
*After we run the program we get the sum.

DETAILS ON EXAMPLE INVOCATION AND OUTPUT:

*Input: 2,-3,1.5,-1,3,-2,-3,3
*Output: (1.5,-1,3)=3.5

CHALLENGES FACED:

*Providing effecient solution.
*Writing better codes.
*Decoding when errors found.
*Coding in recurrsion was very challenging...wherein iterative was manageable.

LEARNT FROM ASSIGNMENT:

*Effective coding.
*Logical thinking.
*Recurrsion concept.

LOGIC OF THIS PROGRAM DONE

* This is based on the concept of Divide and Conquer.
*Firstly we need to divide the array into 2 halves.
as we are told to use recurrsion,there are oly three possible ways to make the code reccursive.
 *return the maximum of following 
a) maximum subarray sum is left half,recurrsive call shud be made.
b) maximum subarray sum in right half,then make a reccrsive call
c)maximum subarray sum such that the subarray crosses the midpoint.
   the main logic of this code is to find maximum sum wchis is starting from mid+1.it shud also end with sum point on right of mid+1.
 We then habe to combine both the two halves and return.
Hence this is the main idea we udes to implement our code.