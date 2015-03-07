'use strict';
/**
* @ngdoc function
* @name mozArtApp.directive:mzMatch
* @description
* # mzMatch
*
* Directive of the mozArtApp.
*/

app.directive('mzMatch', [function(){
  return {
    restrict: 'A',
    require: 'ngModel',
    scope: {
      mzMatch: '='
    },
    link: function(scope, elem, attrs, ctrl){
      scope.compare = function(){
    		return scope.mzMatch === ctrl.$modelValue;
    	};
      scope.$watch(
      	scope.compare, 
      	function(currentValue) {
        	ctrl.$setValidity('match', currentValue);
      	}
      );
    }
  }
}]);

