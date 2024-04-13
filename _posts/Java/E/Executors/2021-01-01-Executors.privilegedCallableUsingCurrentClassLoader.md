---
title: Executors.privilegedCallableUsingCurrentClassLoader()
permalink: /Java/Executors/privilegedCallableUsingCurrentClassLoader/
date: 2021-01-11
key: Java.E.Executors
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Executors.metodos valor="privilegedCallableUsingCurrentClassLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Callable<T> privilegedCallableUsingCurrentClassLoader(Callable<T> callable)
~~~

## Parámetros
* **Callable&lt;T&gt; callable**,  {% include w3api/param_description.html metodo=_dato parametro="Callable<T> callable" %}

## Clase Padre
[Executors](/Java/Executors/)

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
