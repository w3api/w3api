---
title: StampedLock.isReadLockStamp()
permalink: /Java/StampedLock/isReadLockStamp/
date: 2021-01-11
key: Java.S.StampedLock
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StampedLock.metodos valor="isReadLockStamp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean isReadLockStamp(long stamp)
~~~

## Parámetros
* **long stamp**,  {% include w3api/param_description.html metodo=_dato parametro="long stamp" %}

## Clase Padre
[StampedLock](/Java/StampedLock/)

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
