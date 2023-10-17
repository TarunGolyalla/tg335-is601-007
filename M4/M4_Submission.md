<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Tarun Goud Golyalla (tg335)</td></tr>
<tr><td> <em>Generated: </em> 10/16/2023 11:12:02 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/tg335" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-16T20.38.02caladd1.png.webp?alt=media&token=5e74f465-0065-4d44-b510-751a413ae5e2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Addition Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-16T20.38.58calsub.png.webp?alt=media&token=3fc119ec-075a-4fc6-ae73-5c62f0cbede1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-16T20.39.48calmul.png.webp?alt=media&token=462d2fac-3859-4ad4-99f5-4c7cd9df5ece"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-16T20.41.56caldiv.png.webp?alt=media&token=22e0fb99-3ab2-4a52-99bd-3035bf87be2c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division function that handles Zeros<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-17T02.46.50Screenshot%202023-10-16%20at%2010.46.43%20PM.png.webp?alt=media&token=7f96e2c2-0b5d-4f45-a6b4-c9cb50da3d4f"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-add-number Test Case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-17T02.47.59Screenshot%202023-10-16%20at%2010.47.52%20PM.png.webp?alt=media&token=caedad61-d27f-42b3-a29b-4fd1168162fc"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing ans-add-number Test Case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-17T02.48.30Screenshot%202023-10-16%20at%2010.48.24%20PM.png.webp?alt=media&token=ce84ea0e-a7fe-4aa3-9a6f-7ad956992f48"/></td></tr>
<tr><td> <em>Caption:</em> <p> passing number-sub-number Test Case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-17T02.49.17Screenshot%202023-10-16%20at%2010.49.13%20PM.png.webp?alt=media&token=1717f455-1ff9-4eec-a45e-c394ba370f36"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing ans-sub-number Test Case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-17T03.00.50Screenshot%202023-10-16%20at%2011.00.46%20PM.png.webp?alt=media&token=4ae9f086-a12e-4e8d-b3fb-517cb3d6585b"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing number-mult-number Test Case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-17T03.01.48Screenshot%202023-10-16%20at%2011.01.44%20PM.png.webp?alt=media&token=9020a53e-10fc-40b2-939f-451cd8956da9"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing ans-multi-number Test Case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-17T03.04.40Screenshot%202023-10-16%20at%2011.04.34%20PM.png.webp?alt=media&token=5d0dbd3d-be2e-449f-ac68-15537b32799c"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing number-div-number Test Case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-17T03.05.15Screenshot%202023-10-16%20at%2011.05.10%20PM.png.webp?alt=media&token=67eb9e00-448d-4294-94e9-e4f493ec2dd3"/></td></tr>
<tr><td> <em>Caption:</em> <p> passing ans-div-number Test Case<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I did get some error while working in this module. I resolved it.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;&nbsp;Through this assignment, I explored how test cases ensure code reliability, gaining insights<br>into pytest&#39;s fixtures for streamlined setup/teardown processes and the versatility of parameterized tests<br>for multiple input evaluations.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/TarunGolyalla/tg335-is601-007/pull/7">https://github.com/TarunGolyalla/tg335-is601-007/pull/7</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/tg335" target="_blank">Grading</a></td></tr></table>
