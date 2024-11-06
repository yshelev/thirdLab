

def add_amount_to_user_balance_and_save_site_user_model(user, amount):
	user.siteuser.balance += amount
	user.siteuser.save()

def accept_balance_change(change):
	change.is_accepted = True
	change.save()