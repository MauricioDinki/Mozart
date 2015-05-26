(function() {
	'use strict';

	function appConfig($interpolateProvider, $httpProvider) {
		$interpolateProvider.startSymbol('{$');
		$interpolateProvider.endSymbol('$}');
		$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	}

	appConfig.$inject = ['$interpolateProvider', '$httpProvider'];

	function getWorkUrl(username, workSlug) {
		return '/profiles/' + username + '/works/' + workSlug;
	}

	function getUserProfile(username) {
		return '/profiles/' + username;
	}

	angular
		.module('mozArtApp', ['ng.django.forms', 'ngAnimate', 'offClick', 'matchmedia-ng', 'hmTouchEvents'])
		.config(appConfig)
		.value('workUrl', getWorkUrl)
		.value('profileUrl', getUserProfile);
})();
