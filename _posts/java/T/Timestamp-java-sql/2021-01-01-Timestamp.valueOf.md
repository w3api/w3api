---
title: Timestamp.valueOf()
permalink: Java/Timestamp-java-sql/valueOf
date: 2021-01-11
key: JavaJava.T.Timestamp-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Timestamp-java-sql.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Timestamp valueOf(String s)
public static Timestamp valueOf(LocalDateTime dateTime)
~~~

## Parámetros
* **LocalDateTime dateTime**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDateTime dateTime" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

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
