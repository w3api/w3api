---
title: SearchResult.SearchResult()
permalink: Java/SearchResult/SearchResult
date: 2021-01-04
key: JavaJava.S.SearchResult
category: java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SearchResult.constructores valor="SearchResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SearchResult(String name, Object obj, Attributes attrs)
public SearchResult(String name, Object obj, Attributes attrs, boolean isRelative)
public SearchResult(String name, String className, Object obj, Attributes attrs)
public SearchResult(String name, String className, Object obj, Attributes attrs, boolean isRelative)
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **boolean isRelative**,  {% include w3api/param_description.html metodo=_data parametro="boolean isRelative" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}
* **Attributes attrs**,  {% include w3api/param_description.html metodo=_data parametro="Attributes attrs" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[SearchResult](/Java/SearchResult/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SearchResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
