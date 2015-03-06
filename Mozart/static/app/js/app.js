'use strict';

/**
 * @ngdoc overview
 * @name mozArtApp
 * @description
 * # mozArtApp
 *
 * Main module of the application.
 */
var app = angular.module('mozArtApp', ['ng.django.forms', 'offClick']);

app.config(['$interpolateProvider', '$httpProvider', function($interpolateProvider, $httpProvider){
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
}]);
