---
title: AbstractQueuedLongSynchronizer.tryAcquire()
permalink: /Java/AbstractQueuedLongSynchronizer/tryAcquire/
date: 2021-01-11
key: Java.A.AbstractQueuedLongSynchronizer
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedLongSynchronizer.metodos valor="tryAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean tryAcquire(long arg)
~~~

## Parámetros
* **long arg**,  {% include w3api/param_description.html metodo=_dato parametro="long arg" %}

## Excepciones
[IllegalMonitorStateException](/Java/IllegalMonitorStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
