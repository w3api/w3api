---
title: AbstractQueuedSynchronizer.owns()
permalink: Java/AbstractQueuedSynchronizer/owns
date: 2021-01-04
key: JavaJava.A.AbstractQueuedSynchronizer
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractQueuedSynchronizer.metodos valor="owns" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean owns(AbstractQueuedSynchronizer.ConditionObject condition)
~~~

## Parámetros
* **AbstractQueuedSynchronizer.ConditionObject condition**,  {% include w3api/param_description.html metodo=_data parametro="AbstractQueuedSynchronizer.ConditionObject condition" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractQueuedSynchronizer](/Java/AbstractQueuedSynchronizer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractQueuedSynchronizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
