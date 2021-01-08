---
title: DateTimeFormatterBuilder.appendText()
permalink: Java/DateTimeFormatterBuilder/appendText
date: 2021-01-04
key: JavaJava.D.DateTimeFormatterBuilder
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatterBuilder.metodos valor="appendText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeFormatterBuilder appendText(TemporalField field)
public DateTimeFormatterBuilder appendText(TemporalField field, TextStyle textStyle)
public DateTimeFormatterBuilder appendText(TemporalField field, Map<Long,String> textLookup)
~~~

## Parámetros
* **TextStyle textStyle**,  {% include w3api/param_description.html metodo=_data parametro="TextStyle textStyle" %}
* **Map&lt;Long**,  {% include w3api/param_description.html metodo=_data parametro="Map<Long" %}
* **String&gt; textLookup**,  {% include w3api/param_description.html metodo=_data parametro="String> textLookup" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_data parametro="TemporalField field" %}

## Clase Padre
[DateTimeFormatterBuilder](/Java/DateTimeFormatterBuilder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DateTimeFormatterBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
