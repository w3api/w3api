---
title: InvocationHandler.invoke()
permalink: /Java/InvocationHandler/invoke/
date: 2021-01-11
key: Java.I.InvocationHandler
category: Java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InvocationHandler.metodos valor="invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object invoke(Object proxy, Method method, Object[] args) throws Throwable
~~~

## Parámetros
* **Object proxy**,  {% include w3api/param_description.html metodo=_dato parametro="Object proxy" %}
* **Method method**,  {% include w3api/param_description.html metodo=_dato parametro="Method method" %}
* **Object[] args**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] args" %}

## Excepciones
[UndeclaredThrowableException](/Java/UndeclaredThrowableException/)

## Clase Padre
[InvocationHandler](/Java/InvocationHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
