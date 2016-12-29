<!DOCTYPE html>
<html lang="en">

<head>
	<title>Google Books Search Engine</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">

	<!-- Bootstrap CSS library and theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">


	<!-- Custom inline CSS. I would never do this typically but since this seems to be a one
			 file excersize for simplicity CSS is included here -->
	<style>
		header {
			text-align: center;
			padding: 20px;
		}

		h3 {
			font-weight: 300;
		}

		#searchArea {
			text-align: center;
		}

	</style>
</head>

<body>

	<div class="container">

		<header>
			<h1>Google Books Search Engine</h1>
			<h3>Type a book into the search bar to do :this:</h3>
		</header>

		<div id="searchArea" class="input-group col-md-8 col-md-offset-2">
    	<input id="searchBar" type="text" class="form-control" placeholder="Search for...">
    	<span class="input-group-btn">
      	<button id="searchBtn" class="btn btn-default" type="button">Go!</button>
    	</span>
  	</div>

		<div id="resultsArea">
			<ul id="results">
			</ul>
		</div>
	</div>

	<!-- Scripts -->
	<!-- JQuery 1.12.0 -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
	<!-- Bootstrap JS -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
	<!-- Custom JS -->
	<script type="text/javascript">
	/**
	 * 0) Remove the div with id="instructions".  You will be modifying this file.
	 *
	 * 1) Research the Google Books Volume API to determine
	 *    how to search for books given a query.
	 *	  https://developers.google.com/books/docs/v1/reference/volumes
	 *
	 *		https://www.googleapis.com/books/v1/volumes?q=search+terms?orderBy=relevance
	 *
	 * 2) You may use jQuery.
	 *
	 * 3) Given the following HTML, you are tasked with building a basic search engine
	 *    for Google Books.  There should be a search bar to input a query that will be
	 *	  be passed as an argument to the Google Books API.  The results should be rendered
	 *	  in the results area.  You must include at least (if available for the record):
	 *		+ Cover image
	 *		+ Title
	 *		+ Subtitle
	 *		+ Authors
	 *
	 *	  Additionally, each results should somehow provide a link to item's Google Books page.
	 *    hint: Look at a Google Books entry on Google Books, and see which parameter might help you.
	 *
	 * 4) Results should be styled logically, however, this isn't a design position, so don't feel
	 *	  like you have to impress us, although it should be presentable.
	 *
	 * 5) Each subsequent query should append its results to the results area.
	 *    There must be no duplicates (by Google Books id).
	 *
	 * 6) Note: While you must use the three function stubs provided below,
	 *    This will require you to write some code outside of them.
	 *
	 * 7) You should save your final product as googleBooks_codeTest_<your last name>.html
	 */

	/**
	 * Renders an error message
	 * @param msg {string} - error message to render
	 */
	function showError(msg) {
		var html = '<li><p class="error">' + msg + '</p></li>';
		$("#results").html(html);
	}

	/**
	 * Searches for books and returns a JSON list
	 * @param term {string} - search term
	 * @param callback {function} - do something with results
	 */
	function searchForBooks(term, callback) {
		// TODO
	}

	/**
	 * Render loadedBooks contents
	 * Generates HTML and sets #results's contents to it
	 */
	function render() {
		// TODO
	}
	</script>
</body>

</html>
