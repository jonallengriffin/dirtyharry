/***********************************************************************
 *
 * Copyright (c) 2007 ScanScout, Inc. All Rights Reserved.
 *
 * This software is the confidential and proprietary information of
 * ScanScout. ("Confidential Information"). You shall not disclose
 * such Confidential Information and shall use it only inaccordance
 * with the terms of the license agreement you entered into with
 * ScanScout.
 *
 ***********************************************************************/

// adstreamjscontroller.js
// Obsolete - replaced by ScanScout.js

if (!self.ScanScout) ScanScout = {};

ScanScout.fileName = 'adstreamjscontroller.js';
ScanScout.revisionString = "$Revision: 7787 $";

	

/////////////////////////////////////////////////////////////
// Fetch a JS URL, which causes the script to load and execute
// (This works both in IE and FireFox):
//
ScanScout.fetchJSURL = function (theURL)
{
	var script = document.createElement('script');
	script.type = 'text/javascript';
	script.src = theURL;

	var head = document.getElementsByTagName('head').item(0);
	window.setTimeout(function() { head.appendChild(script) });
}


/////////////////////////////////////////////////////////////
// Look through all known script tags to find one containing filename,
// and return its prefix, which is used to generate other URLs for the same server.
ScanScout.getURLPrefix = function (filename)
{
	if (ScanScout.urlPrefix) return ScanScout.urlPrefix;

	var allScripts = document.getElementsByTagName("script");
	var scriptRegExp = new RegExp(filename + "(\\?.*)?$", "");
	var prefix = '';
	for (var i=0; i < allScripts.length; i++)
	{
		var script = allScripts[i];
		if  (script.src && script.src.match(scriptRegExp))
		{
			prefix = script.src.replace(scriptRegExp, '');
			// if (confirm('check prefix: ' + prefix)) debugger;
			break;
		}
	}

	if (prefix.match(/^\//))
	{
		// Make fully qualified absolute URL
		var pageURLPrefix = document.location.protocol + '//' + document.location.host;
		//if (confirm('fully qualify with: ' + pageURLPrefix)) debugger;
		prefix = pageURLPrefix + prefix;
	}
	if (!prefix.match(/^(https?:)/))
	{
		var badPrefix = prefix;
		// Hard-wire the prefix
		prefix = 'http://app.scanscout.com/ssframework/';
		//ss_logWarning('Bad URL prefix: ' + badPrefix);
		//if (confirm('bad URL prefix: ' + badPrefix)) debugger;
	}
	return prefix;
}

// Fallback functions, in case customer calls any of these.
function ss_start()
{
	window.setTimeout(ss_start, 100); // wait until ScanScout.js is loaded.
}

function ss_stop()
{
	// Must not be running yet.
}

function ss_restart()
{
	ss_start();
}

ScanScout.urlPrefix = ScanScout.getURLPrefix(ScanScout.fileName);
window.setTimeout(function()
{
	ScanScout.fetchJSURL(ScanScout.urlPrefix + 'dhtml/ScanScout.js');
}, 10);


//if (confirm('Redirected to ' + ScanScout.urlPrefix + 'dhtml/ScanScout.js')) debugger;

///////////////////////////////////////////////////////////////
// Workaround for references to functions not yet defined.

function ss_workaround (funcName)
// Define a function for funcName that will try to use latest definition.
{
	var fakeFunc = function () 
	{
		var realFunc = self[funcName];
		// If fakeFunc and realFunc are different, function has been redefined, so call it.
		if (fakeFunc != realFunc)
			return realFunc();
		// otherwise just return since the video hasn't been started anyway.
	};
	// If not already defined, use the fakeFunc. 
	if (!self[funcName])
		self[funcName] = fakeFunc;
};

// For Inventory page:
ss_workaround("ss_getPlayPosition");

// For Warp Radio:
ss_workaround("ss_getPlayPositionWMP");

// For Blip.tv:
ss_workaround("ss_getPlayPositionPokkari");
ss_workaround("ss_getPlayStatePokkari");
ss_workaround("ss_pausePlayPokkari");
ss_workaround("ss_resumePlayPokkari");

//=============================================
// This should be the last thing in the file:
self.ss_isLoaded = true; // necessary for backward compatibility
