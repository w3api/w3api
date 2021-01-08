---
title: StampedLock.tryConvertToOptimisticRead()
permalink: Java/StampedLock/tryConvertToOptimisticRead
date: 2021-01-04
key: JavaJava.S.StampedLock
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StampedLock.metodos valor="tryConvertToOptimisticRead" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long tryConvertToOptimisticRead(long stamp)
~~~

## Parámetros
* **long stamp**,  {% include w3api/param_description.html metodo=_data parametro="long stamp" %}

## Clase Padre
[StampedLock](/Java/StampedLock/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StampedLock.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
