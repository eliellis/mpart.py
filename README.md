<h1>Usage</h1>
<h3>Just import mpart.py, create a dictionary containing form-data (plain feild data or some files) and call ```mpart.encode(your dictionary)``` and you're data is now ready for the big time.</h3>
<hr/>
<h1>Example</h1>
<h5>Using mpart.py is as easy as it could get. Consider the following example script that posts a simple string to pastie.org:</h5>

```python
import mpart, urllib2

fields = {'paste[body]':'Hello World!', 'paste[authorization]':'burger', 'paste[restricted]':'0','paste[parser_id]':'6','key':'','lang':''}

mpartdata = mpart.encode(fields)
req = urllib2.Request('http://pastie.org/pastes')
req.add_header('content-type', mpartdata[0])
req.add_header('user-agent', 'mpart.py tutorial 1.0')
req.add_header('content-length', len(mpartdata[1]))
req.add_data(mpartdata[1])
try:
	resp = urllib2.urlopen(req)
	print resp.url
except Exception, e:
	print e.read()
```

<h5>Simple right? Just pass your form data to the encode function in the form of one dictionary (containing fields and or files) and you get the 'content-type' header and the encoded data back.</h5>
<hr/>
<h1>What you get back.</h1>
<h5>When you call encode, you pass in some form data, but how is all that handed back?</h5>
```python
import mpart
data = {'name':'John Doe', 'email':'johndoe@mail.com'}
multipart = mpart.encode(data)
print multipart[0]
print multipart[1]
```
<h5>This yeilds the output (where the boundary is generated randomly):</h5>
```
multipart/form-data, boundary=9q3ep42ief
--9q3ep42ief
Content-Disposition: form-data; name="name"

John Doe
--9q3ep42ief
Content-Disposition: form-data; name="email"

johndoe@mail.com
--9q3ep42ief--

```
<h5>The first line is the 'content-type' header that contains the boundary used in the encoding. The lines following the first are the encoded data. So, the method returns a list containing both the header string you should use, and the multipart form-data</h5>


