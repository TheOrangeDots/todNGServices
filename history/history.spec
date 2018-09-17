{
	"name": "todHistory",
	"displayName": "history",
	"version": 1,
 	"definition": "todngservices/history/history.js",
	"libraries": [],
 	"api":
 	{
	   	"pushState": 
	   	{
	    	"parameters":
	    	[
		    	{
					"name":"stateObject",
					"type":"object"
				}, {
					"name":"title",
					"type":"string"
				}, {
					"name":"url",
					"type":"string"
				}
			]
		},
		"replaceState": 
	   	{
	    	"parameters":
	    	[
		    	{
					"name":"stateObject",
					"type":"object"
				}, {
					"name":"title",
					"type":"string"
				}, {
					"name":"url",
					"type":"string"
				}
			]
		},
		"back": {},
		"forward": {}
 	}
}