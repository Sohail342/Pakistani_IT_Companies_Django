from django.shortcuts import render
from .models import Company
import json
from django.db import connection
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def dashboard(request):
    
    total_companies = Company.objects.count()
    # companies count
    in_karachi = Company.objects.filter(location='Karachi,Pakistan').count()
    in_lahore = Company.objects.filter(location='Lahore,Pakistan').count()
    in_Islamabad = Company.objects.filter(location='Islamabad,Pakistan').count() 
    in_rawalpindi = Company.objects.filter(location='Rawalpindi,Pakistan').count()
    in_sialkot =    Company.objects.filter(location='Sialkot,Pakistan').count()   
    in_faisalabad =    Company.objects.filter(location='Faisalabad,Pakistan').count()  
    in_bahawalpur  = Company.objects.filter(location='Bahawalpur,Pakistan').count()  
    
    # most rated companies location wise
    rating_karachi = Company.objects.filter(location='Karachi,Pakistan', rating=5).count()
    rating_lahore = Company.objects.filter(location='Lahore,Pakistan', rating=5).count()
    rating_Islamabad = Company.objects.filter(location='Islamabad,Pakistan', rating=5).count() 
    rating_rawalpindi = Company.objects.filter(location='Rawalpindi,Pakistan', rating=5).count()
    rating_sialkot =    Company.objects.filter(location='Sialkot,Pakistan', rating=5).count()   
    
    # Top Cards
    query_set = {
        'total':{'total_companies':total_companies, "icon":'person', 'location':"in Pakistan", "color":"dark"},
        "in_karachi":{'total_companies':in_karachi, "icon":'person', 'location':"in Karachi", "color":"success"},
        "in_lahore":{'total_companies':in_lahore, "icon":'person', 'location':"in Lahore", "color":"primary"},
        "in_islamabad":{'total_companies':in_Islamabad, "icon":'person', 'location':"in Islamabad", "color":"info"},
        "in_rawalpindi":{'total_companies':in_rawalpindi, "icon":'person', 'location':"in Rawalpindi", "color":"info"},
        "in_sialkot":{'total_companies':in_sialkot, "icon":'person', 'location':"in Sialkot", "color":"primary"},
        "in_faisalabad":{'total_companies':in_faisalabad, "icon":'person', 'location':"in Faisalabad", "color":"success"},
        "in_bahawalpur":{'total_companies':in_bahawalpur, "icon":'person', 'location':"in Bahawalpur", "color":"dark"},
    }
    
    # Chart data
    chart_data = {
    'labels': ['Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Sialkot'],
    'doughnut_data': [in_karachi, in_lahore, in_Islamabad, in_rawalpindi, in_sialkot],
    'bar_data': [rating_karachi, rating_lahore, rating_Islamabad, rating_rawalpindi, rating_sialkot],
    }
    
    # Clients Table
    Client = fetch_company_details()
    
    context = {
        'clients':Client,
        'query_set':query_set,
        'chart_data':json.dumps(chart_data)  # Convert dict to Json
    }
    
    return render(request, 'dashboard.html', context)
    
@login_required()
def tables(request):
    # Raw Sql Queries
    top_rated = Company.objects.raw('''
                                    
        SELECT id, company_name, location, 
        rating FROM core_company 
        WHERE rating >= 5
                                    
            ''')
    
    karachi_companies = Company.objects.raw('''
                                    
        SELECT id, company_name, location, 
        rating FROM core_company 
        WHERE location = 'Karachi,Pakistan'
                                    
            ''')
    
    lahore_companies = Company.objects.raw('''
        
        SELECT id, company_name, location, 
        rating FROM core_company 
        WHERE location = 'Lahore,Pakistan'
                                
        ''')
    
    islamabad_companies = Company.objects.raw('''
                                
        SELECT id, company_name, location, 
        rating FROM core_company 
        WHERE location = 'Islamabad,Pakistan'
                                
        ''')

    query_set = {
        "top_rated":top_rated, 
        "karachi_companies":karachi_companies,
        "lahore_companies":lahore_companies,
        "islamabad_companies":islamabad_companies
    }
    
    return render(request, 'tables.html',query_set)


# Raw SQl Query
def fetch_company_details():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.company_name, c.location, cl.company_clients
            FROM core_company c
            JOIN core_client cl ON c.id = cl.company_id
        """)
        rows = cursor.fetchall()
        return rows



