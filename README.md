# Coding Challenge Websites

This repository contains various challenges that I have worked through in order to increase my skills in Data Structures as well as programming in general. You will see that the branches have been divided up by Website as well as language to make things easier to follow.

As not to ocupy too many repositories with "tutorials" I've decided to group them into a single repository by making use of the `git`'s *`orphan`* command - allowing you to have independent branches with their own independant `git` history.

# Tutorials Completed

The branches, i.e. Coding Challenge Website, with the respective langauges are as follows:  
1. [Hacker Rank - C++](https://github.com/BenWolfaardt/Coding_Challenge_Websites/tree/01-Hacker_Rank-C+%2B)
<!-- 2. []()
3. []()
4. []()
5. []()
6. []()
7. []()
8. []()
9. []()
10. []() -->

---

# `git checkout --orphan BRANCHNAME` 

The following is an approach to implement **monorepos** as found [here](https://stackoverflow.com/questions/14679614/is-there-a-way-to-put-multiple-projects-in-a-git-repository#14680329).

> Please note that this isn't actually a "monorepo" rather, as stated above, I'm using it to have multile projects in the same repository.

1. Create a new branch for your "new" tutorial.

   > `git checkout --orphan <branch_name>`

    This creates a new branch, unrelated to your current branch. Each project should be in its own orphaned branch.

2. Write your code / do your tutorial
3. Commit your code 

   > git commit -m "Tutorial x comleted"

4. Push your code 

   > git push --set-upstream origin <branch_name>

5. Cleanup local directory

    `rm .git/index`  
    `rm -r *`

   > `git` needs a bit of a cleanup after an `orphan "checkout"`.  

   > **IMPORTANT**: ensure that you commited before performing the previous task.

6. Checkout a new branch to perform the next tutorial

   > `git checkout --orphan <new_branch_name>`

7. Step 5. often needs to be repeated here

     `rm .git/index`  
     `rm -r *`

   > Ensure that you have a blank working directory when starting a new tutorial and that nothing is staged for `git`.  
   > Ensure that the `.git` file is still in the directory.  

   > Follow on from Step 2

# TODO

* // TODO: practice more;  

# Other Website

The list of below websites was extracted from [here](https://www.freecodecamp.org/news/the-10-most-popular-coding-challenge-websites-of-2016-fb8a5672d22f/) - giving a summary of what each site is known for.

* [TopCoder](https://www.topcoder.com/challenges/?pageIndex=1)
* [Coderbyte](https://www.coderbyte.com/)
* [Project Euler](https://projecteuler.net/)
* [CodeChef](https://www.codechef.com/)
* [Exercism.io](https://exercism.io/)
* [Codewars](https://www.codewars.com/)
* [LeetCode](https://leetcode.com/)
* [SPOJ](http://www.spoj.com/)
* [CodinGame](https://www.codingame.com/)
