---
title: ResponseCache.get()
permalink: Java/ResponseCache/get
date: 2021-01-04
key: JavaJava.R.ResponseCache
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
* **URI uri**,  {% include w3api/param_description.html metodo=_data parametro="URI uri" %}
* **List&lt;String&gt;&gt; rqstHeaders**,  {% include w3api/param_description.html metodo=_data parametro="List<String>> rqstHeaders" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **String rqstMethod**,  {% include w3api/param_description.html metodo=_data parametro="String rqstMethod" %}

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
{%- for _ldc in site.data.Java.R.ResponseCache.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
