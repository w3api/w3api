---
title: DateTimeFormatter.withResolverFields()
permalink: Java/DateTimeFormatter/withResolverFields
date: 2021-01-04
key: JavaJava.D.DateTimeFormatter
category: java
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
* **TemporalField... resolverFields**,  {% include w3api/param_description.html metodo=_data parametro="TemporalField... resolverFields" %}
* **Set&lt;TemporalField&gt; resolverFields**,  {% include w3api/param_description.html metodo=_data parametro="Set<TemporalField> resolverFields" %}

## Clase Padre
[DateTimeFormatter](/Java/DateTimeFormatter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DateTimeFormatter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
