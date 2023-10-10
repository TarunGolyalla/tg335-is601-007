<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Tarun Goud Golyalla (tg335)</td></tr>
<tr><td> <em>Generated: </em> 10/10/2023 11:29:07 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/tg335" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.05.31image.png.webp?alt=media&token=290004f7-abd9-4f41-ae07-b0485be0f898"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function code on add task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.07.13image.png.webp?alt=media&token=ce1058d6-2b5b-4c53-b345-96b67f5763f6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and Failure in the same pic <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>In the add_task function, the code first checks that the provided name, description,<br>and due date are not empty. If any of them are missing, it<br>prints an error message and rejects adding the task. If all data is<br>present, it creates a new task based on the TASK_TEMPLATE and updates lastActivity<br>with the current datetime. It then attempts to convert the due date string<br>to a valid datetime format and catches any conversion errors. If successful, it<br>adds the new task to the tasks list and confirms this with a<br>message. Finally, it ensures the changes are saved to a JSON file using<br>the save() function.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.08.58image.png.webp?alt=media&token=6b604a4c-365d-4051-aead-d9793f0d6cc9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function code update logic <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>The process_update function takes an index as input, checks if it&#39;s within the<br>valid range of tasks, and prompts the user for updated task information. It<br>displays the existing values of each property (name, description, and due date) as<br>placeholders in the input prompts. If the index is valid, it then calls<br>the update_task function with the updated data to modify the task. If the<br>index is out of bounds, it notifies the user that the task does<br>not exist. This function allows for user-friendly updates of task details based on<br>the selected index.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.10.45image.png.webp?alt=media&token=c855cec9-bf4f-4c8d-ae77-653f736ba1ad"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function code for update task logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.12.48image.png.webp?alt=media&token=3cbc80e4-8807-4d56-b9af-f7bda7fcb8e4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and Failure in the same pic <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>The update_task function modifies a task&#39;s properties based on the provided index. It<br>first checks if the index is valid within the task list. If valid,<br>it updates the task&#39;s name, description, and due date with new values if<br>provided; otherwise, it retains the original values. The function also updates the task&#39;s<br>lastActivity with the current datetime. It prints a message confirming the update if<br>any changes were made to the task properties; otherwise, it indicates that no<br>updates were made.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.13.47image.png.webp?alt=media&token=4c851739-9188-44cf-9d36-18ffc0cbf17b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function code on mark task done <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.16.22image.png.webp?alt=media&token=e73a8d3c-1deb-4ecd-b4ee-b84ab028333d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.16.54image.png.webp?alt=media&token=eb1020f3-424a-4516-92aa-c21d0f0bf3eb"/></td></tr>
<tr><td> <em>Caption:</em> <p>It already has been done<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>The mark_done function marks a task as done by updating its &quot;done&quot; property<br>with the current datetime if it&#39;s not already marked as done. It checks<br>if the index is valid, handles out-of-bounds scenarios, and prints a completion message<br>accordingly. The function also ensures that the changes are saved to a JSON<br>file.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.20.28image.png.webp?alt=media&token=ea87ba13-5a0a-487c-95ba-d167e2ed8c68"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function for view task logic <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.22.44image.png.webp?alt=media&token=027f4b7d-5ef6-47bc-85f4-b16d1da3b3fa"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.23.15image.png.webp?alt=media&token=5724ff19-0163-44bb-8afd-777443f1a2e3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.25.48image.png.webp?alt=media&token=5b34d201-3f80-47b2-8edb-dcefdaceac20"/></td></tr>
<tr><td> <em>Caption:</em> <p>All the tasks <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.27.17image.png.webp?alt=media&token=7631cda8-721e-4436-85c5-ae78caf54139"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function code for delete task <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.28.18image.png.webp?alt=media&token=d0854ebe-d485-4a04-b884-edd80348db86"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and Failure in the same screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>The delete_task function removes a task from the tasks list based on the<br>provided index, displaying a message indicating success or failure. It also handles out-of-bounds<br>index scenarios and ensures that the changes are saved to a JSON file.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.30.53image.png.webp?alt=media&token=c691521d-826d-4c59-88b2-1e2ec16b0559"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.32.19image.png.webp?alt=media&token=dc9ebe67-efd7-4dbf-b9e4-ba7658c878d1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.32.54image.png.webp?alt=media&token=6a09d0cb-2fd3-44f8-bd3b-52dc4cd903b8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>The get_incomplete_tasks function generates a list of tasks that are marked as incomplete<br>(where the &quot;done&quot; property is set to False). It then passes this list<br>of incomplete tasks to the list_tasks function to display a summary view of<br>those tasks. This function effectively lists all tasks that have not been marked<br>as done, providing a quick overview of pending tasks. It includes a comment<br>with the UCID and the date when it was implemented.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.33.34image.png.webp?alt=media&token=f6b09fae-fbca-4edb-9947-c378b0822b80"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function code for over due tasks <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.35.20image.png.webp?alt=media&token=f55e5fd5-8697-4af9-9242-c51fc93a61ab"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.35.48image.png.webp?alt=media&token=374da2a1-4d4e-4cf9-8ff7-145179526aea"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>The function get_overdue_tasks() identifies and displays tasks that are overdue for completion, specifically<br>those tasks that are not yet completed and have a due date that<br>has already passed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.37.17image.png.webp?alt=media&token=fb21fd24-ee9c-4ca0-9121-c85dc95c05aa"/></td></tr>
<tr><td> <em>Caption:</em> <p>Function code on get time remaining code <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.40.00image.png.webp?alt=media&token=6eb6b398-d38a-4e54-a91a-75046478fc4a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success and failure in same screenshot <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>The function <code>get_time_remaining(index)</code> checks the validity of the provided task index. If valid,<br>it calculates the time difference between the current moment and the task&#39;s due<br>date. The function then breaks down this time difference into days, hours, minutes,<br>and seconds, creating a human-readable format. Depending on whether the task is overdue<br>or not, it prints either the time remaining until the task&#39;s due date<br>or the time since it became overdue. After the function, there&#39;s an unrelated<br><code>command_list</code> containing potential task management commands.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.42.21image.png.webp?alt=media&token=70b52c72-e9ea-4f84-83b9-c30b862dd6b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.42.47image.png.webp?alt=media&token=3eaaa0a0-fe00-4165-9bf9-2b37bb0fdbe9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.43.20image.png.webp?alt=media&token=c805bac4-fde7-474d-a78f-2ed6af560440"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.44.12image.png.webp?alt=media&token=9f176cb7-5f5c-47ae-9e0f-930fc081305e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.44.34image.png.webp?alt=media&token=273761f8-c0a3-430e-b690-f96e19680fd9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-10-10T05.45.39image.png.webp?alt=media&token=ad060865-30a9-476e-99c6-81f8a120a81b"/></td></tr>
<tr><td> <em>Caption:</em> <p>JSON file <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>I have not faced any problems while doing this mini project 1.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/TarunGolyalla/tg335-is601-007/pull/4">https://github.com/TarunGolyalla/tg335-is601-007/pull/4</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/tg335" target="_blank">Grading</a></td></tr></table>