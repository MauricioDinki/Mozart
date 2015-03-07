'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:worksRequest
 * @description
 * #worksRequest
 * Service of the mozArtApp
 */

app.service('worksRequest', ['$http',  function($http){
  var apiBaseUrl = 'http://mozart.com:8000/api/worksets/';
  this.recentWorks = { 
    get:function(fnOK,fnError, category, author, paginate) {
      $http({
        method: 'GET',
        url: apiBaseUrl + '?' + 'category=' + category + '&author=' + author +  '&paginate=' + paginate
      })
      .success(function(data, status, headers, config) {
        fnOK(data);
      })
      .error(function(data, status, headers, config) {
        fnError(data,status);
      });
    }
  };
  this.randomWorks = {
    get:function(fnOK,fnError, category, author, paginate) {
      $http({
        method: 'GET',
        url: apiBaseUrl + '?' + 'category=' + category + '&author=' + author +  '&paginate=' + paginate
      })
      .success(function(data, status, headers, config) {
        fnOK(data);
      })
      .error(function(data, status, headers, config) {
        fnError(data,status);
      });
    }
  };
}]);
