using System.Net.Http.Headers;

class Program
{
    private static readonly HttpClient _client = new HttpClient();
    private static readonly string _cookieSessionHeader = Environment.GetEnvironmentVariable("SESSION_COOKIE");
    private static readonly string _url = "https://adventofcode.com/2024/day/1/input";

    private static async Task Main(string[] args)
    {
        List<int> firstList = new List<int>();
        List<int> secondList = new List<int>();
        int minFirst;
        int minSecond;
        int distance;

        int totalDistance = 0;

        if (_cookieSessionHeader == null)
        {
            throw new Exception("Adjust your session cookie");
        }

        try
        {
            string historianslists = await GetInput(_url);
            SeparateList(historianslists, ref firstList, ref secondList);
            while (firstList.Count > 0)
            {
                minFirst = firstList.Min();
                minSecond = secondList.Min();
                distance = minFirst >= minSecond ? minFirst - minSecond : minSecond - minFirst;

                totalDistance += distance;
                firstList.Remove(minFirst);
                secondList.Remove(minSecond);
            }
            Console.WriteLine($"Total Distance : {totalDistance}");
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"Erreur HTTP : {ex.Message}");
        }
        catch (SplitException ex)
        {
            Console.WriteLine($"Erreur Split : {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Erreur generique : {ex.Message}");
        }
    }

    private static async Task<string> GetInput(string url)
    {
        HttpRequestHeaders headers = _client.DefaultRequestHeaders;
        headers.Add("Cookie", _cookieSessionHeader);
        HttpResponseMessage response = await _client.GetAsync(url);
        response.EnsureSuccessStatusCode();
        return await response.Content.ReadAsStringAsync();
    }

    private static void SeparateList(string historianslists, ref List<int> firstList, ref List<int> secondList)
    {
        foreach (string line in historianslists.Split("\n", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries))
        {
            string[] parts = line.Split(" ", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);

            if (parts.Length == 2)
            {
                firstList.Add(int.Parse(parts[0]));
                secondList.Add(int.Parse(parts[1]));
            }
            else
            {
                throw new SplitException("There was not an equal amount of id in both list");
            }
        }
    }

    public class SplitException : Exception
    {
        public SplitException(string message) : base(message) { }
    }
}
