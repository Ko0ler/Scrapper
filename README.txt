topic : web scrapping app
model : MVC
tools : python
functionalities :
 - take user input (name, email, url, content to extract, saving format)
 - extraction
 - saving (html, txt, xml)
 - history tracking
algo :
 1. home page, presentation
 2. prompt to enter user data (name, email)
 3. user chooses an option
 4. prompt to enter extraction data (content to extract, url, saving format)
 5. check for eligibility/authorization
 6. if eligible then :
 	extraction()
 	display output
    else :
	display "not doable"
 7. ask for a retry :
	if true then :
		retry from step 3
	elif exit then :
	quit()
