"""Module creates a static webpage"""
from datetime import date
from portfolio import TOTAL_MARKET_VALUE, TOTAL_COST_BASIS, TOTAL_PL_PC, INTRADAY_PL
from portfolio import TOP_10_HOLDINGS, CHART, STOCK_NEWS

COMPANY = 'auto{invest}'
HTML = f"""
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
            <h2 class="pb-2 border-bottom">{ COMPANY }</h2>
            <div class="row row-cols-1 row-cols-md-2 align-items-md-center g-5 py-5">
               <div class="d-flex flex-column align-items-start gap-2">
                  <h3 class="fw-bold" style="color: #272643;">Automated Investing with Dynamic Rebalancing</h3>
                  <p class="text-muted">Actively managed and fundamentally oriented portfolio that identifies and captures compelling long-term investment opportunities</p>
                  <p class="fw-bold" style="color: #2b0080;">Inception Date: Nov 7, 2022</p>
                  <a href="https://github.com/atreyasinha/autoinvest" target="_blank" class="btn btn-dark btn-lg">Source Code</a>
               </div>
               <div class="d-flex flex-column align-items-start gap-2" style="padding: 0; margin: 0;">
                  <embed src="{ CHART }" width="100%" height="500">
               </div>
            </div>
            <div class="row text-center g-5">
               <div class="col">
                  <div class="card">
                     <h1 class="fw-semibold mb-0" style="color: #2b0080; padding-top: 1rem;">${ TOTAL_MARKET_VALUE }</h1>
                     <p class="text-muted">Net Asset Value</p>
                  </div>
               </div>
               <div class="col">
                  <div class="card">
                     <h1 class="fw-semibold mb-0" style="color: #009688; padding-top: 1rem;">{ TOTAL_PL_PC }</h1>
                     <p class="text-muted">Total Returns</p>
                  </div>
               </div>
               <div class="col">
                  <div class="card">
                     <h1 class="fw-semibold mb-0" style="color: #2c698d; padding-top: 1rem;">{ INTRADAY_PL }</h1>
                     <p class="text-muted">Intraday Returns</p>
                  </div>
               </div>
               <div class="col">
                  <div class="card">
                     <h1 class="fw-semibold mb-0" style="padding-top: 1rem;">{ TOTAL_COST_BASIS }</h1>
                     <p class="text-muted">S&P 500</p>
                  </div>
               </div>
            </div>
         </div>
         <h2 class="text-center" style="padding-top: 3rem;">Top 10 Holdings</h2>
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
               <tbody>
                  { TOP_10_HOLDINGS }
               </tbody>
            </table>
         </div>
         <div class="container py-5">
            <div class="row mb-2">
               { STOCK_NEWS }
            </div>
         </div>
         <footer class="py-3 my-4 border-top">
            <p class="text-muted">DISCLOSURE</p>
            <p><small class="text-muted">All statements made regarding companies, securities or other financial information on this site are strictly beliefs and points of view held by { COMPANY } and are subject to change without notice. Certain information on this site was obtained from sources that { COMPANY } believes to be reliable; however, { COMPANY } does not guarantee the accuracy or completeness of any information obtained from any third party. The information on this site is for informational purposes only and should not be considered as investment advice or a recommendation of any particular security, strategy or investment product. The information on this site is general in nature and should not be considered legal or tax advice. An investor should consult a financial professional, an attorney, or tax professional regarding the investor’s specific situation.</small></p>

            <p><small class="text-muted">Certain hyperlinks or referenced websites on this site may, for your convenience, forward you to third parties' websites, which generally are recognized by their top level domain name. Any descriptions of, references to, or links to other products, publications or services do not constitute an endorsement, authorization, sponsorship or affiliation with { COMPANY } with respect to any linked site or its sponsor, unless expressly stated by { COMPANY }. Any such information, products or sites have not necessarily been reviewed by { COMPANY } and are provided or maintained by third parties over whom { COMPANY } exercises no control. { COMPANY } expressly disclaims any responsibility for the content, the accuracy of the information, and/or the quality of products or services provided by or advertised on these third-party sites. { COMPANY } reserves the right to terminate any hyperlink or hyperlinking program at any time.</small></p>
            <p><small class="text-muted">© { date.today().strftime("%Y") } { COMPANY }, Inc</small></p>
         </footer>
      </main>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
   </body>
</html>
"""

with open('index.html', 'w', newline='', encoding='utf8') as f:
    f.write(HTML)
    f.close()
