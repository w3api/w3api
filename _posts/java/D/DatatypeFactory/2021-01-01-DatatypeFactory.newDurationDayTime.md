---
title: DatatypeFactory.newDurationDayTime()
permalink: /Java/DatatypeFactory/newDurationDayTime/
date: 2021-01-11
key: Java.D.DatatypeFactory
category: Java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeFactory.metodos valor="newDurationDayTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Duration newDurationDayTime(boolean isPositive, int day, int hour, int minute, int second)
public Duration newDurationDayTime(boolean isPositive, BigInteger day, BigInteger hour, BigInteger minute, BigInteger second)
public Duration newDurationDayTime(long durationInMilliseconds)
public Duration newDurationDayTime(String lexicalRepresentation)
~~~

## Parámetros
* **int day**,  {% include w3api/param_description.html metodo=_dato parametro="int day" %}
* **long durationInMilliseconds**,  {% include w3api/param_description.html metodo=_dato parametro="long durationInMilliseconds" %}
* **BigInteger hour**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger hour" %}
* **boolean isPositive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isPositive" %}
* **int second**,  {% include w3api/param_description.html metodo=_dato parametro="int second" %}
* **int minute**,  {% include w3api/param_description.html metodo=_dato parametro="int minute" %}
* **BigInteger day**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger day" %}
* **String lexicalRepresentation**,  {% include w3api/param_description.html metodo=_dato parametro="String lexicalRepresentation" %}
* **BigInteger minute**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger minute" %}
* **BigInteger second**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger second" %}
* **int hour**,  {% include w3api/param_description.html metodo=_dato parametro="int hour" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[DatatypeFactory](/Java/DatatypeFactory/)

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
