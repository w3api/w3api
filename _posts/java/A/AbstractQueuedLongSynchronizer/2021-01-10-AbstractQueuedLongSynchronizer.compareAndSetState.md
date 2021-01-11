---
title: AbstractQueuedLongSynchronizer.compareAndSetState()
permalink: Java/AbstractQueuedLongSynchronizer/compareAndSetState
date: 2021-01-10
key: JavaJava.A.AbstractQueuedLongSynchronizer
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedLongSynchronizer.metodos valor="compareAndSetState" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean compareAndSetState(long expect, long update)
~~~

## Parámetros
* **long update**,  {% include w3api/param_description.html metodo=_dato parametro="long update" %}
* **long expect**,  {% include w3api/param_description.html metodo=_dato parametro="long expect" %}

## Clase Padre
[AbstractQueuedLongSynchronizer](/Java/AbstractQueuedLongSynchronizer/)

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
