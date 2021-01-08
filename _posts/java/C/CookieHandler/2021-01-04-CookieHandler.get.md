---
title: CookieHandler.get()
permalink: Java/CookieHandler/get
date: 2021-01-04
key: JavaJava.C.CookieHandler
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CookieHandler.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Map<String,List<String>> get(URI uri, Map<String,List<String>> requestHeaders) throws IOException
~~~

## Parámetros
* **List&lt;String&gt;&gt; requestHeaders**,  {% include w3api/param_description.html metodo=_data parametro="List<String>> requestHeaders" %}
* **URI uri**,  {% include w3api/param_description.html metodo=_data parametro="URI uri" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[CookieHandler](/Java/CookieHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CookieHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
