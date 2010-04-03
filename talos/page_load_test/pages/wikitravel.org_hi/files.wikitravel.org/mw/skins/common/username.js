// arch-tag: User name indication Javascript

var page_title = new String;
var script_path = new String;
var db_name = new String;
var specialns = new String;
var admins = new Array;
var watchlist = new Array;
var protected_page = false;
var message_map = false;
var new_msg_path = new String;

function set_page_title (string) {
     page_title = string;
     return true;
}

function set_script_path (string) {
     script_path = string;
     return true;
}

function set_db_name (string) {
     db_name = string;
     return true;
}

function set_specialns (string) {
    specialns = string;
    return true;
}

function set_admins (list) {
    admins = list.split(',');
    return true;
}

function is_admin(id) {
    for(var i=0;i < admins.length;i++) {
        if (admins[i] == id) {
            return true
        }
    }
    return false;
}

function set_message_map(obj) {
   message_map = obj;
}

function set_new_msg_path(path) {
   new_msg_path = path;
}

function is_logged_in()
{
   return (read_cookie(db_name + '_session') &&
	   read_cookie(db_name + 'UserID') &&
	   read_cookie(db_name + 'UserName'));
}

function set_watchlist(list) {
    watchlist = list.split(',');
    return true;
}

function set_protected(bool) {
    protected_page = bool;
    return true;
}

function read_cookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for(var i=0;i < ca.length;i++) {
    var c = ca[i];
    while (c.charAt(0)==' ') c = c.substring(1,c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
  }
  return null;
}

function get_link(id) {
  var the_link = null;
  var the_item = document.getElementById(id);
  if (the_item) {
     var nl = the_item.getElementsByTagName('a');
     if (nl.length >= 1) {
         the_link = nl.item(0);
     }
  }
  return the_link;
}

function set_link_text(id, new_text) {
  var the_link = get_link(id);
  if (the_link) {
     var new_text_node = document.createTextNode(new_text);
     var old_text_node = the_link.firstChild;
     the_link.replaceChild(new_text_node, old_text_node);
  }
  return true;
}

function string_replace(str, old, repl) {
  var index = str.indexOf(old);
  if (index == -1) {
    return str;
  } else {
    return str.substr(0, index) + repl + str.substr(index + old.length);
  }
}

function replace_link_href(id, old, repl) {
     var the_link = get_link(id);
     if (the_link) {
          var old_href = the_link.getAttribute('href');
          var new_href = string_replace(old_href, old, repl);
          the_link.setAttribute('href', new_href);
     }
}

function set_element()
{
   this._element.src = this.src;
}

function set_image_src(id, new_src) {
   var the_image = new Image();
//   var the_image = document.createElement("img");

   the_image._element = document.getElementById(id);
   the_image.onload = set_element;
   the_image.src = new_src + "?datestamp=" + (new Date()).getTime() ;
   // onload function will actually set the value
}

function new_msg_url(username) {
   return new_msg_path + "/" + username + ".gif";
}

function page_name(ns, title) {
  return ns + ":" + title;
}

function setup_user_name(userns, usertalkns, logout) {

   if (is_logged_in()) {
      var user_name = read_cookie(db_name + 'UserName');
      set_link_text('pt-logout', logout);
      set_link_text('pt-userpage', decodeURIComponent(user_name).replace(/\+/, ' '));
      replace_link_href('pt-userpage', page_name(specialns, "Mypage"),
                        page_name(userns, user_name));
      replace_link_href('pt-mytalk', page_name(specialns, "Mytalkpage"),
                        page_name(usertalkns, user_name));

      //IE isn't happy if this runs before the page loads.
      addWindowOnload(
         function () {
            set_image_src('pt-newmsg', new_msg_url(user_name.replace(/[ \+]/, '_')));
         }
      );
   } 
   else {
      var ip = read_cookie('wikitravel_ip'); // FIXME: site name needs to go
      if (ip) {
         //IE isn't happy if this runs before the page loads.
         addWindowOnload(
            function () {
               set_image_src('pt-newmsg', new_msg_url(ip));
            }
         );
      }
   }

  return true;
}

/*
  Simple event chainer.  Should move this to a nicer js package.  
  But then we should probably reconsider how we do the js altogether.
*/
function addWindowOnload(f) {
  if (!window.onload) {
    window.onload = f;
  }
  else {
    o = window.onload;
    window.onload = function(){o();f();}; 
  }
}

function add_list_link(list, title, url) {
    var link = document.createElement('a');
    var text = document.createTextNode(title);
    link.setAttribute('href', url);
    link.appendChild(text);
    var item = document.createElement('li');
    item.appendChild(link);
    list.appendChild(item);
    return true;
}

function add_move_url(list) {
   return add_list_link(list, message_map.move,
			script_path + '?title=' + page_name(specialns, "Movepage")
			+ '&target=' + encodeURIComponent(page_title));
}

function add_watch_url(list) {
   return add_list_link(list, message_map.watch,
			script_path + '?title=' + page_name(specialns, "Watchunwatch")
			+ '&target=' + encodeURIComponent(page_title));
}

function create_link_element(list, action) {
   return add_list_link(list, message_map[action],
			script_path + '?action=' + action + '&title=' +
			encodeURIComponent(page_title));
}

function add_protect_url(list) {
    if (protected_page) {
        create_link_element(list, 'unprotect');
    } else {
        create_link_element(list, 'protect');
    }
    return true;
}

function add_delete_url(list) {
    create_link_element(list, 'delete');
}

function build_content_action_urls() {
     if (is_logged_in()) {
          var id = read_cookie(db_name + 'UserID');
          var p_cactions = document.getElementById('p-cactions');
          var list = p_cactions.getElementsByTagName('ul').item(0);

          add_move_url(list);
          add_watch_url(list);

          if (is_admin(id)) {
               add_delete_url(list);
               add_protect_url(list);
          }
     }
     return true;
}

