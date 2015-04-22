(function() {
  'use strict';

  function worksRequestService($http) {
    /* jshint validthis:true */
    var apiBaseUrl = '/api/worksets/';
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
  }

  worksRequestService.$inject = ['$http'];

  angular.module('mozArtApp')
    .service('worksRequest', worksRequestService);
})();