<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Tarun Goud Golyalla (tg335)</td></tr>
<tr><td> <em>Generated: </em> 12/11/2023 1:52:27 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/tg335" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T18.43.421a.png.webp?alt=media&token=86cabf68-1af7-42e9-a0d9-29ebe2a6bb7c"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot depicting html page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T18.47.091b.png.webp?alt=media&token=581c7556-bee0-44df-9451-fec04ff63b9a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code changes made<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T18.49.272a.png.webp?alt=media&token=df2ed41b-5137-4beb-9e8a-f5fb56fb3c44"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updating the Navigation bar in the file with ucid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T18.52.522b.png.webp?alt=media&token=7b08e80e-a9e5-4a40-accd-cce6139b09fc"/></td></tr>
<tr><td> <em>Caption:</em> <p>full code with replacement<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T18.56.363a.png.webp?alt=media&token=1b3b8446-d136-4b95-b9f6-b06fdf853506"/></td></tr>
<tr><td> <em>Caption:</em> <p>Imported csv file and checked for data uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T19.07.474b.png.webp?alt=media&token=1dbdba75-ecbf-4602-a68b-9e1ebd5275b0"/></td></tr>
<tr><td> <em>Caption:</em> <p>View of created fields <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T19.08.314.png.webp?alt=media&token=5e8f1202-ca50-48ac-8e3e-27852ddc9426"/></td></tr>
<tr><td> <em>Caption:</em> <p>outputhtml shown below with the fields mentioned<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T19.59.445a.png.webp?alt=media&token=43669176-ebd3-477a-bb84-bf10485de213"/></td></tr>
<tr><td> <em>Caption:</em> <p>Retreiving all the fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.02.055b.png.webp?alt=media&token=b0df1dea-f7ca-4f2f-84b7-940dbae2b314"/></td></tr>
<tr><td> <em>Caption:</em> <p>search 7,8,9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.09.315c.png.webp?alt=media&token=7499adc0-b17c-465b-9ee6-44b35060003f"/></td></tr>
<tr><td> <em>Caption:</em> <p>search 10,11,12<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.13.395d.png.webp?alt=media&token=5d3236fc-d971-4703-8cf8-5b425a9ad396"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add -1,2,3,4,5,6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.14.395e.png.webp?alt=media&token=a63154ef-c941-4336-b689-8f801ea2189f"/></td></tr>
<tr><td> <em>Caption:</em> <p>add 7,8,9,10,11<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.20.186a.png.webp?alt=media&token=86cb357f-3392-45b5-b57c-559ee89337eb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donations edit mode<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.20.546b.png.webp?alt=media&token=75d0e0cf-a502-4358-9a05-9771d28bab96"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit mode donations adding<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.26.516c.png.webp?alt=media&token=ccf6c9b5-f0a1-462d-8ffd-2f015e974f29"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.29.256d.png.webp?alt=media&token=be949c79-e622-4667-a7cc-68a246cc0abf"/></td></tr>
<tr><td> <em>Caption:</em> <p>website perspective<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.33.456e.png.webp?alt=media&token=433c85fb-0856-4d57-b900-79f576e87afb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Web browser view creation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.35.587a.png.webp?alt=media&token=8dd804a2-7251-4a1a-a6f5-ad638756dddf"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit view <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.37.397b.png.webp?alt=media&token=7e2f287d-cb1b-402d-9b89-a3c433c8e697"/></td></tr>
<tr><td> <em>Caption:</em> <p>view<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.40.457c.png.webp?alt=media&token=d8ef2c1c-368e-4efe-a023-0874a5f14d32"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search view from browser<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.50.337d.png.webp?alt=media&token=87831386-0171-43b1-9555-14a433ec776f"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.51.027e.png.webp?alt=media&token=9a7c07ea-fc69-4883-9443-49a070825b50"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.51.497f.png.webp?alt=media&token=04eb427d-0adf-4967-9927-0b02f58ecd61"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.54.157g.png.webp?alt=media&token=bddeaa01-a28f-42ad-bd19-13d2a6fbb7fe"/></td></tr>
<tr><td> <em>Caption:</em> <p>add- 1,2 ,3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.54.307h.png.webp?alt=media&token=7720c5f4-c7cd-44a0-803a-2ee91511d8dc"/></td></tr>
<tr><td> <em>Caption:</em> <p>4,5,6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T20.54.407i.png.webp?alt=media&token=f6b28b76-a23a-4bea-a330-996a62a1ca74"/></td></tr>
<tr><td> <em>Caption:</em> <p>7,8,9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T21.00.558a.png.webp?alt=media&token=7a90be7a-acf3-4512-ad74-2a401d211e4c"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T21.02.188b.png.webp?alt=media&token=8a18df67-77bf-40df-a386-b3b81acfccbc"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T21.03.228c.png.webp?alt=media&token=2f858a7e-52da-4012-9aea-19af919ea5ec"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T21.03.398d.png.webp?alt=media&token=ed55d6a0-8bac-4264-a34c-4a0f733382d0"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T21.08.289b.png.webp?alt=media&token=775e5a7d-f48d-4b9c-a786-82dcef213cdb"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete route code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T21.20.26t1.png.webp?alt=media&token=ea91632a-4c6c-4566-91c7-28c411e151ca"/></td></tr>
<tr><td> <em>Caption:</em> <p>sub task 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T21.21.04t2.png.webp?alt=media&token=96a1c539-c336-409f-a9c8-7a63136da23e"/></td></tr>
<tr><td> <em>Caption:</em> <p>sub task 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T21.21.34t3.png.webp?alt=media&token=9be023ed-35ce-4038-a9d2-5c07ffe56a4f"/></td></tr>
<tr><td> <em>Caption:</em> <p>sub task 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-11-29T21.22.01t4.png.webp?alt=media&token=05e6de9b-c07f-4329-b1a8-3f515d3950e5"/></td></tr>
<tr><td> <em>Caption:</em> <p>sub<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>Yes, all the passed successfully.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/TarunGolyalla/tg335-is601-007/pull/15">https://github.com/TarunGolyalla/tg335-is601-007/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-11T18.49.35commit%20msg%20ss.png.webp?alt=media&token=0906f817-6541-4396-96b1-b5f8211eea9d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Commit <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-11T18.51.312a.png.webp?alt=media&token=a623852d-231e-4405-8088-c89d60d9978f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Dashboard<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-tg335-prod-4626440d54b8.herokuapp.com/">https://is601-tg335-prod-4626440d54b8.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/tg335" target="_blank">Grading</a></td></tr></table>
