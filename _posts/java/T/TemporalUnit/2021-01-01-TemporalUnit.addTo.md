---
title: TemporalUnit.addTo()
permalink: Java/TemporalUnit/addTo
date: 2021-01-11
key: JavaJava.T.TemporalUnit
category: java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TemporalUnit.metodos valor="addTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<R extends Temporal>R addTo(R temporal, long amount)
~~~

## Parámetros
* **R temporal**,  {% include w3api/param_description.html metodo=_dato parametro="R temporal" %}
* **long amount**,  {% include w3api/param_description.html metodo=_dato parametro="long amount" %}

## Clase Padre
[TemporalUnit](/Java/TemporalUnit/)

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
