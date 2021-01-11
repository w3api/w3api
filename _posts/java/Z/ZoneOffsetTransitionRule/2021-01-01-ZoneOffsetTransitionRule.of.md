---
title: ZoneOffsetTransitionRule.of()
permalink: Java/ZoneOffsetTransitionRule/of
date: 2021-01-11
key: JavaJava.Z.ZoneOffsetTransitionRule
category: java
tags: ['java se', 'java.time.zone', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoneOffsetTransitionRule.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ZoneOffsetTransitionRule of(Month month, int dayOfMonthIndicator, DayOfWeek dayOfWeek, LocalTime time, boolean timeEndOfDay, ZoneOffsetTransitionRule.TimeDefinition timeDefnition, ZoneOffset standardOffset, ZoneOffset offsetBefore, ZoneOffset offsetAfter)
~~~

## Parámetros
* **DayOfWeek dayOfWeek**,  {% include w3api/param_description.html metodo=_dato parametro="DayOfWeek dayOfWeek" %}
* **ZoneOffset offsetAfter**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offsetAfter" %}
* **Month month**,  {% include w3api/param_description.html metodo=_dato parametro="Month month" %}
* **int dayOfMonthIndicator**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfMonthIndicator" %}
* **boolean timeEndOfDay**,  {% include w3api/param_description.html metodo=_dato parametro="boolean timeEndOfDay" %}
* **ZoneOffsetTransitionRule.TimeDefinition timeDefnition**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffsetTransitionRule.TimeDefinition timeDefnition" %}
* **ZoneOffset standardOffset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset standardOffset" %}
* **ZoneOffset offsetBefore**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offsetBefore" %}
* **LocalTime time**,  {% include w3api/param_description.html metodo=_dato parametro="LocalTime time" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ZoneOffsetTransitionRule](/Java/ZoneOffsetTransitionRule/)

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
