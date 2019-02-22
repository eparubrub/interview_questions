# interview_questions
These are my solutions to interview questions that I have gotten and the things I learned from them. I would like to thank all the people who gave me these interviews as they gave me a better understanding on how to problem solve and approach these types of questions. 

## palindrome_rearranging

### The thought process
For this program, I was asked to create a function that would receive an input string and return a boolean that indicated whether or not the input string could be rearranged into a boolean. My first approach and thoughts went straight to thinking about how to make the function work. That is how I usually prioritize my approaches. Make it work -> Make it efficient -> Make it clean. My initial thought was to rearrange the string into every single way possible and check whether or not it was a palindrome. Of course, it was not efficient in any way possible but it was the only logical solution I could come up with on the spot. From there, I created a helper function to check if the string was a palindrome. At some point, I was asked more questions, did a bit more coding, and stopped. After the interview, I was pretty adamant about solving the problem for future reference and I came to the realization that there was a pattern in palindromes. I found that there could be an infinite amount of occurrences of a character so long as the amount was even. On the other hand, there could be only one character that had an amount that was odd. From there I wrote up this solution.

### What I learned
I learned that I should take more time into understanding the nature of the problem before I take a deeper dive. In this case, I only understood palindromes for what they were and jumped to coding a bit too fast. Next time I should take more time in the interview to FULLY understand all problems and all variables, like palindromes, in order to have a better approach. 
