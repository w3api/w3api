---
title: ByteArrayOutputStream.toString()
permalink: Java/ByteArrayOutputStream/toString
date: 2021-01-11
key: JavaJava.B.ByteArrayOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteArrayOutputStream.metodos valor="toString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String toString()
@Deprecated public String toString(int hibyte)
public String toString(String charsetName) throws UnsupportedEncodingException
public String toString(Charset charset)
~~~

## Parámetros
* **String charsetName**,  {% include w3api/param_description.html metodo=_dato parametro="String charsetName" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **int hibyte**,  {% include w3api/param_description.html metodo=_dato parametro="int hibyte" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/)

## Clase Padre
[ByteArrayOutputStream](/Java/ByteArrayOutputStream/)

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
