---
title: AbstractQueuedSynchronizer.compareAndSetState()
permalink: /Java/AbstractQueuedSynchronizer/compareAndSetState/
date: 2021-01-11
key: Java.A.AbstractQueuedSynchronizer
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedSynchronizer.metodos valor="compareAndSetState" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean compareAndSetState(int expect, int update)
~~~

## Parámetros
* **int expect**,  {% include w3api/param_description.html metodo=_dato parametro="int expect" %}
* **int update**,  {% include w3api/param_description.html metodo=_dato parametro="int update" %}

## Clase Padre
[AbstractQueuedSynchronizer](/Java/AbstractQueuedSynchronizer/)

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
