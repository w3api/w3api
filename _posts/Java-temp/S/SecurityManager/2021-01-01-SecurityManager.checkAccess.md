---
title: SecurityManager.checkAccess()
permalink: /Java/SecurityManager/checkAccess/
date: 2021-01-11
key: Java.S.SecurityManager
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecurityManager.metodos valor="checkAccess" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void checkAccess(Thread t)
public void checkAccess(ThreadGroup g)
~~~

## Parámetros
* **ThreadGroup g**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadGroup g" %}
* **Thread t**,  {% include w3api/param_description.html metodo=_dato parametro="Thread t" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SecurityManager](/Java/SecurityManager/)

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
