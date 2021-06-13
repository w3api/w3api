---
title: RuleBasedCollator.compare()
permalink: Java/RuleBasedCollator/compare
date: 2021-01-11
key: Java.R.RuleBasedCollator
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RuleBasedCollator.metodos valor="compare" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int compare(String source, String target)
~~~

## Parámetros
* **String source**,  {% include w3api/param_description.html metodo=_dato parametro="String source" %}
* **String target**,  {% include w3api/param_description.html metodo=_dato parametro="String target" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[RuleBasedCollator](/Java/RuleBasedCollator/)

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
