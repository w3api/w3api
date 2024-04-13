---
title: CacheResponse.getHeaders()
permalink: /Java/CacheResponse/getHeaders/
date: 2021-01-11
key: Java.C.CacheResponse
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CacheResponse.metodos valor="getHeaders" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Map<String,List<String>> getHeaders() throws IOException
~~~

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[CacheResponse](/Java/CacheResponse/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
