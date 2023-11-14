from behave import given, when, then
import requests

@given(u'the URI is https://www.w3.org/1999/02/22-rdf-syntax-ns#')
def step_impl(context):
    # Implement the step logic to set the URI in the context
    context.uri = "https://www.w3.org/1999/02/22-rdf-syntax-ns#"

@when('I fetch the MADSRDF resource')
def step_fetch_madsrdf(context):
    context.madsrdf_response = requests.get(context.uri + ".madsrdf.rdf")

@then('the MADSRDF resource should return a status code of 200')
def step_madsrdf_status_code(context):
    assert context.madsrdf_response.status_code == 200, \
        f"Failed to fetch MADSRDF resource: {context.uri}.madsrdf.rdf"

@when('I fetch the SKOS resource')
def step_fetch_skos(context):
    context.skos_response = requests.get(context.uri + ".skos.rdf")

@then('the SKOS resource should return a status code of 200')
def step_skos_status_code(context):
    assert context.skos_response.status_code == 200, \
        f"Failed to fetch SKOS resource: {context.uri}.skos.rdf"

@then('there should be more than 190 MADSRDF Narrowers')
def step_check_madsrdf_narrowers(context):
    count_narrowers = len(context.madsrdf_response.json()['RDF']['Topic']['hasNarrowerAuthority'])
    assert count_narrowers > 190, f"Too many or too few MADSRDF Narrowers for {context.uri}.madsrdf.rdf"

@then('there should be more than 190 SKOS Narrowers')
def step_check_skos_narrowers(context):
    count_narrowers = len(context.skos_response.json()['RDF']['Description']['narrower'])
    assert count_narrowers > 190, f"Too many or too few SKOS Narrowers for {context.uri}.skos.rdf"
