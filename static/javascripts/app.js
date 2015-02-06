'use strict';

/**
 * @ngdoc overview
 * @name mozArtApp
 * @description
 * # mozArtApp
 *
 * Main module of the application.
 */
var app = angular.module('mozArtApp', ['ngTagsInput', 'angularFileUpload']);

app.config(['$interpolateProvider', function($interpolateProvider){
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
}]);