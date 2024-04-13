---
title: GZIPInputStream.GZIPInputStream()
permalink: /Java/GZIPInputStream/GZIPInputStream/
date: 2021-01-11
key: Java.G.GZIPInputStream
category: Java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GZIPInputStream.constructores valor="GZIPInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GZIPInputStream(InputStream in) throws IOException
public GZIPInputStream(InputStream in, int size) throws IOException
~~~

## Parámetros
* **InputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream in" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [ZipException](/Java/ZipException/)

## Clase Padre
[GZIPInputStream](/Java/GZIPInputStream/)

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
