---
title: GZIPOutputStream.GZIPOutputStream()
permalink: Java/GZIPOutputStream/GZIPOutputStream
date: 2021-01-04
key: JavaJava.G.GZIPOutputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GZIPOutputStream.constructores valor="GZIPOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GZIPOutputStream(OutputStream out) throws IOException
public GZIPOutputStream(OutputStream out, boolean syncFlush) throws IOException
public GZIPOutputStream(OutputStream out, int size) throws IOException
public GZIPOutputStream(OutputStream out, int size, boolean syncFlush) throws IOException
~~~

## Parámetros
* **boolean syncFlush**,  {% include w3api/param_description.html metodo=_data parametro="boolean syncFlush" %}
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[GZIPOutputStream](/Java/GZIPOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GZIPOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
