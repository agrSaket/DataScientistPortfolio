import os
import requests
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    leetcode_data = {
        'total': '450+',
        'easy': '200',
        'medium': '180',
        'hard': '70',
        'easy_pct': 45,
        'medium_pct': 40,
        'hard_pct': 15,
    }
    
    username = os.getenv('LEETCODE_USERNAME')
    if username:
        try:
            query = """
            query getUserStats($username: String!) {
              matchedUser(username: $username) {
                submitStats {
                  acSubmissionNum {
                    difficulty
                    count
                  }
                }
              }
            }
            """
            response = requests.post(
                'https://leetcode.com/graphql', 
                json={'query': query, 'variables': {'username': username}},
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                stats = data.get('data', {}).get('matchedUser', {}).get('submitStats', {}).get('acSubmissionNum', [])
                
                if stats:
                    results = {item['difficulty']: item['count'] for item in stats}
                    total = results.get('All', 1) or 1
                    
                    leetcode_data = {
                        'total': results.get('All', 0),
                        'easy': results.get('Easy', 0),
                        'medium': results.get('Medium', 0),
                        'hard': results.get('Hard', 0),
                        'easy_pct': int((results.get('Easy', 0) / total) * 100),
                        'medium_pct': int((results.get('Medium', 0) / total) * 100),
                        'hard_pct': int((results.get('Hard', 0) / total) * 100),
                    }
        except Exception as e:
            print("Error fetching LeetCode stats:", e)

    return render(request, 'about.html', {'leetcode': leetcode_data})

def skills(request):
    return render(request, "skills.html")

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')
