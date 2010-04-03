/*
 Meta functions
 http://www.irt.org/articles/cgi.htm
*/

function showMeta(object) {
    if (document.getElementById && document.getElementById(object) != null) {
         document.getElementById(object).style.visibility='visible';
         document.getElementById(object).style.display='block';
    }

    else if (document.layers && document.layers[object] != null) {
        document.layers[object].visibility = 'visible';
    }

    else if (document.all) {
        document.all[object].style.zIndex = 100;
        document.all[object].style.visibility = 'visible';
    }
}

function hideMeta(object) {
    if (document.getElementById && document.getElementById(object) !=  null) {
         document.getElementById(object).style.visibility='hidden';
         document.getElementById(object).style.display='none';
    }

    else if (document.layers && document.layers[object] != null) {
        document.layers[object].visibility = 'hidden';
    }
	
    else if (document.all) {
         document.all[object].style.visibility = 'hidden';
    }
}
