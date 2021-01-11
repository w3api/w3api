---
title: ZoneOffsetTransitionRule.TimeDefinition.createDateTime()
permalink: Java/ZoneOffsetTransitionRule/TimeDefinition/createDateTime
date: 2021-01-11
key: JavaJava.Z.ZoneOffsetTransitionRule.TimeDefinition
category: java
tags: ['java se', 'java.time.zone', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoneOffsetTransitionRule.TimeDefinition.metodos valor="createDateTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDateTime createDateTime(LocalDateTime dateTime, ZoneOffset standardOffset, ZoneOffset wallOffset)
~~~

## Parámetros
* **ZoneOffset standardOffset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset standardOffset" %}
* **ZoneOffset wallOffset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset wallOffset" %}
* **LocalDateTime dateTime**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDateTime dateTime" %}

## Clase Padre
[ZoneOffsetTransitionRule.TimeDefinition](/Java/ZoneOffsetTransitionRule/TimeDefinition/)

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
