
## Models
 - One can say, that `Status` can be implemented via `choices`. That's true, but it's not ideal since it's not editable via API (without explicit implementation).
 - `on_delete` behavior is debatable and would depend on other factors, current behavior was choosen without extensive thinking.
 - To store or not to store stats (resolution time, etc...)? Calculating them during saving process is easy, but takes space. Calculating them during retrieval takes time and resources.  

## Views
 - Pretty straightforward in this case, no need to over-complicate it for no real reason.

## Serializers
 - I'm not big fan of `rest_frameworks`'s serializers. It takes too much code to optimize queries in case of "deep" relations - might use experimental `serpy` module, which can be easily rewritten to work similar to `ModelSerializer`.