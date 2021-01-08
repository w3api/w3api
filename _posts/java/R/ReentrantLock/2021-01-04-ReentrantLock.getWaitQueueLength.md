---
title: ReentrantLock.getWaitQueueLength()
permalink: Java/ReentrantLock/getWaitQueueLength
date: 2021-01-04
key: JavaJava.R.ReentrantLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReentrantLock.metodos valor="getWaitQueueLength" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getWaitQueueLength(Condition condition)
~~~

## Parámetros
* **Condition condition**,  {% include w3api/param_description.html metodo=_data parametro="Condition condition" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalMonitorStateException](/Java/IllegalMonitorStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ReentrantLock](/Java/ReentrantLock/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReentrantLock.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
