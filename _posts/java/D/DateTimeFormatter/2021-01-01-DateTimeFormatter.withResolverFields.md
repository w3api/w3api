---
title: DateTimeFormatter.withResolverFields()
permalink: /Java/DateTimeFormatter/withResolverFields/
date: 2021-01-11
key: Java.D.DateTimeFormatter
category: Java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatter.metodos valor="withResolverFields" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeFormatter withResolverFields(TemporalField... resolverFields)
public DateTimeFormatter withResolverFields(Set<TemporalField> resolverFields)
~~~

## Parámetros
* **Set&lt;TemporalField&gt; resolverFields**,  {% include w3api/param_description.html metodo=_dato parametro="Set<TemporalField> resolverFields" %}
* **TemporalField... resolverFields**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalField... resolverFields" %}

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
