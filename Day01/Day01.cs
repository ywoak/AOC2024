using System.Net.Http.Headers;

public class DefaultDictionary<TKey, TValue> : Dictionary<TKey, TValue> where TKey : notnull
{
    private Func<TValue> _defaultFactory;

    public DefaultDictionary(Func<TValue> defaultFactory)
    {
        _defaultFactory = defaultFactory;
    }

    public new TValue this[TKey key]
    {
        get
        {
            if (!ContainsKey(key))
            {
                this[key] = _defaultFactory();
            }
            return base[key];
        }
        set { base[key] = value; }
    }
}

class Program
{
    private static readonly HttpClient _client = new HttpClient();
    private static readonly string _cookieSessionHeader = Environment.GetEnvironmentVariable("SESSION_COOKIE");
    private static readonly string _url = "https://adventofcode.com/2024/day/1/input";

    private static async Task Main(string[] args)
    {
        List<int> left = new List<int>();
        List<int> right = new List<int>();
        DefaultDictionary<int, int> right_counter = new DefaultDictionary<int, int>(() => 0);

        if (_cookieSessionHeader == null)
        {
            throw new Exception("Adjust your session cookie");
        }

        try
        {
            string historianslists = await GetInput(_url);
            SeparateList(historianslists, ref left, ref right);
            Console.WriteLine($"Distance    : {GetDistanceAndCounter(left, right, ref right_counter)}");
            Console.WriteLine($"Similarity  : {GetSimilarityScore(left, right_counter)}");
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

    private static void SeparateList(string historianslists, ref List<int> left, ref List<int> right)
    {
        foreach (string line in historianslists.Split("\n", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries))
        {
            string[] parts = line.Split(" ", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);

            if (parts.Length == 2)
            {
                left.Add(int.Parse(parts[0]));
                right.Add(int.Parse(parts[1]));
            }
            else
            {
                throw new SplitException("There was not an equal amount of id in both list");
            }
        }
    }

    private static int GetDistanceAndCounter(List<int> left, List<int> right, ref DefaultDictionary<int, int> right_counter)
    {
        int distance = 0;

        left.Sort();
        right.Sort();

        for (int i = 0; i < left.Count(); i++)
        {
            right_counter[right[i]] += 1;
            distance += Math.Abs(left[i] - right[i]);
        }
        return distance;
    }

    private static int GetSimilarityScore(List<int> left, DefaultDictionary<int, int> right_counter)
    {
        int similarityScore = 0;

        foreach (int id in left)
        {
            similarityScore += id * right_counter[id];
        }

        return similarityScore;
    }

    public class SplitException : Exception
    {
        public SplitException(string message) : base(message) { }
    }
}
