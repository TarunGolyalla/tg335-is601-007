<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Tarun Goud Golyalla (tg335)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 3:41:31 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/tg335" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <p>FOOTBALL API BETA - Getting the stats of football leagues, stats, and teams.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <div><pre class="code-highlighter" style="box-sizing: border-box; font-size: 12px; font-family: Inconsolata, Monaco, Consolas, &quot;Courier New&quot;, Courier,<br>monospace; margin-top: 0.5em; margin-bottom: 0.5em; overflow: hidden auto; padding: 1em; color: rgb(197, 200,<br>198); text-shadow: rgba(0, 0, 0, 0.3) 0px 1px; word-spacing: normal; background: transparent; direction:<br>ltr; word-break: break-all; line-height: 1.5; tab-size: 4; hyphens: none; border-radius: 0.3em; border-width: 0px;<br>overflow-wrap: anywhere;"><code style="box-sizing: border-box; font-family: Inconsolata, Monaco, Consolas, &quot;Courier New&quot;, Courier, monospace; text-wrap:<br>nowrap; word-break: normal; text-shadow: rgba(0, 0, 0, 0.3) 0px 1px; direction: ltr; word-spacing:<br>normal; line-height: 1.5; tab-size: 4; hyphens: none;"><span class="token" style="box-sizing: border-box; background: none !important;<br>color: rgb(168, 255, 96);">Endpoint -   '/timezone'</span></code></pre></div><b><div><b><br></b></div>The goal is to obtain a<br>roster of football teams.</b><div><b>Parameters: To filter the results, you can enter parameters such<br>as the name of the team, the nation, the league, etc.</b></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <div>"name": "Barcelona," "code": "BAR," "country": "Spain," "founded": 1899, team":&nbsp; &nbsp;"National": Untrue, The logo<br>can be found at https://media-4.api-sports.io/football/teams/529.png.</div><div>Regarding Football Teams:</div><div><br></div><div>ID:</div><div><br></div><div>Goal: An exclusive the football team's identity.</div><div><br></div><div>Use:<br>The database's primary key for group stats.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <div>Providing thorough information about football teams and the venues that are connected to<br>them is the main objective of the various entities (football teams). The application's<br>rich user experience is made possible by this information, which lets users do<br>the following:</div><div><br></div><div>design="font-size: 14px;"&gt;</div><div>Explore Teams: Users can look up and see comprehensive football team<br>information containing their logos, names, nations, and years of founding.</div><div><br></div><div>Management of Teams: Admins<br>can Football teams can be added, edited, and deleted to keep the application<br>up to date with the most recent data.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T19.21.45dv2%20a1.png.webp?alt=media&token=e3694645-e7f8-4f9d-83eb-5799b8bf3aeb"/></td></tr>
<tr><td> <em>Caption:</em> <p>create team page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T19.26.21dv2%20a2.png.webp?alt=media&token=6707964d-e775-429d-944c-a89f4e0d8bec"/></td></tr>
<tr><td> <em>Caption:</em> <p>added data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T19.33.28dv2%20a3.png.webp?alt=media&token=34052f58-30c2-48a7-aec5-25cbc49798a8"/></td></tr>
<tr><td> <em>Caption:</em> <p>added data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T19.34.43dv2%20a6.png.webp?alt=media&token=1291df70-2920-41cf-9736-f4ba261ff730"/></td></tr>
<tr><td> <em>Caption:</em> <p>new data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/TarunGolyalla/tg335-is601-007/pull/20">https://github.com/TarunGolyalla/tg335-is601-007/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T19.49.37dv3%20a1.png.webp?alt=media&token=8e3c9af4-c757-4c9d-9054-268f2d16b6a4"/></td></tr>
<tr><td> <em>Caption:</em> <p>records<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T19.49.59dv3%20a2.png.webp?alt=media&token=8bb8a25a-3b2c-434c-93be-df18b0864c3f"/></td></tr>
<tr><td> <em>Caption:</em> <p>records<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T19.50.41dv3%20a3.png.webp?alt=media&token=3472305a-a122-423a-8597-7c42b3024c0b"/></td></tr>
<tr><td> <em>Caption:</em> <p>records<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/TarunGolyalla/tg335-is601-007/pull/20">https://github.com/TarunGolyalla/tg335-is601-007/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T19.55.43dv4%20a1.png.webp?alt=media&token=d0e66b12-3622-4c87-9046-db293855f00b"/></td></tr>
<tr><td> <em>Caption:</em> <p>entity with details shown<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/TarunGolyalla/tg335-is601-007/pull/20">https://github.com/TarunGolyalla/tg335-is601-007/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T19.56.12dv5%20a1.png.webp?alt=media&token=202e915e-d601-4a4e-a42a-555d69e958fa"/></td></tr>
<tr><td> <em>Caption:</em> <p>team data edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T20.00.12dv5%20a2.png.webp?alt=media&token=a2928ae9-0034-4b61-9e6e-ca74af2bd9a1"/></td></tr>
<tr><td> <em>Caption:</em> <p>before and after ss<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T20.01.37dv5%20b1.png.webp?alt=media&token=30c8a129-0d5b-42a9-8f13-ba9e4317cd57"/></td></tr>
<tr><td> <em>Caption:</em> <p>before and after ss<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T20.02.00dv5%20b2.png.webp?alt=media&token=e328923d-d248-4cc6-965e-ed3e2a322693"/></td></tr>
<tr><td> <em>Caption:</em> <p>after ss<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/TarunGolyalla/tg335-is601-007/pull/20">https://github.com/TarunGolyalla/tg335-is601-007/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T20.03.11dv6%20st1.png.webp?alt=media&token=e684c28c-1d8a-48c2-83c9-0a972475c0dc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete should hold and pass the filter/sort criteria from the search page and<br>re-apply it upon direct like previous lessons have shown<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T20.04.28dv6%20st2.png.webp?alt=media&token=9dffa8b9-b35e-4b69-8b70-9145c2aad4a1"/></td></tr>
<tr><td> <em>Caption:</em> <p>database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/TarunGolyalla/tg335-is601-007/pull/20">https://github.com/TarunGolyalla/tg335-is601-007/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T20.05.42dv7%20st1.png.webp?alt=media&token=bc84b44a-2aa0-4ba7-b9cf-52c0bd73e4d1"/></td></tr>
<tr><td> <em>Caption:</em> <p>code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <div>User Input: When a user submits the team search form, the procedure is<br>initiated.</div><div>The name of the football team the user wishes to retrieve information about<br>is probably entered in an input field on this form.</div><div><br></div><div>Validating Forms: The form.validate_on_submit()<br>method condition verifies the form's contents and determines whether it has been submitted.<br>Should the form is valid; the procedure is carried out.</div><div><br></div><div>API Request: An API<br>is used by the code.obtain technique, most likely from a custom class API<br>that communicates with an API for football. It submits a request to the<br>/v3/teams endpoint of the API, supplying the team name asa variable.</div><div>&nbsp;</div><div>Handling API Responses:<br>This involves processing the API request's outcome.</div><div><br></div><div>Results (result.get('results', 0) &gt; 0) indicates that<br>information is returned by the API details about the desired team are at<br>hand.</div><div><br></div><div><div>Data Transformation: team_data = result['response'][0]['team'] extracts the team data from the API response.<br>After that, the data is formatted so that it can be added to<br>the database.</div><div><br></div><div>Database Function: The converted team information is entered using the DB.insertOne function<br>into the database's IS601_Team table. The</div><div><br></div><div>A clause known as "ON DUPLICATE KEY UPDATE"<br>guarantees that if a team with the same ID is already present in<br>the database, and its details have been updated.</div><div><br></div></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/TarunGolyalla/tg335-is601-007/pull/20">https://github.com/TarunGolyalla/tg335-is601-007/pull/20</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>One significant problem that arose during this milestone was with the Flask application's<br>implementation of data validation and error handling. The difficulty was specifically making sure<br>that several error messages for various form fields were appropriately displayed when there</div><div><br></div><div>were<br>mistakes in validation. Initially, the implementation simply displayed a general error message, which<br>made.It is challenging to pinpoint particular problems with the form submission.</div><div><br></div><div>To deal with<br>this matter, I discovered that although helpful, Flask's validate_on_submit() method lacked a detailed<br>methodology to addressing specific form field mistakes. To get around this restriction, I<br>changed the accessing form fields directly from the request during the validation process.form<br>object and examining particular circumstances. This made it possible to validate data more<br>precisely and show clearly error messages for every pertinent field on the form.</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://dashboard.heroku.com/apps/is601-tg335-dev/login">https://dashboard.heroku.com/apps/is601-tg335-dev/login</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T20.40.18wakatime.png.webp?alt=media&token=683731d8-f9a2-45e4-abf6-c9e72cbbb12f"/></td></tr>
<tr><td> <em>Caption:</em> <p>ss<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Ftg335%2F2023-12-14T20.40.40wakatime%202.png.webp?alt=media&token=c55c0860-d39a-435a-a7c9-58fb35f3b03e"/></td></tr>
<tr><td> <em>Caption:</em> <p>ss<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/tg335" target="_blank">Grading</a></td></tr></table>
