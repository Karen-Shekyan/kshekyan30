*Team Scooby-Doo Dog Erasers - Karen Shekyan, Gabriel Thompson, Russell Goyachev`* \
*SoftDev* \
*K12 -- Take and Give* \
*2022-10-17* \
*time spent: 0.5hrs*

### DISCO
 * GET requests send data to the web server as key/value pairs in the URL. Within the Python route, these arguments can be accessed through request.args
 * POST requests send data to the web server without them being written in the URL bar. They can only be accessed via request.form from the Python route, via request.form
    * `request.form` returns an `ImmutableMultiDict` containing the data sent to the route, and the data can be accessed via `request.form.get(key)`
 * To specify that an HTML form should force a POST request, you can add `method="post"` to the `<form>` tag
 * `request.method` returns the type of request (`GET` or `POST`)

### QCC
 * We noticed that `POST` doesn't show the form entry data in the URL bar. Would this make it better for entering passwords or other pieces of sensitive information?
 * Why is `request.form` used for `POST` requests, not `request.args`?
 * We noticed that routes can have multiple methods (both `GET` and `POST`). When would this be useful?
