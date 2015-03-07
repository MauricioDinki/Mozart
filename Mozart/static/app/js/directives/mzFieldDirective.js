'use strict';
/**
* @ngdoc function
* @name mozArtApp.directive:mzField
* @description
* # mzField
*
* Directive of the mozArtApp.
*/

app.directive('mzField', [function(){
  return {
    restrict: 'A',
    scope: false,
    transclude: false,
    link: function(scope, elem, attrs){
      var input = angular.element('#' + attrs.id);
    	input.focus(function(){
       	input.prev('label').removeClass('initial-label');
       	input.prev('label').addClass('active-label');
       	input.removeClass('empty-initial-field'); 
       	input.addClass('active-field');
    	});
    	input.blur(function(){
       	if(input.val()==''){
       	  input.removeClass('active-field');
       	  input.addClass('empty-initial-field'); 
       	}
       	input.prev('label').removeClass('active-label');
       	input.prev('label').addClass('initial-label');
    	});
    }
  }
}]);

