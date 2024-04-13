---
title: DateTimeFormatterBuilder.appendZoneText()
permalink: /Java/DateTimeFormatterBuilder/appendZoneText/
date: 2021-01-11
key: Java.D.DateTimeFormatterBuilder
category: Java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatterBuilder.metodos valor="appendZoneText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeFormatterBuilder appendZoneText(TextStyle textStyle)
public DateTimeFormatterBuilder appendZoneText(TextStyle textStyle, Set<ZoneId> preferredZones)
~~~

## Parámetros
* **TextStyle textStyle**,  {% include w3api/param_description.html metodo=_dato parametro="TextStyle textStyle" %}
* **Set&lt;ZoneId&gt; preferredZones**,  {% include w3api/param_description.html metodo=_dato parametro="Set<ZoneId> preferredZones" %}

## Clase Padre
[DateTimeFormatterBuilder](/Java/DateTimeFormatterBuilder/)

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
