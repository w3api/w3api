---
title: PrintWriter.format()
permalink: Java/PrintWriter/format
date: 2021-01-04
key: JavaJava.P.PrintWriter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintWriter.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintWriter format(String format, Object... args)
public PrintWriter format(Locale l, String format, Object... args)
~~~

## Parámetros
* **String format**,  {% include w3api/param_description.html metodo=_data parametro="String format" %}
* **Locale l**,  {% include w3api/param_description.html metodo=_data parametro="Locale l" %}
* **Object... args**,  {% include w3api/param_description.html metodo=_data parametro="Object... args" %}

## Excepciones
[IllegalFormatException](/Java/IllegalFormatException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrintWriter](/Java/PrintWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
