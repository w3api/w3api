---
title: Properties.storeToXML()
permalink: Java/Properties/storeToXML
date: 2021-01-04
key: JavaJava.P.Properties
category: java
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
* **String comment**,  {% include w3api/param_description.html metodo=_data parametro="String comment" %}
* **OutputStream os**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream os" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_data parametro="Charset charset" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_data parametro="String encoding" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[Properties](/Java/Properties/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Properties.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
