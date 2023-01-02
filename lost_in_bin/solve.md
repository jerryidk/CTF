
# Solved

Do the typical stuff, feed into decompiler. You will find something like this


<code> 

int main(int argc, char** argv)
{

  if( ptrace(0,0,0,0) != -1 ){
    
    // Fake flag
    if (argc < 5) {
      // ask for password
      // md5 encrypted input
    }

    // Real Flag

    // Get 4 args, which is the solution to system of linear equations
    // Grab the flag


  }else {
    // Fake flag
    // ask for password
    // md5 encrypted input
  }


  return 0;
}

</code>


<code>
  ptrace(0,0,0,0) == -1 
</code>

gdb will run ptrace on program upon start, thus ptrace call will fail in the user program causing branch to be taken differently. ( A neat trick ).


To get the flag, solve following system

<code>
    -24w - 18x - 15y - 12z = -18393
    18w + 18x + 9y - 9z = 4419
    16w + 12x + 4y + 2z = 7300
    -6w - 6x - 3y - 11z = -8613

    w = 227
    x = 115
    y = 317
    z = 510
</code>

finally, you can obtain the flag by input the above 4 numbers as command line argument.
