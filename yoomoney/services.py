

def add_amount_to_user_balance_and_save_site_user_model(user, amount):
	user.siteuser.balance += amount
	user.siteuser.save()