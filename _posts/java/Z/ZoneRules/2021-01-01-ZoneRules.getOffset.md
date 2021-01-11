---
title: ZoneRules.getOffset()
permalink: Java/ZoneRules/getOffset
date: 2021-01-11
key: JavaJava.Z.ZoneRules
category: java
tags: ['java se', 'java.time.zone', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoneRules.metodos valor="getOffset" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZoneOffset getOffset(Instant instant)
public ZoneOffset getOffset(LocalDateTime localDateTime)
~~~

## Parámetros
* **Instant instant**,  {% include w3api/param_description.html metodo=_dato parametro="Instant instant" %}
* **LocalDateTime localDateTime**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDateTime localDateTime" %}

## Clase Padre
[ZoneRules](/Java/ZoneRules/)

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
