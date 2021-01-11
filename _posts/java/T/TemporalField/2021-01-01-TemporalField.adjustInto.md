---
title: TemporalField.adjustInto()
permalink: Java/TemporalField/adjustInto
date: 2021-01-11
key: JavaJava.T.TemporalField
category: java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TemporalField.metodos valor="adjustInto" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<R extends Temporal>R adjustInto(R temporal, long newValue)
~~~

## Parámetros
* **R temporal**,  {% include w3api/param_description.html metodo=_dato parametro="R temporal" %}
* **long newValue**,  {% include w3api/param_description.html metodo=_dato parametro="long newValue" %}

## Clase Padre
[TemporalField](/Java/TemporalField/)

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
