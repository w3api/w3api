---
title: ZoneRules.isValidOffset()
permalink: /Java/ZoneRules/isValidOffset/
date: 2021-01-11
key: Java.Z.ZoneRules
category: Java
tags: ['java se', 'java.time.zone', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoneRules.metodos valor="isValidOffset" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isValidOffset(LocalDateTime localDateTime, ZoneOffset offset)
~~~

## Parámetros
* **ZoneOffset offset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offset" %}
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
