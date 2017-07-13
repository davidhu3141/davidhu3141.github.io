
def permute ( finished_part, not_yet_permute ):

	if not not_yet_permute:
		print(''.join(finished_part))
		return
	
	for e in not_yet_permute:
		new_finished_part = finished_part + [e]
		remains = not_yet_permute[:]  # copy not_yet_permute to remains
		remains.remove(e)
		permute ( new_finished_part, remains)

permute ([], ['a', 'b', 'c', 'd'])
