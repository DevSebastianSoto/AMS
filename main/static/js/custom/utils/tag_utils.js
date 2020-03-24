'use strict';

function searchTag(searchInput, cb) {
    const input = $('#' + searchInput);
    input.on('keyup', function () {
        if (input.val().length > 0) {
            let tag_list = $('span[name*="' + input.val().toLowerCase() + '"]');
            if (tag_list.length > 0)
                cb(tag_list);
        }else{
            cb([]);
        }
    });
}

function removeDups(list) {
    let unique = {};
    list.forEach(function (i) {
        if (!unique[i]) {
            unique[i] = true;
        }
    });
    return Object.keys(unique);
}