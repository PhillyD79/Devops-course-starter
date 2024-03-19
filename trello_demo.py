var client = new HttpClient();
var request = new HttpRequestMessage();
request.RequestUri = new Uri("https://api.trello.com/1/boards/65e5d7fb5e09969f4df0252d/lists?key=5873a30945dd9886b74ed129e7ad8cc7&token=ATTAd5ad29547411987e60cecc7a781ac4993a90773e26cc6a298988378887ae03ce8F55EDEC");
request.Method = HttpMethod.Get;

request.Headers.Add("Accept", "*/*");
request.Headers.Add("User-Agent", "Thunder Client (https://www.thunderclient.com)");

var response = await client.SendAsync(request);
var result = await response.Content.ReadAsStringAsync();
Console.WriteLine(result);