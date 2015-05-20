(function() {
  'use strict';

  function worksRequestService($http, $filter) {
    /* jshint validthis:true */
    var apiBaseUrl = '/api/worksets/';
    this.recentWorks = {
      get:function(fnOK,fnError, category, author, pageNumber) {
        $http({
          method: 'GET',
          url: apiBaseUrl + '?' + 'category=' + category + '&author=' + author +  '&page=' + pageNumber
        })
        .success(function(data, status, headers, config) {
          fnOK(data.results, data.next);
        })
        .error(function(data, status, headers, config) {
          fnError(data,status);
        });
      }
    };
    this.randomWorks = {
      get:function(fnOK,fnError, category, author, pageNumber) {
        $http({
          method: 'GET',
          url: apiBaseUrl + '?' + 'category=' + category + '&author=' + author +  '&page=' + pageNumber
        })
        .success(function(data, status, headers, config) {
          fnOK(data.results, data.next);
        })
        .error(function(data, status, headers, config) {
          fnError(data,status);
        });
      }
    };
    this.checkRepeatedWork = function(worksArray, work) {
      return $filter('filter')(
        worksArray,
        work
      )[0];
    };
  }

  worksRequestService.$inject = ['$http', '$filter'];

  angular.module('mozArtApp')
    .service('worksRequest', worksRequestService);
})();