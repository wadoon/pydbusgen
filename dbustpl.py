#!/usr/bin/python


__author__="Alexander Weigl <alexweigl@gmail.com>"
__date__=""
__version__="0.1"


import dbus


__all__= ( 'SERVICENAME', 'PATH',
           '${proxy_name}',
%for item in items:
% if item:
%  if item['item_type'] == 'signal':
           'signal_${item['name']},'
%  else:
           '${item['name']},'
%  endif
% endif
%endfor
        ) 

SERVICENAME='${serviceName}'
INTERFACE='${interface}'
PATH='${path}'

__sessionBus = dbus.SessionBus()
${proxy_name} = dbus.Interface( __sessionBus.get_object(SERVICENAME, PATH) ,
                                dbus_interface=INTERFACE )
    

% for item in items:
    
% if item:
%if item['item_type'] == 'signal':
def signal_${item['name']}( callback , ${item['args']} ):
    '''${item['doc']}'''
    return ${proxy_name}.connect_to_signal("${item['name']}", callback, None)    
%else:
def ${item['name']}( ${item['args']} ):
    '''${item['doc']}'''
    return ${proxy_name}.${item['name']}(${item['args']})
%endif
%endif
%endfor
