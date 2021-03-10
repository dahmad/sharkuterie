# Sharkuterie

A charcuterie board is a platter of perserved foods chosen for their complementary flavors that is carefully presented in an aesthetically pleasing way.

A shark is an apex predator famous for its ability to chomp pieces from large prey.

These are some tools I use to iterate through random samples in an input MP3 to get a sense of where compelling samples may reside within the source material.

# Usage

`python3 main.py -i path/to/file.mp3 -b 400 -r 10`

Let's deconstruct this.

`main.py` is a script that accepts arguments. 

The `--input` (`-i`) flag specifies the source MP3.

The `--beat_length` (`-b`) flag specifies how long (in milliseconds) a quarter note will be.

The `--rounds` (`-r`) flag specifies how many iterations the script should produce before quitting.

When the script is invoked, we create a random sequence of beats for one measure. The sequences are currently limited to quarter notes or two successive eighth notes. I previously had half notes, triplet quarter notes, triplet eighth notes, and sixteenth notes, but I found that the output often sounded too chaotic.

With the random sequence of beats in the measure, we find random sections of the song for each beat. This is where the `-b` flag comes in. The default is 800ms. This corresponds to 75 bpm. This is an arbitrary choice--it just happened to work well with multiple inputs.

Once the sequence and samples are selected, we can render the output and play it back. Then, we wait for keyboard input. I type `1` and `Enter/Return` if I like the selection, which then gets exported to an mp3 where the timestamps (in milliseconds) of each sample are included in the filename. This helps me chase down these samples later.

# Coming Soon

I also have tools which allow me to capture quarter-note selections first before arranging them into measures, add a randomly-selected drum loop to play beneath the sample, and "pause" some selections within an measure to randomize out the parts I don't like. However, these are not in a good state.

I am also missing my unit tests. The architecture of my tests could use some love. The project layout in general leaves a lot to be desired. This is an active work in progress that is only a few weeks old as of March 2021.