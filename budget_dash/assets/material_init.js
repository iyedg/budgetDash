$(document).ready(function () {
    setTimeout(function () {
        M.AutoInit();
        $('#orgs').autocomplete({
            data: {
                "Apple": null,
                "Microsoft": null,
                "Google": 'https://placehold.it/250x250'
            },
        });
    }, 5000);
});