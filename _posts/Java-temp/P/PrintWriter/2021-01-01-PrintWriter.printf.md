---
title: PrintWriter.printf()
permalink: /Java/PrintWriter/printf/
date: 2021-01-11
key: Java.P.PrintWriter
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintWriter.metodos valor="printf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintWriter printf(String format, Object... args)
public PrintWriter printf(Locale l, String format, Object... args)
~~~

## Parámetros
* **Locale l**,  {% include w3api/param_description.html metodo=_dato parametro="Locale l" %}
* **String format**,  {% include w3api/param_description.html metodo=_dato parametro="String format" %}
* **Object... args**,  {% include w3api/param_description.html metodo=_dato parametro="Object... args" %}

## Excepciones
[IllegalFormatException](/Java/IllegalFormatException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrintWriter](/Java/PrintWriter/)

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
