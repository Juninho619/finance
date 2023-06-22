
def buy():
    """Buy shares of stock"""
    #if request.method == "POST":

        #shares = int(request.form.get("shares"))

        # Make sure the user entered input
        #if not request.form.get("symbol"):
           # return apology("Please enter a valid symbol")

        # Same for shares
        #elif not request.form.get("shares"):
            #return apology("Please enter valid shares")

        # Shares have to be positive

       # elif int(request.form.get("shares")) < 0:
            #return apology("Shares must be a positive number", 400)

        #elif not shares.isdigit():
            #return apology("Shares must be a positive number", 400)


        # Make sure stock is correct
       # if not lookup(request.form.get("symbol")):
            #return apology("Symbol couldn't be found. Please enter another")

        # Use lookup function
        #symbol = request.form.get("symbol").upper()
        #stock = lookup(symbol)


        # initialise values at stake
        #shares = int(request.form.get("shares"))

       # try:
            #shares = int(shares)
            #assert shares > 0
        #except ValueError as ex:
           # return apology("shares must be a positive integer", 400)
        #beetlebum = shares * stock['price']

        # Make sure the user has enough money
        #user_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        #cash = user_cash[0]["cash"]

        # Make the needed substraction
       # subdcash = cash - beetlebum

        # Can't proceed if user doesn't have enough money
        #if subdcash < 0:
            #return apology("Sorry. You do not possess enough money to make this transaction")

        # Update the user's database
        #db.execute("UPDATE users SET cash=: subdcash WHERE id=:id", subdcash=subdcash, id=session["user_id"]);

        # Update the transaction's table
        #db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)", user_id=session["user_id"], symbol=stock['symbol'], shares=shares, price=stock['price'])

        # Notice the user the transaction was successful
        #flash("Transaction successfully completed")

        #return redirect("/")

        # Get method
    #else:
        #return render_template("buy.html")