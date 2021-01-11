---
title: DecimalFormat.DecimalFormat()
permalink: Java/DecimalFormat/DecimalFormat
date: 2021-01-11
key: JavaJava.D.DecimalFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DecimalFormat.constructores valor="DecimalFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DecimalFormat()
public DecimalFormat(String pattern)
public DecimalFormat(String pattern, DecimalFormatSymbols symbols)
~~~

## Parámetros
* **DecimalFormatSymbols symbols**,  {% include w3api/param_description.html metodo=_dato parametro="DecimalFormatSymbols symbols" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DecimalFormat](/Java/DecimalFormat/)

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
