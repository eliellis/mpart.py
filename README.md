<h1>Usage.</h1>
<h3>Using mpart-encoder is a simple as it could get. Consider the following example script that posts a simple string to pastie.org:</h3>

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

Simple right? Just pass your form data to the mpart_encode function in the form of two dictionaries (one containing post fields, the other files) and you get the 'content-type' header and the encoded data back.


