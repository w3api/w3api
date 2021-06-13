---
title: CookieHandler.get()
permalink: /Java/CookieHandler/get/
date: 2021-01-11
key: Java.C.CookieHandler
category: Java
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
* **List&lt;String&gt;&gt; requestHeaders**,  {% include w3api/param_description.html metodo=_dato parametro="List<String>> requestHeaders" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **URI uri**,  {% include w3api/param_description.html metodo=_dato parametro="URI uri" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
