---
title: ResponseCache.put()
permalink: /Java/ResponseCache/put/
date: 2021-01-11
key: Java.R.ResponseCache
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResponseCache.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract CacheRequest put(URI uri, URLConnection conn) throws IOException
~~~

## Parámetros
* **URLConnection conn**,  {% include w3api/param_description.html metodo=_dato parametro="URLConnection conn" %}
* **URI uri**,  {% include w3api/param_description.html metodo=_dato parametro="URI uri" %}

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
