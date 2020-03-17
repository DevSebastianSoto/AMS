'use strict';
let project_list = []
$(document).ready(function () {
    project_list = $('.project-card');

    searchTag('search', function (matches) {
        $.each(project_list, function (indexInArray, valueOfElement) {
            $(valueOfElement).show();
        });
        if (matches.length > 0) {
            // Get valid Id's
            let valid_projects = [];
            $.each(matches, function (indexInArray, valueOfElement) {
                valid_projects.push($(valueOfElement).closest('div.project-card').attr('id'));
            });
            valid_projects = removeDups(valid_projects);
            //    hide not contained in list
            $.each(project_list, function (indexInArray, valueOfElement) {
                $(valueOfElement).hide();
            });

            $.each(project_list, function (indexInArray, valueOfElement) {
                let show = false;
                let i = 0;
                while (i < valid_projects.length && show == false) {
                    if ($(valueOfElement).attr('id') === valid_projects[i]) {
                        $(valueOfElement).show();
                        show = true;
                    }
                    i++;
                }
            });
        }
    });
});