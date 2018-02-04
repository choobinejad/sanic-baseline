# Clean up the directory
rm certs/*

# Make the files
touch certs/index.txt
echo '01' > certs/serial

# Make CA key and cert
openssl genrsa -out certs/ca.key 4096
openssl req -new -x509 -key certs/ca.key -out certs/ca.crt -config ca_req.cnf

# Make the server CSR
openssl req -new -out certs/server.csr -days 3650 -config server.cnf

# Sign the server CSR
openssl ca -config ca.cnf -out certs/server.crt -extfile server.ext.cnf -in certs/server.csr

# Make the client CSR
openssl req -new -out certs/client.csr -days 3650 -config client.cnf

# Sign the client CSR
openssl ca -config ca.cnf -out certs/client.crt -in certs/client.csr

# Also make a client pkcs12 for browsers
openssl pkcs12 -export -out certs/client.p12 -inkey certs/client.key -in certs/client.crt -certfile certs/ca.crt