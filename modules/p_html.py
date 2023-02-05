"""Module creates a static webpage"""
from datetime import date
from portfolio import TOTAL_MARKET_VALUE, CASH_FLOW, TOTAL_PL_PC, INTRADAY_PL, NET_ASSET_VALUE
from portfolio import TOP_10_HOLDINGS, CHART, STOCK_NEWS, COMPARISON

COMPANY = 'Cernunnos Capital'
HTML = f"""
<!doctype html>
<html lang="en">
   <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{ COMPANY }</title>
      <link rel="apple-touch-icon" sizes="180x180" href="favicon/apple-touch-icon.png">
      <link rel="icon" type="image/png" sizes="32x32" href="favicon/favicon-32x32.png">
      <link rel="icon" type="image/png" sizes="16x16" href="favicon/favicon-16x16.png">
      <link rel="manifest" href="favicon/site.webmanifest">
      <link rel="mask-icon" href="favicon/safari-pinned-tab.svg" color="#5bbad5">
      <meta name="msapplication-TileColor" content="#00aba9">
      <meta name="theme-color" content="#ffffff">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
   </head>
   <body>
      <main class="container">
         <img src="cc.png" alt="" width="200px" style="position: relative; bottom: 20px;">
         <div class="container px-4">
            <div class="row row-cols-1 row-cols-md-2 g-5">
               <div class="d-flex flex-column align-items-start py-5 gap-2">
                  <h3 class="fw-bold" style="color: #272643;">Automated Investing with Dynamic Rebalancing</h3>
                  <p class="text-muted">Actively managed and fundamentally oriented portfolio that identifies and captures compelling long-term investment opportunities</p>
                  <p class="fw-bold" style="color: #2b0080;">Inception Date: Nov 7, 2022</p>
                  <iframe src="https://embeds.beehiiv.com/2627520d-8805-48c6-98ea-4e2cfe71353a?slim=true" data-test-id="beehiiv-embed" frameborder="0" scrolling="no" style="margin: 0; border-radius: 0px !important; background-color: transparent;"></iframe>
               </div>
               <div class="d-flex flex-column align-items-start gap-2" style="padding: 0; margin: 0;">
                  <embed src="{ CHART }" width="100%" height="500">
               </div>

               <div class="d-flex flex-column align-items-start gap-2" style="margin: 0;">
                  <embed src="{ COMPARISON }" width="100%" height="400">
               </div>

               
               <div class="align-items-md-center">
                  <div class="row row-cols-2 g-5 text-center">
                     <div class="d-flex flex-column gap-2">
                           <div class="card">
                              <h1 class="fw-semibold mb-0" style="color: #2b0080; padding-top: 1rem;">${ NET_ASSET_VALUE }</h1>
                              <p class="text-muted">Net Asset Value</p>
                           </div>
                     </div>
               
                     <div class="d-flex flex-column gap-2">
                           <div class="card">
                              <h1 class="fw-semibold mb-0" style="color: #009688; padding-top: 1rem;">{ TOTAL_PL_PC }%</h1>
                              <p class="text-muted">Total Returns</p>
                           </div>
                     </div>
               
                     <div class="d-flex flex-column gap-2">
                           <div class="card">
                              <h1 class="fw-semibold mb-0" style="color: #2c698d; padding-top: 1rem;">{ INTRADAY_PL }</h1>
                              <p class="text-muted">Intraday Returns</p>
                           </div>
                     </div>
               
                     <div class="d-flex flex-column gap-2">
                           <div class="card">
                              <h1 class="fw-semibold mb-0" style="padding-top: 1rem;">${ CASH_FLOW }</h1>
                              <p class="text-muted">Cash Flow</p>
                           </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
         <h2 class="text-center" style="padding-top: 3rem;">Top 10 Holdings</h2>
         <p class="text-muted text-center">As of { date.today().strftime("%B %d, %Y") }</p>
         <div class="table-responsive">
            <table class="table table-bordered">
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
