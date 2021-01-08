---
title: AtomicLongFieldUpdater.updateAndGet()
permalink: Java/AtomicLongFieldUpdater/updateAndGet
date: 2021-01-04
key: JavaJava.A.AtomicLongFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongFieldUpdater.metodos valor="updateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final long updateAndGet(T obj, LongUnaryOperator updateFunction)
~~~

## Parámetros
* **LongUnaryOperator updateFunction**,  {% include w3api/param_description.html metodo=_data parametro="LongUnaryOperator updateFunction" %}
* **T obj**,  {% include w3api/param_description.html metodo=_data parametro="T obj" %}

## Clase Padre
[AtomicLongFieldUpdater](/Java/AtomicLongFieldUpdater/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicLongFieldUpdater.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
