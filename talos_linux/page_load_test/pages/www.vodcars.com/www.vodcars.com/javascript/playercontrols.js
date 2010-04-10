

    function mediaPause()
    {
        // placeholder
        sendEvent('pause',0);
    }
    
    function mediaPlay()
    {
        // placeholder
        sendEvent('resume',1);
    }
    
    function mediaGetElapsed()
    {
        // placeholder
        return currentPosition * 1000;
    }
    
    // some variables to save
    var currentPosition;
    var currentVolume;
    var currentItem;

    // these functions are caught by the JavascriptView object of the player.
    function sendEvent(typ,prm) { thisMovie("mediaplayer").sendEvent(typ,prm); };
    function getUpdate(typ,pr1,pr2,pid) {
        if(typ == "time") { currentPosition = pr1; }
        else if(typ == "volume") { currentVolume = pr1; }
        else if(typ == "item") { currentItem = pr1; setTimeout("getItemData(currentItem)",100); }
        var id = document.getElementById(typ);
        id.innerHTML = typ+ ": "+Math.round(pr1);
        pr2 == undefined ? null: id.innerHTML += ", "+Math.round(pr2);
        if(pid != "null") {
            document.getElementById("pid").innerHTML = "(received from the player with id <i>"+pid+"</i>)";
        }
    };

    // These functions are caught by the feeder object of the player.
    function loadFile(obj) { thisMovie("mediaplayer").loadFile(obj); };
    function addItem(obj,idx) { thisMovie("mediaplayer").addItem(obj,idx); }
    function removeItem(idx) { thisMovie("mediaplayer").removeItem(idx); }
    function getItemData(idx) {
        var obj = thisMovie("mediaplayer").itemData(idx);
        var nodes = "";
        for(var i in obj) { 
            nodes += "<li>"+i+": "+obj[i]+"</li>"; 
        }
        //document.getElementById("data").innerHTML = nodes;
    };

    // This is a javascript handler for the player and is always needed.
    function thisMovie(movieName) {
        if(navigator.appName.indexOf("Microsoft") != -1) {
            return window[movieName];
        } else {
            return document[movieName];
        }
    };
   