---
title: OffsetDateTime.parse()
permalink: Java/OffsetDateTime/parse
date: 2021-01-04
key: JavaJava.O.OffsetDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OffsetDateTime.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static OffsetDateTime parse(CharSequence text)
public static OffsetDateTime parse(CharSequence text, DateTimeFormatter formatter)
~~~

## Parámetros
* **DateTimeFormatter formatter**,  {% include w3api/param_description.html metodo=_data parametro="DateTimeFormatter formatter" %}
* **CharSequence text**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence text" %}

## Excepciones
[DateTimeParseException](/Java/DateTimeParseException/)

## Clase Padre
[OffsetDateTime](/Java/OffsetDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OffsetDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
