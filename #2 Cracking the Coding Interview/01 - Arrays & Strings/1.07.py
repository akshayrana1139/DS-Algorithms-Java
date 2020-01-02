'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Can you do this in place?


123
456
789

1234
5678
1255

147->temp, left to temp
789->147,  bottom to left
369->789,  right to bottom
123->369,  top to right
temp->123, temp to top

4x4... work on first layer..
left: i=0,1,2; j=0,0,0
bottom: i=0,0,0; j=3,3,3
right: i=0,1,2; j=3,3,3
top: i=0,0,0; j=0,1,2


first = 0++ till n/2
last = n-1 -- till n/2

first = 0 
last = n-1
while(first<n/2 and last>n/2):

    arr[0:]
        

    last--
    first++

'''


