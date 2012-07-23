<h1>Usage.</h1>
<h5>Using mpart-encoder is as easy as it could get. Consider the following example script that posts a simple string to pastie.org:</h5>

```python
import mpart, urllib2

fields = {'paste[body]':'Hello World!', 'paste[authorization]':'burger', 'paste[restricted]':'0','paste[parser_id]':'4','key':'','lang':''}
files = {}

mpart = mpart_encode(fields, files)
req = urllib2.Request('http://pastie.org/pastes')
req.add_header('content-type', mpart[0])
req.add_header('user-agent', 'mpart-encoder tutorial 1.0')
req.add_header('content-length', len(mpart[1]))
req.add_data(mpart[1])
try:
	resp = urllib2.urlopen(req)
	print resp.url
except Exception, e:
	print e.read()
```

<h5>Simple right? Just pass your form data to the mpart_encode function in the form of two dictionaries (one containing post fields, the other files) and you get the 'content-type' header and the encoded data back.</h5>
<hr/>
<h1>What you get back.</h1>
<h5>When you call mpart_encode, you pass in form data, but how is all that encoding handed back?</h5>
```python
import mpart
data = {'name':'John Doe', 'email':'johndoe@mail.com'}
files = {}
multipart = mpart_encode(data, files)
print multipart[0]
print multipart[1]
```
<h5>This yeilds the output:</h5>
```text
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


