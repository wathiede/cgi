# CGI In Go

	# Build the go cgi example
	$ go build -o cgi-bin/cgigo ./cgigo
	# Run the server
	$ go run server/server.go -addr :1234

## Now visit a cgi url:
Assuming you have perl & python installed all the following URLs will work. 

[Go version](http://localhost:1234/cgi-bin/cgigo)
[Python version](http://localhost:1234/cgi-bin/cgitest.py)
[Perl version](http://localhost:1234/cgi-bin/cgi.pl)
