# BranchChange-2015
                                                            GROUP 17
                       (Sindhura,140050051) (Sowmya Mutyala,140050072) (Shachi Deshpande,140110047)
                       

                       Individual percentages:
                           Sindhura : 100%
                           Sowmya   : 100%
                           Shachi   : 100%
      		
			                 

                      List of commands to run the code:
                        1. Set up virtual environment, and clone the submitted repository in the directory in virtual environment.
                        2. Type 'python manage.py makemigrations'
                        3. Now type 'python manage.py migrate'
                        4. Type 'python manage.py syncdb'
                        5. Now type 'python manage.py runserver'
                        6. Now go to http://127.0.0.1:8000/ on your browser and see the welcome page
                        7. If you go to http://127.0.0.1:8000/admin , you should be able to login as admin, with username 'mutant' and password 'password'
                        8. You can create a superuser using bash commands inside the floder containing manage.py, so that you can login with your own username and password.
                        9. You can add users (i.e. students) as an admin and assign them default passwords, giving them permission to only view the form. This is done using the 'add user' button on admin page. Admin can himself also fill branch change form, being a superuser.
                        10. Also, admin can upload the csv using 'csvimport' option. After that he has to fill required options and the file gets uploaded in ./media/documents/ path. CSV can also be uploaded using  http://127.0.0.1:8000/list/ as address.
                        11. You can logout, and then login once again as a user created b admin, with corresponding username and password. Thus you can see the branch change form to fill.


                        NOTE: We will add the remaining functionalities in admin and user interface after 1 day ( we are taking one lateday). We have added the python code 'process.py' which generates 'final.csv' as the final branch change allotment. 'tocheck.csv' creates the same final.csv with sorted entries according to name and roll number.All the output files will be generated in the root folder where manage.py is located. The input file should be available in ./media/documents/ with name input.csv and the branch capacities should be available in ./media/documents/ as capacities.csv.




                      Honor code:
                        We pledge on our honor that we did not give or receive any unauthorized assistance for this assignment.
                        And the above mentioned percentages are  claimed sincerely.
                        We are using 1 lateday.

                      References:
                       we througly used this internet source to understand concepts and learn the syntax.
                        http://tutorial.djangogirls.org/
                       
