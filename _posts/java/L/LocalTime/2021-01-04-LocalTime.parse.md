---
title: LocalTime.parse()
permalink: Java/LocalTime/parse
date: 2021-01-04
key: JavaJava.L.LocalTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalTime.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LocalTime parse(CharSequence text)
public static LocalTime parse(CharSequence text, DateTimeFormatter formatter)
~~~

## Parámetros
* **DateTimeFormatter formatter**,  {% include w3api/param_description.html metodo=_data parametro="DateTimeFormatter formatter" %}
* **CharSequence text**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence text" %}

## Excepciones
[DateTimeParseException](/Java/DateTimeParseException/)

## Clase Padre
[LocalTime](/Java/LocalTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
