require 'base64'
require 'openssl'

jwt= "jwt_goes_here"

header, data, signature = jwt.split(".")
def sign(data, secret)    
Base64.urlsafe_encode64(OpenSSL::HMAC.digest(OpenSSL::Digest.new("sha256"), 
secret, data)).gsub("=","")
end
File.readlines("possible_secrets.txt").each do |line|
  line.chomp!
    if sign(header+"."+data, line) == signatureputs 
    puts line
    exit
  end
end
