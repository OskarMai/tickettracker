Description:
This project is a web application that tracks bugs within projects. You are able to add projects and submit tickets for each project.
This web application was created to help manage issues involving tickets in an organized manner.
----------------------------------------------------------------------------------------------------------------------------------------------------------
Functions:
	user_profile index:
	user_profile edit:
	ticket index:
	ticket submission:
	ticket details:
	ticket comments:
	ticket upload:
	ticket edit:
	project index:
	project add/remove:
	project personnel:
	registration:
	login and logout:
	change password:
----------------------------------------------------------------------------------------------------------------------------------------------------------
Restrictions:
By default, all newly created accounts are in the submitter group.
All non-admin accounts are restricted from accessing certain view functions. 
Newly created accounts must be manually given permission.
Submitter accounts have access to ticket submission and user profile.
Developer accounts have access to ticket submission,ticket index, user profile, ticket details, and ticket edit.
All tickets have its own details pages and edit page. They are only accessible by members assigned to that ticket's project.
Admin accounts have access to projects index, project member management, ticket submission, ticket index, user profile, ticket details, and ticket edit.
Admin accounts must assign users(developers or admin accounts) to projects. 
Only users assigned to a project can access the details of that project's tickets.

----------------------------------------------------------------------------------------------------------------------------------------------------------
Accounts:
admin account email:admin@gmail.com
admin account pass:superuserpass

developer account email:developer@gmail.com
developer account pass:adminpass

submitter acount email:submitter@gmail.com
submitter account email:adminpass
