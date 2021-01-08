---
title: InvocationHandler.invoke()
permalink: Java/InvocationHandler/invoke
date: 2021-01-04
key: JavaJava.I.InvocationHandler
category: java
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
* **Method method**,  {% include w3api/param_description.html metodo=_data parametro="Method method" %}
* **Object proxy**,  {% include w3api/param_description.html metodo=_data parametro="Object proxy" %}
* **Object[] args**,  {% include w3api/param_description.html metodo=_data parametro="Object[] args" %}

## Excepciones
[UndeclaredThrowableException](/Java/UndeclaredThrowableException/)

## Clase Padre
[InvocationHandler](/Java/InvocationHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InvocationHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
