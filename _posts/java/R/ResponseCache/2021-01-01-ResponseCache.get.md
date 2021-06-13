---
title: ResponseCache.get()
permalink: Java/ResponseCache/get
date: 2021-01-11
key: Java.R.ResponseCache
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResponseCache.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract CacheResponse get(URI uri, String rqstMethod, Map<String,List<String>> rqstHeaders) throws IOException
~~~

## Parámetros
* **String rqstMethod**,  {% include w3api/param_description.html metodo=_dato parametro="String rqstMethod" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **URI uri**,  {% include w3api/param_description.html metodo=_dato parametro="URI uri" %}
* **List&lt;String&gt;&gt; rqstHeaders**,  {% include w3api/param_description.html metodo=_dato parametro="List<String>> rqstHeaders" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ResponseCache](/Java/ResponseCache/)

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
