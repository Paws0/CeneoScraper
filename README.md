# CeneoScraper
## Etap 1 - Pobranie składowych pojedzynczej opinii o wybranym produkcie z serwisu [Ceneo.pl](https://www.ceneo.pl/)
* pobranie kodu pojedynczej strony z opiniami o wskazanym produkcie (done)
*  Analiza kodu HTML pojedynczej opinii

|Składowa opinii|Celektor CSS|Nazwa zmiennej|Typ danych|
|:--------------|:-----------|:-------------|:---------|
|Opinia|`div.js_product-review`|opinion||
|Identyfikator opinii|`["data-entry-id"]`|opinion_id||
|Autor|`span.user-post__author-name`|author||
|Rekomendacja|`span.user-post__author-recomendation`|recomm||
|Liczba gwiazdek|`span.user-post__score-count`|stars||
|Treść|`div.user-post__text`|content||
|Lista zalet|`review-feature__col:has(> div.review-feature__title--positives) > review-feature__item` <br> `review-feature__col:has(> div[class*="positives") > review-feature__item` <br> `div.review-feature__title--positives ~ review-feature__item`|pros||
|Lista wad|`review-feature__col:has(> div.review-feature__title--negatives) > review-feature__item` <br> `review-feature__col:has(> div[class*="negatives") > review-feature__item` <br> `div.review-feature__title--negatives ~ review-feature__item`|cons||
|Dla ilu osób użyteczna|`span[id^="votes-yes"]` <br> `button.vote-yes > span` <br> `button.vote-yes["data-total-vote"]`|useful||
|Dla ilu osób nieużyteczna|`span[id^="votes-no"]` <br> `button.vote-no > span` <br> `button.vote-no["data-total-vote"]`|useless||
|Czy opinia potwierdzona zakupem|`div.review-pz`|purchased||
|Data wystawienia opinii|`span.user-post__published > time:nth-child(1)["datetime"]`|publish_date||
|Data zakupu produktu|`span.user-post__published > time:nth-child(2)["datetime"]`|purchase_date||
