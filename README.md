## Optimal Spacing Program
Problem:  
For “N” linearly arranged discrete spaces, place incoming placeholders in such a way that each of the 
object to be placed maintain maximum possible spacing between its laterals, without replacing those 
who has already been placed in other discrete spaces.  

The Urinal Problem in Mathematics:  
Imagine there are “n” urinals in a washroom. If one person is to choose one of the urinals from “n” unoccupied urinals, he will probably choose any 
of the urinals. But since a new person could enter the washroom and choose a urinal from either side 
of him, it would be wise of him to choose urinal at the end, to reduce the chance of next incoming 
person choosing a urinal in his proximity. The second person should also choose a urinal farthest from 
the one the first person has chosen. Similarly, if the first two person choose the urinals at the end, the 
third person would most likely choose the urinal in the middle. This pattern of choosing the urinal 
continues most of the time or, at least this pattern is an extreme case that is possibly a 100% 
possibility when all the incoming persons are equally vigilant of their privacy. For example, in banks, 
people would love to stay as apart as possible from other customers. They would feel safer talking 
about transactions. Also, it could help prevent distractions from other customers in the row if they are 
spaced optimally. So, why not use this Urinal Problem in Mathematics in systems that could have the 
following implications?

Note: Our Optimal Spacing Program is the extreme case of the Urinal Problem in Mathematics 
because we are only concerned about maximizing privacy.  

Implications:  
The algorithm developed in response to the generic problem could be used for multiple purposes.  
1. Management of parking system to maintain proper spacing between cars and bikes, to allow 
them more ease and convenience while parking and moving out. It will prevent congestion.  
2. Could be used in libraries for maintaining distance optimum distance between readers
3. It could be used in exams for incoming students. Not only will it help maintain spacing 
between incoming students in the exam hall but will also possibly spread-out students who 
are likely to come along in a group to cheat in an exam. 
4. Could be used at counters in Banks, US Visa offices, social security offices etc. 
5. It could be used in cinema theaters after some modifications in the code. 
6. It could be used in metro washrooms, public toilets 
7. It could be used in  
8. Particle Placement in Experiments: In experiments involving particles or ions, such as in 
particle accelerators or ion traps, we could use our algorithm to optimize the spacing between 
particles to minimize interactions or collisions, improving experimental accuracy. It can 
further reduce any possibility of cross continuation, while also making most use of the spaces. 

Algorithm: 
Core part of the program:  
1. The program has two core modules 
2. One module interacts with the user, fetching input whether to do the following:
   - Assign a new seat
   - If any occupied seats have been emptied?
   - Empty an occupied seat?
   - Handle wrong inputs 
4. The other module will make logics to figure out the best seat. 
   - It will use the record of occupied and unoccupied seats to return the best seat  
     - If two or more best seats are possible, it will call for another function that will select  
       the best of the best seats. 
 
Explaining the module that calculates the best seat: 

- This algorithm aims to find the "best" available counter by selecting the one that is 
farthest from any already occupied counter, ensuring maximum spacing between 
people or items. Here's how it works in a more intuitive way:
- If no counters are filled yet, it returns to the first available counter because no 
spacing is needed. But when some counters are already filled, the algorithm 
compares each unfilled counter to the nearest filled counter. The goal is to pick 
the counter that keeps the most distance from the others. 
- For each unfilled counter, it checks how far it is from the closest filled counter. If 
the counters are in a straight line (linear), it measures the direct distance between 
them. If the counters are arranged in a circle, it also considers the wrap-around 
distance (e.g., from the last counter back to the first) to ensure accurate spacing in 
both directions.
- Once it finds a counter with the biggest minimum distance from the filled ones, it 
marks that as the best choice. If several unfilled counters are equally far from the 
filled ones, they all become candidates. The algorithm’s job is to ensure that 
whichever counter is chosen provides the most space possible, helping to avoid 
clustering and ensuring maximum separation.



