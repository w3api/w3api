---
title: PrintStream.format()
permalink: Java/PrintStream/format
date: 2021-01-04
key: JavaJava.P.PrintStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintStream.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintStream format(String format, Object... args)
public PrintStream format(Locale l, String format, Object... args)
~~~

## Parámetros
* **String format**,  {% include w3api/param_description.html metodo=_data parametro="String format" %}
* **Locale l**,  {% include w3api/param_description.html metodo=_data parametro="Locale l" %}
* **Object... args**,  {% include w3api/param_description.html metodo=_data parametro="Object... args" %}

## Excepciones
[IllegalFormatException](/Java/IllegalFormatException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrintStream](/Java/PrintStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
