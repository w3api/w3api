---
title: ZoneOffsetTransition.of()
permalink: Java/ZoneOffsetTransition/of
date: 2021-01-11
key: JavaJava.Z.ZoneOffsetTransition
category: java
tags: ['java se', 'java.time.zone', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoneOffsetTransition.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ZoneOffsetTransition of(LocalDateTime transition, ZoneOffset offsetBefore, ZoneOffset offsetAfter)
~~~

## Parámetros
* **ZoneOffset offsetAfter**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offsetAfter" %}
* **LocalDateTime transition**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDateTime transition" %}
* **ZoneOffset offsetBefore**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offsetBefore" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ZoneOffsetTransition](/Java/ZoneOffsetTransition/)

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
