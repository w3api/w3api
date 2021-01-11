---
title: XMLGregorianCalendar.setTime()
permalink: Java/XMLGregorianCalendar/setTime
date: 2021-01-11
key: JavaJava.X.XMLGregorianCalendar
category: java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLGregorianCalendar.metodos valor="setTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTime(int hour, int minute, int second)
public void setTime(int hour, int minute, int second, int millisecond)
public void setTime(int hour, int minute, int second, BigDecimal fractional)
~~~

## Parámetros
* **BigDecimal fractional**,  {% include w3api/param_description.html metodo=_dato parametro="BigDecimal fractional" %}
* **int millisecond**,  {% include w3api/param_description.html metodo=_dato parametro="int millisecond" %}
* **int second**,  {% include w3api/param_description.html metodo=_dato parametro="int second" %}
* **int minute**,  {% include w3api/param_description.html metodo=_dato parametro="int minute" %}
* **int hour**,  {% include w3api/param_description.html metodo=_dato parametro="int hour" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[XMLGregorianCalendar](/Java/XMLGregorianCalendar/)

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
