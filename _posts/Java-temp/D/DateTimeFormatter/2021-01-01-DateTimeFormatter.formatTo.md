---
title: DateTimeFormatter.formatTo()
permalink: /Java/DateTimeFormatter/formatTo/
date: 2021-01-11
key: Java.D.DateTimeFormatter
category: Java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatter.metodos valor="formatTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void formatTo(TemporalAccessor temporal, Appendable appendable)
~~~

## Parámetros
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor temporal" %}
* **Appendable appendable**,  {% include w3api/param_description.html metodo=_dato parametro="Appendable appendable" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[DateTimeFormatter](/Java/DateTimeFormatter/)

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
