---
title: Timestamp.Timestamp()
permalink: /Java/Timestamp-java-sql/Timestamp/
date: 2021-01-11
key: Java.T.Timestamp-java-sql
category: Java
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
* **int nano**,  {% include w3api/param_description.html metodo=_dato parametro="int nano" %}
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}
* **long time**,  {% include w3api/param_description.html metodo=_dato parametro="long time" %}
* **int minute**,  {% include w3api/param_description.html metodo=_dato parametro="int minute" %}
* **int second**,  {% include w3api/param_description.html metodo=_dato parametro="int second" %}
* **int year**,  {% include w3api/param_description.html metodo=_dato parametro="int year" %}
* **int date**,  {% include w3api/param_description.html metodo=_dato parametro="int date" %}
* **int hour**,  {% include w3api/param_description.html metodo=_dato parametro="int hour" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
