---
title: LockSupport.parkUntil()
permalink: /Java/LockSupport/parkUntil/
date: 2021-01-11
key: Java.L.LockSupport
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LockSupport.metodos valor="parkUntil" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void parkUntil(long deadline)
public static void parkUntil(Object blocker, long deadline)
~~~

## Parámetros
* **Object blocker**,  {% include w3api/param_description.html metodo=_dato parametro="Object blocker" %}
* **long deadline**,  {% include w3api/param_description.html metodo=_dato parametro="long deadline" %}

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
