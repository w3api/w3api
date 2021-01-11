---
title: AbstractQueuedSynchronizer.tryAcquire()
permalink: Java/AbstractQueuedSynchronizer/tryAcquire
date: 2021-01-10
key: JavaJava.A.AbstractQueuedSynchronizer
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedSynchronizer.metodos valor="tryAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean tryAcquire(int arg)
~~~

## Parámetros
* **int arg**,  {% include w3api/param_description.html metodo=_dato parametro="int arg" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalMonitorStateException](/Java/IllegalMonitorStateException/)

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
