import user


first_admin = user.Admin('Lois','Kwakyewaa','LoisK',20,'Amasaman')
first_admin.increament_login_attempts()
# calling the show privilages method from the privilages attribute
first_admin.privileges.show_privilages()

