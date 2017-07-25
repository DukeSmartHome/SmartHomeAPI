var express = require('express'),
	app = express(),
	bodyParser = require('body-parser'),
	morgan = require('morgan'),
	firebase = require("firebase");

var port = process.env.PORT || 6969;


// firebase setup
firebase.initializeApp({
	databaseURL: "https://parentsparse.firebaseio.com/",
	serviceAccount: "firebasekey.json"
});

var db = firebase.database();
var lightingDB = db.ref("lighting");


// CONFIGURE APP

// body parser, to grab information from POST requests
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// configure app to handle CORS requests
app.use(function(req, res, next) {
	res.setHeader('Access-Control-Allow-Origin', '*');
	res.setHeader('Access-Control-Allow-Methods', 'GET, POSTS');
	res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With, \
		content-type, Authorization');
	next();
});


// BASE APP ==================================================================
// MIDDLEWARE
app.use(morgan('dev'));  // log all requests to the console

// BASE ROUTES
app.get('/', function(req, res) {
	res.send('Smart Home API');
});



// API =======================================================================
var apiRouter = express.Router();  // get an express router

// API MIDDLEWARE ============================================================
apiRouter.use(function(req, res, next) {
	// console.log("someone just came to the app");
	// this is where we authenticate users
	next();
});

// API Routes =================================================================
apiRouter.get('/', function(req, res) {
	res.json({ message: 'docs go here'});
});

apiRouter.route('/lighting')
	//create a new light

	.post(function(req, res) {
		// Firebase
		// var newlight = {};
		// newlight.room = req.body.room;
		// newlight.light =req.body.light;
    // console.log("hehe");
    // console.log(String(req.body.fname));
		lightingDB.push({
			room: req.body.room,
			light: req.body.light,
      status: "off",
		}, function(err) {
			if (err) {
				res.send(err)
			} else {
				res.json({ message: "Success: Light created."})
			}
		});

	})
	.get(function(req, res) {
		// get all lights from firebase
		lightingDB.once("value", function(snapshot, prevChildKey) {
			res.json(snapshot.val());
		})
	});

// Single Light Routes
apiRouter.route('/lighting/:l')

	.get(function(req, res) {
		// Firebase GET user info
		var l = req.params.l;
			if (l.length != 20) {
				res.json({message: "Error: Light ID must be 20 characters long."});
			} else {
				lightingDB.child(l).once("value", function(snapshot) {
					if (snapshot.val() == null) {
						res.json({message: "Error: No Light found with that ID"});
					} else {
						res.json(snapshot.val());
					}
				});
			}
		})
	.put(function(req, res) {
		// Firebase Update light info
		var l = req.params.l,
			user = {};
		// update only parameters sent in request
		if (req.body.room) user.room = req.body.room;
		if (req.body.light) user.light = req.body.lights;
    if (req.body.status) user.status = req.body.status;


		lightingDB.child(l).update(user, function(err) {
			if (err) {
				res.send(err);
			} else {
				res.json({message: "Success"})
			}
		});

	})


// Register routes
app.use('/api', apiRouter);

app.listen(port);
console.log('port: '+ port);
