---
title: AtomicBoolean.compareAndExchange()
permalink: Java/AtomicBoolean/compareAndExchange
date: 2021-01-11
key: JavaJava.A.AtomicBoolean
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicBoolean.metodos valor="compareAndExchange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean compareAndExchange(boolean expectedValue, boolean newValue)
~~~

## Parámetros
* **boolean newValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean newValue" %}
* **boolean expectedValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean expectedValue" %}

## Clase Padre
[AtomicBoolean](/Java/AtomicBoolean/)

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
