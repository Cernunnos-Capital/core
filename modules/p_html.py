from datetime import date
from portfolio import data, total_market_value, total_cost_basis, total_pl, intraday_pl

message = f"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>autoinvest</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
  </head>
  <body>
    <main class="container">
        <div class="container px-4 py-5">
        <h2 class="pb-2 border-bottom">auto{{invest}}</h2>
    
        <div class="row row-cols-1 row-cols-md-2 align-items-md-center g-5 py-5">
          <div class="d-flex flex-column align-items-start gap-2">
            <h3 class="fw-bold" style="color: #272643;">Automated Investing with Dynamic Rebalancing</h3>
            <p class="text-muted">Actively managed and fundamentally oriented portfolio that identifies and captures compelling long-term investment opportunities</p>
            <a href="https://github.com/atreyasinha/autoinvest" target="_blank" class="btn btn-dark btn-lg">Source Code</a>
          </div>
          <div class="row row-cols-2 row-cols-sm-2 g-5">
            <div class="d-flex flex-column gap-2">
              <h1 class="fw-semibold mb-0" style="color: #ff4500;">${ total_market_value }</h1>
              <p class="text-muted">Market Value</p>
            </div>
    
            <div class="d-flex flex-column gap-2">
              <h1 class="fw-semibold mb-0">${ total_cost_basis }</h1>
              <p class="text-muted">Cost Basis</p>
            </div>
    
            <div class="d-flex flex-column gap-2">
              <h1 class="fw-semibold mb-0">{ total_pl }</h1>
              <p class="text-muted">Total Returns</p>
            </div>
    
            <div class="d-flex flex-column gap-2">
              <h1 class="fw-semibold mb-0" style="color: #2c698d;">{ intraday_pl }</h1>
              <p class="text-muted">Intraday Returns</p>
            </div>
          </div>
        </div>
      </div>



        <h2 class="display-6 text-center mb-4">Top 10 Holdings</h2>
        <p class="text-muted text-center">As of { date.today().strftime("%B %d, %Y") }</p>
        <div class="table-responsive">
        <table class="table">
          <thead>
            <tr>
              <th style="width: 40%;"></th>
              <th style="width: 15%;">Weight (%)</th>
              <th style="width: 15%;">Avg Entry ($)</th>
              <th style="width: 15%;">Today's P/L (%)</th>
              <th style="width: 15%;">Total P/L (%)</th>
            </tr>
          </thead>

            { data }

          <tbody>

          </tbody>
        </table>
        </div>

        <footer class="py-3 my-4">
            <p class="text-center text-muted">© { date.today().strftime("%Y") } autoinvest, Inc</p>
        </footer>
    </main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
  </body>
</html>
"""

with open('index.html', 'w', newline='', encoding='utf8') as f:
    f.write(message)
    f.close()
