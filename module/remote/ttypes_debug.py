#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autogenerated by pyload
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

from ttypes import *

classes = {

'AccountInfo' : {
	'plugin': basestring,
	'loginname': basestring,
	'owner': int,
	'valid': bool,
	'validuntil': int,
	'trafficleft': int,
	'maxtraffic': int,
	'premium': bool,
	'activated': bool,
	'shared': bool,
	'options': (dict, basestring, basestring),
},
'AddonInfo' : {
	'func_name': basestring,
	'description': basestring,
	'value': basestring,
},
'AddonService' : {
	'func_name': basestring,
	'description': basestring,
	'arguments': (list, basestring),
	'media': int,
},
'ConfigHolder' : {
	'name': basestring,
	'label': basestring,
	'description': basestring,
	'long_description': basestring,
	'items': (list, ConfigItem),
	'info': (list, AddonInfo),
	'handler': (list, InteractionTask),
},
'ConfigInfo' : {
	'name': basestring,
	'label': basestring,
	'description': basestring,
	'saved': bool,
	'activated': bool,
},
'ConfigItem' : {
	'name': basestring,
	'label': basestring,
	'description': basestring,
	'type': basestring,
	'default_value': basestring,
	'value': basestring,
},
'DownloadInfo' : {
	'url': basestring,
	'plugin': basestring,
	'hash': basestring,
	'status': int,
	'statusmsg': basestring,
	'error': basestring,
},
'DownloadProgress' : {
	'fid': int,
	'pid': int,
	'speed': int,
	'status': int,
},
'EventInfo' : {
	'eventname': basestring,
	'event_args': (list, basestring),
},
'FileDoesNotExists' : {
	'fid': int,
},
'FileInfo' : {
	'fid': int,
	'name': basestring,
	'package': int,
	'owner': int,
	'size': int,
	'status': int,
	'media': int,
	'added': int,
	'fileorder': int,
	'download': DownloadInfo,
},
'InteractionTask' : {
	'iid': int,
	'input': int,
	'data': (list, basestring),
	'output': int,
	'default_value': basestring,
	'title': basestring,
	'description': basestring,
	'plugin': basestring,
},
'LinkStatus' : {
	'url': basestring,
	'name': basestring,
	'plugin': basestring,
	'size': int,
	'status': int,
	'packagename': basestring,
},
'OnlineCheck' : {
	'rid': int,
	'data': (dict, basestring, LinkStatus),
},
'PackageDoesNotExists' : {
	'pid': int,
},
'PackageInfo' : {
	'pid': int,
	'name': basestring,
	'folder': basestring,
	'root': int,
	'owner': int,
	'site': basestring,
	'comment': basestring,
	'password': basestring,
	'added': int,
	'tags': (list, basestring),
	'status': int,
	'packageorder': int,
	'stats': PackageStats,
	'fids': (list, int),
	'pids': (list, int),
},
'PackageStats' : {
	'linkstotal': int,
	'linksdone': int,
	'sizetotal': int,
	'sizedone': int,
},
'ProgressInfo' : {
	'plugin': basestring,
	'name': basestring,
	'statusmsg': basestring,
	'eta': int,
	'format_eta': basestring,
	'done': int,
	'total': int,
	'download': DownloadProgress,
},
'ServerStatus' : {
	'pause': bool,
	'active': int,
	'queue': int,
	'total': int,
	'speed': int,
	'download': bool,
	'reconnect': bool,
},
'ServiceDoesNotExists' : {
	'plugin': basestring,
	'func': basestring,
},
'ServiceException' : {
	'msg': basestring,
},
'TreeCollection' : {
	'root': PackageInfo,
	'files': (dict, int, FileInfo),
	'packages': (dict, int, PackageInfo),
},
'UserData' : {
	'uid': int,
	'name': basestring,
	'email': basestring,
	'role': int,
	'permission': int,
	'folder': basestring,
	'traffic': int,
	'dllimit': int,
	'dlquota': basestring,
	'hddquota': int,
	'user': int,
	'templateName': basestring,
},
'UserDoesNotExists' : {
	'user': basestring,
},
}

methods = {
	'addFromCollector': int,
	'addLinks': None,
	'addLocalFile': None,
	'addPackage': int,
	'addPackageChild': int,
	'addPackageP': int,
	'addToCollector': None,
	'addUser': UserData,
	'callAddon': None,
	'callAddonHandler': None,
	'checkOnlineStatus': OnlineCheck,
	'checkOnlineStatusContainer': OnlineCheck,
	'checkURLs': (dict, basestring, list),
	'configurePlugin': ConfigHolder,
	'createPackage': int,
	'deleteCollLink': None,
	'deleteCollPack': None,
	'deleteConfig': None,
	'deleteFiles': None,
	'deletePackages': None,
	'findFiles': TreeCollection,
	'freeSpace': int,
	'generateAndAddPackages': (list, int),
	'generateDownloadLink': basestring,
	'generatePackages': (dict, basestring, list),
	'getAccountTypes': (list, basestring),
	'getAccounts': (list, AccountInfo),
	'getAddonHandler': (dict, basestring, list),
	'getAllFiles': TreeCollection,
	'getAllInfo': (dict, basestring, list),
	'getAllUserData': (dict, int, UserData),
	'getCollector': (list, LinkStatus),
	'getConfig': (dict, basestring, ConfigHolder),
	'getEvents': (list, EventInfo),
	'getFileInfo': FileInfo,
	'getFileTree': TreeCollection,
	'getFilteredFileTree': TreeCollection,
	'getFilteredFiles': TreeCollection,
	'getGlobalPlugins': (list, ConfigInfo),
	'getInfoByPlugin': (list, AddonInfo),
	'getInteractionTask': InteractionTask,
	'getLog': (list, basestring),
	'getNotifications': (list, InteractionTask),
	'getPackageContent': TreeCollection,
	'getPackageInfo': PackageInfo,
	'getProgressInfo': (list, ProgressInfo),
	'getServerVersion': basestring,
	'getUserData': UserData,
	'getUserPlugins': (list, ConfigInfo),
	'hasAddonHandler': bool,
	'isInteractionWaiting': bool,
	'isTimeDownload': bool,
	'isTimeReconnect': bool,
	'kill': None,
	'login': bool,
	'moveFiles': bool,
	'movePackage': bool,
	'orderFiles': None,
	'orderPackage': None,
	'parseURLs': (dict, basestring, list),
	'pauseServer': None,
	'pollResults': OnlineCheck,
	'recheckPackage': None,
	'removeAccount': None,
	'removeUser': None,
	'renameCollPack': None,
	'restart': None,
	'restartFailed': None,
	'restartFile': None,
	'restartPackage': None,
	'saveConfig': None,
	'setConfigHandler': None,
	'setInteractionResult': None,
	'setPackageData': None,
	'setPackageFolder': bool,
	'setPackagePaused': None,
	'setPassword': bool,
	'statusServer': ServerStatus,
	'stopAllDownloads': None,
	'stopDownloads': None,
	'togglePause': bool,
	'toggleReconnect': bool,
	'unpauseServer': None,
	'updateAccount': None,
	'updateAccountInfo': None,
	'updateUserData': None,
	'uploadContainer': int,
}