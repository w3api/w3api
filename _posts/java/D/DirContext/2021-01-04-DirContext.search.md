---
title: DirContext.search()
permalink: Java/DirContext/search
date: 2021-01-04
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
* **Object[] filterArgs**,  {% include w3api/param_description.html metodo=_data parametro="Object[] filterArgs" %}
* **String filter**,  {% include w3api/param_description.html metodo=_data parametro="String filter" %}
* **String filterExpr**,  {% include w3api/param_description.html metodo=_data parametro="String filterExpr" %}
* **Attributes matchingAttributes**,  {% include w3api/param_description.html metodo=_data parametro="Attributes matchingAttributes" %}
* **String[] attributesToReturn**,  {% include w3api/param_description.html metodo=_data parametro="String[] attributesToReturn" %}
* **SearchControls cons**,  {% include w3api/param_description.html metodo=_data parametro="SearchControls cons" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Name name**,  {% include w3api/param_description.html metodo=_data parametro="Name name" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NamingException](/Java/NamingException/), [InvalidSearchControlsException](/Java/InvalidSearchControlsException/), [InvalidSearchFilterException](/Java/InvalidSearchFilterException/)

## Clase Padre
[DirContext](/Java/DirContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DirContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
