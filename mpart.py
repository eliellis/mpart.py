import random

def mpart_encode(fields, files):
	random_boundary = randy_boundary(10)
	content_type = "multipart/form-data, boundary=%s" % random_boundary


	form_data = []
	for (key, value) in fields.iteritems():
		itemstr = '--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n' % (random_boundary, key, value)
		form_data.append(itemstr)

	for (key, value) in files.iteritems():
		with value:
			itemstr = '--%s\r\nContent-Disposition: form-data; name="%s"; filename="%s"\r\n\r\n%s\r\n' % (random_boundary, key, value.name, value.read())
		form_data.append(itemstr)

	form_data.append('--%s--\r\n' % random_boundary)

	return content_type, ''.join(form_data)

def randy_boundary(length=5,reshuffle=False):
	character_string = "abcdefghijklmnopqrstuvwxz1234567890"
	boundary_string = []
	for i in range(0,length):
		rand_index = random.randint(0,len(character_string) - 1)
		boundary_string.append(character_string[rand_index])
	if reshuffle:
		random.shuffle(boundary_string)
	else:
		pass
	return ''.join(boundary_string)