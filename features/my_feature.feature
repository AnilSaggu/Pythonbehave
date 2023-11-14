Feature: Testing Migrating XQuery to Python with Serenity BDD

  Scenario: Fetching MADSRDF and SKOS resources
    Given the URI is https://www.w3.org/1999/02/22-rdf-syntax-ns#
    When I fetch the MADSRDF resource
    Then the MADSRDF resource should return a status code of 200
    When I fetch the SKOS resource
    Then the SKOS resource should return a status code of 200
    And there should be more than 190 MADSRDF Narrowers
    And there should be more than 190 SKOS Narrowers
