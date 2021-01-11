---
title: LockSupport.park()
permalink: Java/LockSupport/park
date: 2021-01-11
key: JavaJava.L.LockSupport
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LockSupport.metodos valor="park" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void park()
public static void park(Object blocker)
~~~

## Parámetros
* **Object blocker**,  {% include w3api/param_description.html metodo=_dato parametro="Object blocker" %}

## Clase Padre
[LockSupport](/Java/LockSupport/)

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
