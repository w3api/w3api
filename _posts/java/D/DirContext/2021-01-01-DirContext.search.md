---
title: DirContext.search()
permalink: Java/DirContext/search
date: 2021-01-11
key: JavaJava.D.DirContext
category: java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirContext.metodos valor="search" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
NamingEnumeration<SearchResult> search(String name, String filterExpr, Object[] filterArgs, SearchControls cons) throws NamingException
NamingEnumeration<SearchResult> search(String name, String filter, SearchControls cons) throws NamingException
NamingEnumeration<SearchResult> search(String name, Attributes matchingAttributes) throws NamingException
NamingEnumeration<SearchResult> search(String name, Attributes matchingAttributes, String[] attributesToReturn) throws NamingException
NamingEnumeration<SearchResult> search(Name name, String filterExpr, Object[] filterArgs, SearchControls cons) throws NamingException
NamingEnumeration<SearchResult> search(Name name, String filter, SearchControls cons) throws NamingException
NamingEnumeration<SearchResult> search(Name name, Attributes matchingAttributes) throws NamingException
NamingEnumeration<SearchResult> search(Name name, Attributes matchingAttributes, String[] attributesToReturn) throws NamingException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String filterExpr**,  {% include w3api/param_description.html metodo=_dato parametro="String filterExpr" %}
* **Object[] filterArgs**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] filterArgs" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **String[] attributesToReturn**,  {% include w3api/param_description.html metodo=_dato parametro="String[] attributesToReturn" %}
* **SearchControls cons**,  {% include w3api/param_description.html metodo=_dato parametro="SearchControls cons" %}
* **Attributes matchingAttributes**,  {% include w3api/param_description.html metodo=_dato parametro="Attributes matchingAttributes" %}
* **String filter**,  {% include w3api/param_description.html metodo=_dato parametro="String filter" %}

## Excepciones
[InvalidSearchFilterException](/Java/InvalidSearchFilterException/), [InvalidSearchControlsException](/Java/InvalidSearchControlsException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NamingException](/Java/NamingException/)

## Clase Padre
[DirContext](/Java/DirContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
