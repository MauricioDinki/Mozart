(function () {
    'use strict';

    function baseRequestsController() {
        /* jshint validthis:true */
        this.getController = function ($scope, arrayName, getFunctionName, requestFunction, filterFunction, filterAttribute, extraFunctions, parameters) {
            var scope, getItems;
            scope = $scope;
            scope[arrayName] = [];
            scope.showMessage = false;
            scope.pageNumber = 1;
            getItems = function () {
                requestFunction(
                    function (apiResults) {
                        var resultsArray,  nextPage, prevSize;
                        resultsArray = apiResults.results;
                        nextPage = apiResults.next;
                        prevSize = scope[arrayName].length;
                        resultsArray.forEach(function (item) {
                            var filterObject, isRepeated, extraFilters;
                            filterObject = {};
                            extraFilters = true;
                            filterObject[filterAttribute] = item[filterAttribute];
                            isRepeated = filterFunction(scope[arrayName], filterObject);
                            if (extraFunctions[1]) {
                                extraFilters = extraFunctions[1](item);
                            }
                            if (!isRepeated && extraFilters) {
                                item = extraFunctions[0](item);
                                scope[arrayName].push(item);
                            }
                        });
                        // for(var i in resultsArray) {
                        //     var item = resultsArray[i];
                        //     var filterObject = {};
                        //     filterObject[filterAttribute] = item[filterAttribute];
                        //     var isRepeated = filterFunction(scope[arrayName], filterObject);
                        //     var extraFilters = true;
                        //     if (extraFunctions[1]) {
                        //         extraFilters = extraFunctions[1](item);
                        //     }
                        //     if (!isRepeated && extraFilters) {
                        //         item = extraFunctions[0](item);
                        //         scope[arrayName].push(item);
                        //     }
                        // }
                        if (nextPage !== null) {
                            scope.pageNumber += 1;
                        }
                        scope.showMessage = (prevSize === scope[arrayName].length);
                    },
                    parameters,
                    scope.pageNumber
                );
            };
            scope[getFunctionName] = getItems;
            return scope;
        };
    }

    angular.module('mozArtApp')
        .service('baseController', baseRequestsController);
}());