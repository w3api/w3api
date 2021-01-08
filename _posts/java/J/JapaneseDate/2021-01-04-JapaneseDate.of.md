---
title: JapaneseDate.of()
permalink: Java/JapaneseDate/of
date: 2021-01-04
key: JavaJava.J.JapaneseDate
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JapaneseDate.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static JapaneseDate of(int prolepticYear, int month, int dayOfMonth)
public static JapaneseDate of(JapaneseEra era, int yearOfEra, int month, int dayOfMonth)
~~~

## Parámetros
* **JapaneseEra era**,  {% include w3api/param_description.html metodo=_data parametro="JapaneseEra era" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_data parametro="int yearOfEra" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_data parametro="int prolepticYear" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[JapaneseDate](/Java/JapaneseDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JapaneseDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
