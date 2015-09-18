
def net_reg(hours,rate):
	'''calculates net pay w/o OT'''
	net_reg = hours*rate
	return net_reg

def net_inc_ot(hours,rate):
	'''reg pay with OT (reg hours are at least 8)'''
	reg_hours = 8
	ot_hours = hours - reg_hours
	ot_rate = 1.5*rate
	total_net=rate*reg_hours+ot_rate*ot_hours
	return total_net
	
def net(hours,rate):
	reg_hours = 8
	if hours <= reg_hours:
		return net_reg(hours,rate)
	else:
		return net_inc_ot(hours,rate)


