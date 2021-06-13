---
title: Properties.storeToXML()
permalink: /Java/Properties/storeToXML/
date: 2021-01-11
key: Java.P.Properties
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Properties.metodos valor="storeToXML" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void storeToXML(OutputStream os, String comment) throws IOException
public void storeToXML(OutputStream os, String comment, String encoding) throws IOException
public void storeToXML(OutputStream os, String comment, Charset charset) throws IOException
~~~

## Parámetros
* **OutputStream os**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream os" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_dato parametro="String encoding" %}
* **String comment**,  {% include w3api/param_description.html metodo=_dato parametro="String comment" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [IOException](/Java/IOException/)

## Clase Padre
[Properties](/Java/Properties/)

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
