---
title: DateTimeParseException.DateTimeParseException()
permalink: /Java/DateTimeParseException/DateTimeParseException/
date: 2021-01-11
key: Java.D.DateTimeParseException
category: Java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeParseException.constructores valor="DateTimeParseException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeParseException(String message, CharSequence parsedData, int errorIndex)
public DateTimeParseException(String message, CharSequence parsedData, int errorIndex, Throwable cause)
~~~

## Parámetros
* **CharSequence parsedData**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence parsedData" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **int errorIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int errorIndex" %}

## Clase Padre
[DateTimeParseException](/Java/DateTimeParseException/)

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
