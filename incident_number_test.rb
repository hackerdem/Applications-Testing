

require 'net/http'
require 'json'
require 'workers'
require 'rest-client'
#login and receive authentication token############################
def login()
    uri = URI('http://54.252.241.122:8000/users/authenticate')
    http = Net::HTTP.new(uri.host, uri.port)
    req = Net::HTTP::Post.new(uri.path, 'Content-Type' => 'application/json')
<<<<<<< HEAD:incident_number_test.rb
    req.body = {email: 'demo1@g.com', password: '**********'}.to_json
=======
    req.body = {email: 'demo1@g.com', password: '********'}.to_json
>>>>>>> ad82cfe334c55b5b264ff0ba4d4dfca5537450f9:incident_num_test.rb
    res = http.request(req)
    tkn=JSON.parse(res.body)
    return tkn['result']['token']
end
# query for creating actions #######################################
mytoken=login() #from action test
header={
        'Accept'=> "application/json, text/plain, */*",
        'Accept-Encoding'=>'gzip, deflate',
        'Accept-Language'=>'en-US,en;q=0.8,tr;q=0.6,es;q=0.4,la;q=0.2',
        "Authorization"=>"#{mytoken}",
        "Connection"=>"keep-alive",
        "Host"=>"54.252.241.122:8000",
        "Origin"=>"http://safechamp-8000.herokuapp.com",
        "Referer"=>"http://safechamp-8000.herokuapp.com/",
        "User-Agent"=>"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
query1={
    tzDateCreated:"Australia/Sydney",
    dateOccurred:"2017-08-08",
    personReporting:"test numbering",
    location:"test numbering",
    overview:"test numbering",
    category:"First Aid",
    injuredPersonName:"test numbering",
    injuredPersonPhone:"test numbering",
    injuredPersonRole:"Employee",
    injuryDescription:"test numbering",
    propOrEnvDamage:"No",
    propOrEnvDamageDescription:"null",
    witnessName:"test numbering",
    witnessPhone:"test numbering",
    description:"test numbering",
    attachments:""   
}.to_json
boundary='------WebKitFormBoundarypzp7PZte3S2nqOT5'
EOL = "\015\012"  # "\r\n"
key=boundary+"\r\n"+"Content-Disposition: form-data; name=\"json\""+EOL+EOL+query1+EOL+boundary+'--'

# threading part####################################################
pool=Workers::Pool.new(:on_exception=>proc{|e|
puts "A worker encountered exception:#{e.class}:#{e.message}"
})
50.times do
    pool.perform do
        req1 = RestClient::Request.execute(
            method: :POST,
            url:'http://54.252.241.122:8000/incidents/new',
            payload:{:multipart => true, :json => query1},
            headers:header
        )
        puts req1 
        RestClient.log = 'stdout'

    end 
end


pool.dispose(30) do
    puts "Worker thread #{Thread.current.object_id} is shutting down"
    end

