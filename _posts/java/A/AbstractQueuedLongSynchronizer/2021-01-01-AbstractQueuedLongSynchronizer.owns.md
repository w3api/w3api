---
title: AbstractQueuedLongSynchronizer.owns()
permalink: /Java/AbstractQueuedLongSynchronizer/owns/
date: 2021-01-11
key: Java.A.AbstractQueuedLongSynchronizer
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedLongSynchronizer.metodos valor="owns" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean owns(AbstractQueuedLongSynchronizer.ConditionObject condition)
~~~

## Parámetros
* **AbstractQueuedLongSynchronizer.ConditionObject condition**,  {% include w3api/param_description.html metodo=_dato parametro="AbstractQueuedLongSynchronizer.ConditionObject condition" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
