from beaker import * 
from pyteal import *

class FirstApp(Application):
    # @create tells beaker that this is going to be used for the creation of the smart contract
    @create
    def create(self):
        return Approve()
    
    @external
    def hello(self, name: abi.String, *, output:abi.String):
        #anything we want to do on chain needs to be in our return statement
        return output.set(Concat(Bytes("Hello "), name.get()))
    
    @external
    def add(self, a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64):
        return output.set(a.get() + b.get() + Int(5))
    
    @external
    def multi_logger(self, a: abi.String, b: abi.String, *, output: abi.String):
        return Seq(
            Log(a.get()),
            Log(b.get()),
            output.set(Concat(a.get(), b.get()))
        )
    
    @external
    def if_expression(self, input)
    
first_app = FirstApp(version=8)

#executes the teal files
#used if you want to use the teal files for front end
first_app.dump()

#use in sandbox for testing for now
acct = sandbox.get_accounts()[0]

app_client = client.application_client.ApplicationClient(
    app = first_app,
    client = sandbox.clients.get_algod_client(),
    sender = acct.address,
    signer = acct.signer,
)

app_client.create()
return_object = app_client.call(method = FirstApp.multi_logger, a = "Hello ", b = "Meko")

print(return_object.return_value)