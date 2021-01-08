---
title: Timestamp.Timestamp()
permalink: Java/Timestamp-java-sql/Timestamp
date: 2021-01-04
key: JavaJava.T.Timestamp-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Timestamp-java-sql.constructores valor="Timestamp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="1.2") public Timestamp(int year, int month, int date, int hour, int minute, int second, int nano)
public Timestamp(long time)
~~~

## Parámetros
* **int date**,  {% include w3api/param_description.html metodo=_data parametro="int date" %}
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int nano**,  {% include w3api/param_description.html metodo=_data parametro="int nano" %}
* **long time**,  {% include w3api/param_description.html metodo=_data parametro="long time" %}
* **int hour**,  {% include w3api/param_description.html metodo=_data parametro="int hour" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Timestamp](/Java/Timestamp-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Timestamp-java-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
