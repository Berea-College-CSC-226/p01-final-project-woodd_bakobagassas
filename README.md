# CSC226 Final Project

## Instructions

Exclamation Marks  ️indicate action items; you should remove these emoji as you complete/update the items which 
  they accompany. (This means that your final README should have no ❗️in it!)

**Author(s)**: David Wood, Sara Bako
 
**Google Doc Link**: https://docs.google.com/document/d/1CFn9LUzHUE3x_Se9GAdVWB8VejiQzqDdxyUdAuKnuOs/edit?tab=t.0

---

## Milestone 1: Setup, Planning, Design

️**Title**: Tic_Tac_Toe`

**Purpose**: `To play a simple game of tic tac toe with the computer.`

️**Source Assignment(s)**: `HW07: The Game of Nim. Well be using this for inspiration for the computer functionality; t11,t12nn. .`

️**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  
CRC cards 
![Screenshot 2025-04-28 101658.png](../../Pictures/Screenshots/Screenshot%202025-04-28%20101658.png)
![Screenshot 2025-04-28 102357.png](../../Pictures/Screenshots/Screenshot%202025-04-28%20102357.png)
![Screenshot 2025-04-28 104024.png](../../Pictures/Screenshots/Screenshot%202025-04-28%20104024.png)
![Screenshot 2025-04-28 110839.png](../../Pictures/Screenshots/Screenshot%202025-04-28%20110839.png)

️**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: woodd
    Branch 2 starting name: bakobagassas
```

### References 

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!

---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    So far we have done around 45% of game. We have written the methods and class for the first level and we have started
    to work on our test suite. We are feeling a little bit ahead because we have an idea of the additioanl methods that 
    need to be added. Furthermore, we are also coming up with ways to improve our game and make it more engaging. 
    Everything so far is working smoothing, we manage to communicate effectively and we have a good team dynamic therefore, 
    we don't really have much to worry out for now. We were surprised by how "easy" widgets can actually be if we properly 
    read about them to understand how they work. We are feeling quite confident and we hope it keeps going that way. 
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `75%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    We feel pretty confident about completing this project. Because we have done most of th work we needed to do and broke 
    down the rest of the assignment, we it is quite clear what still needs to be done. The strategy we will employ is keep 
    going with the same intensity even when we think that we are almnost done, to make sure that we don't suddenly get begin. 
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 

First, the user will have to choose a symbol/name as well as a color. Then the game officially starts. The user will always be playing first 
against the computer. The user places their symbol on a box followed by the computer. For the first level the computer 
is taking it easy and randomly places symbols. Who ever has their symbol placed in a whole rows/column/diagonal then they 
win. No matter who wins Level 1, the user will be asked if they want to move 
to the next level, same for level 2. Furthermore, when there is a tie, the user will also be asked if they want to reset in order to 
continue playing. 

### Errors and Constraints

Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

(done)

### Peer Evaluation

It is important that all members of your team contribute equitably. The peer evaluation is your chance to either 
a) celebrate the great work you all did together as an effective team, or b) indicate to the instructor if a member of
your team did not contribute their fair share. Grades will be adjusted for any team member who is evaluated poorly. Your
commit history will be used as evidence, so make sure you are using git effectively!

We think we both contribute equitably to the project. We were all invested, we were meeting often to talk and work and 
we were always communicating when we ran into issues. We are both really proud of our work!!

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Sara: I think we selected this project because it is a fun game that can also be instructive for both adults 
    and kids as it stimulate cognitive thinking since the player is constantly finding a way to place their symbol 
    in a strategic place in order to win. This game is what we wanted to do from the start, the only difference 
    is that we actually expanded it to the point that we personalized colors and symbols as well as the levels of difficulty. 
    
    I learned alot about classes during this project as well as inheritence because we started this project a few weeks 
    after we learned the topics. I also learned more about the GUI features because most of our code was about that, so 
    i spent quite a lot of time reading the documentation for GUI. 
    
    The hardest part I think was just to find and correct a bug related to our inheritance. When we created more 
    than one class, we had some bugs at first and we discoved it was because our window was distroyed in the reset 
    method hence when we were getting attributes related errors when we were ready to move on to the Second class. 
    A part from that I think the project went smoothly. Next time, I think I will try to test the full first Class 
    before moving on to the other classes to be sure that everything is okay so that I don't spend that much time 
    trying to figure out what is wrong. 
    
    I think I worked well with my partner. We were both communicating when needed and we were respectful of each other's 
    time. When it happened that we could not meet for a good reason, we told each other and we were understanding. So I 
    think what made it work is communication, respect for each other's time and work, understanding, as well as taking 
    ownership of our actions. 
```

```
    Partner 2:  
    ** We selected this project looking for something simple but not too easy. but once we got the ground level
    for the game we decided that we should add onto it by letting the player choose a color and their symbol. We also created
    a couple of other levels so that the game would get more difficult. Our final project looked completely different from
    what we originally had hoped for. Our original idea was just a basic tic tac toe game but we built upon that too increase
    the computers difficulty and to allow for more customization. I learned that communicating ideas and issues with your 
    partner, effectivley,  makes everything easier because its not just me being stuck on a loop of the same idea getting me
    nowhere.
    
    The hardest part of this project for me was getting everything to work together correctly. We both had somewhat different
    ideas that were for the most part the same thing. like i was trying to delete the window and make a new one for each level
    but that messed up with the level 2 so sarah informed me that deleting the window was messing it up so i made it where it passes
    all the stuff that needed to pass from the class level 2 into the window. We found issues with eachothers code and we talked
    it through and got things solved.
    
    I would talk more with my partner than i did this time. We talked enough to get what we wanted to get done but their were
    times where i thought i should of asked sarah something but i didnt. If i talked with her about my issue it probably would
    of gone smoother and with less of a headache. It would also help clear up any confusion and misunderstandings. like 
    when i was deleting the window; if i asked what we were doing exactly i would of tried to do it with out making a new 
    window from the beginning. But all in all i felt that we worked really well. Even though I felt that i should of communicated
    better with sarah i feel like we still worked really well together and communicated effectivly enough.**
```

---