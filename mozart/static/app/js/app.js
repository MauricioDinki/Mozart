(function () {
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

    function getMonthAbbreviation() {
        return function (monthNumber) {
            var monthAbbreviations = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec' ];
            return monthAbbreviations[monthNumber - 1];
        };
    }

    function getHoursMinutes() {
        return function (fullTime) {
            var array = fullTime.split(':');
            return array[0] + ':' + array[1];
        };
    }

    angular
        .module('mozArtApp', ['ng.django.forms', 'ngAnimate', 'offClick', 'matchmedia-ng', 'hmTouchEvents', 'asModalDialogs'])
        .config(appConfig)
        .value('workUrl', getWorkUrl)
        .value('profileUrl', getUserProfile)
        .filter('monthAbbreviation', getMonthAbbreviation)
        .filter('hoursMinutes', getHoursMinutes);
}());