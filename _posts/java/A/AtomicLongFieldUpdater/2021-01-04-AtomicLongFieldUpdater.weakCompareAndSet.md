---
title: AtomicLongFieldUpdater.weakCompareAndSet()
permalink: Java/AtomicLongFieldUpdater/weakCompareAndSet
date: 2021-01-04
key: JavaJava.A.AtomicLongFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongFieldUpdater.metodos valor="weakCompareAndSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean weakCompareAndSet(T obj, long expect, long update)
~~~

## Parámetros
* **long expect**,  {% include w3api/param_description.html metodo=_data parametro="long expect" %}
* **long update**,  {% include w3api/param_description.html metodo=_data parametro="long update" %}
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
