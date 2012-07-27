import random, mimetypes, string

def encode(fields={}, files={}):
	random_boundary = __randy_boundary()
	content_type = "multipart/form-data, boundary=%s" % random_boundary

	form_data = []
	if fields:
		for (key, value) in fields.iteritems():
			itemstr = '--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n' % (random_boundary, key, value)
			form_data.append(itemstr)
	else:
		pass

	if files:
		for (key, value) in files.iteritems():
			with value:
				file_mimetype = mimetypes.guess_type(value.name)[0] if mimetypes.guess_type(value.name)[0] else 'application/octet-stream'
				itemstr = '--%s\r\nContent-Disposition: form-data; name="%s"; filename="%s"\r\nContent-Type: %s\r\n\r\n%s\r\n' % (random_boundary, key, value.name, file_mimetype, value.read())
			form_data.append(itemstr)

	form_data.append('--%s--\r\n' % random_boundary)

	return content_type, ''.join(form_data)

def __randy_boundary(length=10,reshuffle=False):
	character_string = string.letters+string.digits
	boundary_string = []
	for i in range(0,length):
		rand_index = random.randint(0,len(character_string) - 1)
		boundary_string.append(character_string[rand_index])
	if reshuffle:
		random.shuffle(boundary_string)
	else:
		pass
	return ''.join(boundary_string)