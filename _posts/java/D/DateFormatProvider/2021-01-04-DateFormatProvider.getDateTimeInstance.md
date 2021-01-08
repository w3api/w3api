---
title: DateFormatProvider.getDateTimeInstance()
permalink: Java/DateFormatProvider/getDateTimeInstance
date: 2021-01-04
key: JavaJava.D.DateFormatProvider
category: java
tags: ['java se', 'java.text.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateFormatProvider.metodos valor="getDateTimeInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract DateFormat getDateTimeInstance(int dateStyle, int timeStyle, Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **int timeStyle**,  {% include w3api/param_description.html metodo=_data parametro="int timeStyle" %}
* **int dateStyle**,  {% include w3api/param_description.html metodo=_data parametro="int dateStyle" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DateFormatProvider](/Java/DateFormatProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DateFormatProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
