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