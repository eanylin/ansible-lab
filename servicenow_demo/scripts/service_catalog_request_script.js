try {
	    // Get Request Item Number
	    var requestedItem = new GlideRecord('sc_req_item');
	    requestedItem.addQuery('sys_id', current.sys_id);
	    requestedItem.query();
	    if (requestedItem.next()) {
	       var req_item_number = requestedItem.number;
		}
	
	    // Get Request Number
	    var request_number = current.request.number;
	
	    // Retrieve Value of Variables
	    var server1 = current.variables.server1;
	    var server2 = current.variables.server2;
		var server3 = current.variables.server3;
	
	    // Construct extra_vars variable
	    var extra_vars = '{"extra_vars": { "request_number": ' + '"' + request_number + '", ' + '"req_item_number": ' + '"' + req_item_number + '", ' + '"server1": ' + '"' + server1 + '", ' +  '"server2": ' + '"' + server2 + '", ' + '"server3": ' + '"' + server3 + '"' + ' }}';
	
	    // Trigger REST API Call to Ansible Tower
        var request = new sn_ws.RESTMessageV2();
	    request.setLogLevel('all');
	    request.setBasicAuth('username','mypassword');
	    request.setRequestHeader("Content-Type","application/json");
        request.setHttpMethod('post');
        //request.setEndpoint('https://10.10.10.10/api/v2/job_templates/8/launch/');
	    request.setEndpoint('https://10.10.10.10/api/v2/workflow_job_templates/10/launch/');
		request.setRequestBody(extra_vars);
	
        // REST API Call Response;    
        var response = request.execute();
	    var responseBody = response.getBody();
        var httpResponseStatus = response.getStatusCode();
      
        gs.print("http response status_code: " + httpResponseStatus);        
}

catch (ex) {
        var message = ex.getMessage();
        gs.print(message);
}
