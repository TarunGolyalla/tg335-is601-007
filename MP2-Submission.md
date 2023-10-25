<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Pumpkins</td></tr>
<tr><td> <em>Student: </em> Tarun Goud Golyalla (tg335)</td></tr>
<tr><td> <em>Generated: </em> 10/25/2023 9:59:59 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/tg335" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4">https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4</a></li><li>Put them into a subfolder in your repository folder (I called my folder MP2)</li><li>Create a test folder as a subdirectory of MP2</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the below input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-23T21.42.48p1.png.webp?alt=media&token=4842a68f-ef8b-4abc-b131-9f0174a1bb4f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Calculating the proper value of cost<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>The code calculates the total cost of the in-progress pumpkin and sets the<br>total cost for the in-progress pumpkin.<div><br></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-23T21.49.18p2.png.webp?alt=media&token=adbbab42-9c79-43a4-bedf-2b9e4446ffe9"/></td></tr>
<tr><td> <em>Caption:</em> <p>out of stock exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-23T22.05.32p3.png.webp?alt=media&token=8a0454cb-544a-4574-8b68-3d8eb59a90f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>needscleaning exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-23T22.07.21p4.png.webp?alt=media&token=018ee7b8-cd9f-40e7-b415-8e7b6b5c7746"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalidchoiceexceptions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-23T22.09.19p5.png.webp?alt=media&token=6d183e51-d43b-442f-896e-eae696851c7b"/></td></tr>
<tr><td> <em>Caption:</em> <p>limit exceeded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-23T22.11.02p6.png.webp?alt=media&token=d16a4146-e2cf-4ae6-9465-c48ea805e25c"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid payment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div>When an item runs out, a `OutOfStockException` message appears. The message {NeedsCleaningException} appears<br>if the machine requires cleaning. The user is notified that they selected an<br>item that is not available on the menu by the {InvalidChoiceException}. {ExceededRemainingChoicesException} alerts<br>the user to the user that they selected an item in excess. Lastly,<br>should the user doesn't make the correct payment, the `InvalidPaymentException} notifies them of<br>their error mistake. Every one of these exclusions offers concise and easy-to-use feedback<br>to guarantee a seamless the way the pumpkin-making process works.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.37.59t1.png.webp?alt=media&token=8c2366de-4206-441e-be7a-6695ccbeda3d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case 1: Pumpkin selection<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.38.49t2.png.webp?alt=media&token=94cec6f9-efc1-4582-b107-5648ead35b39"/></td></tr>
<tr><td> <em>Caption:</em> <p>test case 2: only face stencils<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.39.26t3.png.webp?alt=media&token=d219fdba-8fc5-4fdc-933e-5db3a6d73d7e"/></td></tr>
<tr><td> <em>Caption:</em> <p>can add only if in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.39.42t4.png.webp?alt=media&token=d87b7461-9eda-4163-814e-5b0408f08b48"/></td></tr>
<tr><td> <em>Caption:</em> <p>can add upto 3 extras of face stencils<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.40.17t5.png.webp?alt=media&token=214b912c-601e-4a87-96a1-a319ddd6c989"/></td></tr>
<tr><td> <em>Caption:</em> <p>add upto 3 extras of any combo<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.40.56t6.png.webp?alt=media&token=fec65370-a3ae-40f7-96c1-3d7eed3aaa62"/></td></tr>
<tr><td> <em>Caption:</em> <p>cost calculation based on choices<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.41.30t7.png.webp?alt=media&token=705f34ba-016b-4182-b859-6448a2d7df22"/></td></tr>
<tr><td> <em>Caption:</em> <p>total sales <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.41.58t8.png.webp?alt=media&token=ad00c1f6-57a5-40f0-99b3-1296906a6969"/></td></tr>
<tr><td> <em>Caption:</em> <p>test 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.42.15t1-8.png.webp?alt=media&token=4c4fdc2b-6f4f-4e55-a68b-835e20c44d13"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing all tests<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>We're making sure you can't just pick your pumpkin and choose a face<br>stencil without first choosing it with the `test_pumpkin_first_selection'; if you try to do<br>so, the system will stop you with a `InvalidStageException'. Next, in "test_face_stencils_in_stock" as<br>well as 'test_extras_in_stock', we're assuming the part of an anxious customer, confirming that<br>the system won't allow you to select an additional face stencil or one<br>if it's already out of supply. Just think of the letdown if that<br>happened! The next step is `test_max_face_stencils' and 'test_max_extras', we are essentially gauging the<br>system's tolerance to ensure it alerts us to any issues. to end once<br>we've selected three extras or face stencils. I mean, we can't become avaricious.<br>The `test_calculate_cost' is primarily concerned with finances; we are ensuring that the system<br>bills us accurately, and as such, I've experimented with various shopping scenarios. Then<br>there's "test_total_sales", which makes sure the store records its overall revenue. Lastly, even<br>though the excerpt you provided did not go into specific detail,</div><div><br></div><div>Increments of "test_total_products"<br>It seems to be monitoring the total number of products in the store,<br>ensuring</div><div><br></div><div>Every purchase is accurately totaled.&nbsp;</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td>Not provided</td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Though I faced couple issues and delays whilst testing everything was fine and<br>went smoothly.<div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-24T17.45.43all%20outputs%20%20mp2.png.webp?alt=media&token=8e9119df-ef30-40d9-b31f-bd1be154482d"/></td></tr>
<tr><td> <em>Caption:</em> <p>outputs<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/tg335" target="_blank">Grading</a></td></tr></table>
