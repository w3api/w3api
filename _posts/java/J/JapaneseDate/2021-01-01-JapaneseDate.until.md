---
title: JapaneseDate.until()
permalink: /Java/JapaneseDate/until/
date: 2021-01-11
key: Java.J.JapaneseDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JapaneseDate.metodos valor="until" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long until(Temporal endExclusive, TemporalUnit unit)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalUnit unit" %}
* **Temporal endExclusive**,  {% include w3api/param_description.html metodo=_dato parametro="Temporal endExclusive" %}

## Clase Padre
[JapaneseDate](/Java/JapaneseDate/)

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
