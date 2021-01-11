---
title: Timestamp.from()
permalink: Java/Timestamp-java-sql/from
date: 2021-01-11
key: JavaJava.T.Timestamp-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Timestamp-java-sql.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Timestamp from(Instant instant)
~~~

## Parámetros
* **Instant instant**,  {% include w3api/param_description.html metodo=_dato parametro="Instant instant" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Timestamp](/Java/Timestamp-java-sql/)

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
