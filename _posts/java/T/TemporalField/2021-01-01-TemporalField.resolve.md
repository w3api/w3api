---
title: TemporalField.resolve()
permalink: /Java/TemporalField/resolve/
date: 2021-01-11
key: Java.T.TemporalField
category: Java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TemporalField.metodos valor="resolve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default TemporalAccessor resolve(Map<TemporalField,Long> fieldValues, TemporalAccessor partialTemporal, ResolverStyle resolverStyle)
~~~

## Parámetros
* **TemporalAccessor partialTemporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor partialTemporal" %}
* **Map&lt;TemporalField**,  {% include w3api/param_description.html metodo=_dato parametro="Map<TemporalField" %}
* **Long&gt; fieldValues**,  {% include w3api/param_description.html metodo=_dato parametro="Long> fieldValues" %}
* **ResolverStyle resolverStyle**,  {% include w3api/param_description.html metodo=_dato parametro="ResolverStyle resolverStyle" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[TemporalField](/Java/TemporalField/)

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
