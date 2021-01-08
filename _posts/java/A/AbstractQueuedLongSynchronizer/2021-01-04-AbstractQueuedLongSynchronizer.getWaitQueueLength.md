---
title: AbstractQueuedLongSynchronizer.getWaitQueueLength()
permalink: Java/AbstractQueuedLongSynchronizer/getWaitQueueLength
date: 2021-01-04
key: JavaJava.A.AbstractQueuedLongSynchronizer
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedLongSynchronizer.metodos valor="getWaitQueueLength" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int getWaitQueueLength(AbstractQueuedLongSynchronizer.ConditionObject condition)
~~~

## Parámetros
* **AbstractQueuedLongSynchronizer.ConditionObject condition**,  {% include w3api/param_description.html metodo=_data parametro="AbstractQueuedLongSynchronizer.ConditionObject condition" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalMonitorStateException](/Java/IllegalMonitorStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AbstractQueuedLongSynchronizer](/Java/AbstractQueuedLongSynchronizer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractQueuedLongSynchronizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
