# This is a simplified example of how you could structure the backend using Flask

 from flask import Flask, request,jsonify

   app = Flask(_name_)

#Simulated database for storing listings

   listings = []

#Route to create a new listing
   @app.route('/create_listing',methods=['POST'])
   def create_listing():
         data = request.json
         new_listing ={
                       'item_name':data['item_name'],
                       'price':data['price'],
                       'seller_id':data['seller_id'],
                       'expiry':7 # Expire in days
                      }
                      listings.append(new_listing)
                      return jsonify({'message': 'Listing created successfully'})

 # Route to fetch all listings                    
 @app.route('/listings', methods=['GET'])
 def get.listings():
     return jsonify({'listings': listings})

 # Route to buy a listed item
 @app.route('/buy_item/<int:listing_id>',methods=['POST'])
 def buy_item(listing_id):
     # Simulated paymenr process
     item = listing[listing_id]
     #Here you would initiate the payment process, mark the item as sold,etc.
     listing.pop(listing_id)
     return jsonify({'message': 'Item bought successefully'})


  if __name__  == '__main__':
      app.run(debug=True)

                       
