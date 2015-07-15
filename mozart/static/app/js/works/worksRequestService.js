(function() {
  'use strict';

  function worksRequestService($http, $filter) {
    /* jshint validthis:true */
    var apiBaseUrl = '/api/worksets/';
    this.recentWorks = {
      get:function(fnOK,fnError, category, author, pageNumber) {
        var requestUrl;
        if(category === 'all' && author === 'all') {
          requestUrl = apiBaseUrl + '?page=' + pageNumber;
        }
        else if(category === 'all') {
          requestUrl = apiBaseUrl + '?user=' + author + '&page=' + pageNumber;
        }
        else if(author==='all') {
          requestUrl = apiBaseUrl + '?category=' + category + '&page=' + pageNumber;
        }
        else {
          requestUrl = apiBaseUrl + '?user=' + author +  '&category=' + category + '&page=' + pageNumber;
        }
        $http({
          method: 'GET',
          url: requestUrl
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
        var requestUrl;
        if(category === 'all' && author === 'all') {
          requestUrl = apiBaseUrl + '?page=' + pageNumber;
        }
        else if(category === 'all') {
          requestUrl = apiBaseUrl + '?user=' + author + '&page=' + pageNumber;
        }
        else {
          requestUrl = apiBaseUrl + '?category=' + category + '&page=' + pageNumber;
        }
        $http({
          method: 'GET',
          url: requestUrl
        })
        .success(function(data, status, headers, config) {
          fnOK(data.results, data.next);
        })
        .error(function(data, status, headers, config) {
          fnError(data,status);
        });
      }
    };
    this.checkRepeatedWork = function(worksArray, work, ex) {
      return $filter('filter')(
        worksArray,
        work,
        true
      )[0] ? true: false;
    };
  }

  worksRequestService.$inject = ['$http', '$filter'];

  angular.module('mozArtApp')
    .service('worksRequest', worksRequestService);
})();