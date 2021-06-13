---
title: NumberFormat.parse()
permalink: Java/NumberFormat/parse
date: 2021-01-11
key: JavaJava.N.NumberFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberFormat.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Number parse(String source) throws ParseException
public abstract Number parse(String source, ParsePosition parsePosition)
~~~

## Parámetros
* **String source**,  {% include w3api/param_description.html metodo=_dato parametro="String source" %}
* **ParsePosition parsePosition**,  {% include w3api/param_description.html metodo=_dato parametro="ParsePosition parsePosition" %}

## Excepciones
[ParseException](/Java/ParseException/)

## Clase Padre
[NumberFormat](/Java/NumberFormat/)

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
