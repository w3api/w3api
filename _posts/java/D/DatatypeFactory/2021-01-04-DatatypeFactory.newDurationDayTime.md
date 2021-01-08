---
title: DatatypeFactory.newDurationDayTime()
permalink: Java/DatatypeFactory/newDurationDayTime
date: 2021-01-04
key: JavaJava.D.DatatypeFactory
category: java
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
* **BigInteger second**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger second" %}
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}
* **boolean isPositive**,  {% include w3api/param_description.html metodo=_data parametro="boolean isPositive" %}
* **BigInteger day**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger day" %}
* **int day**,  {% include w3api/param_description.html metodo=_data parametro="int day" %}
* **BigInteger hour**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger hour" %}
* **String lexicalRepresentation**,  {% include w3api/param_description.html metodo=_data parametro="String lexicalRepresentation" %}
* **long durationInMilliseconds**,  {% include w3api/param_description.html metodo=_data parametro="long durationInMilliseconds" %}
* **int hour**,  {% include w3api/param_description.html metodo=_data parametro="int hour" %}
* **BigInteger minute**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger minute" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DatatypeFactory](/Java/DatatypeFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatatypeFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
