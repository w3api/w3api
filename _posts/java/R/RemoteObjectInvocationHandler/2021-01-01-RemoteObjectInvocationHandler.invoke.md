---
title: RemoteObjectInvocationHandler.invoke()
permalink: Java/RemoteObjectInvocationHandler/invoke
date: 2021-01-11
key: JavaJava.R.RemoteObjectInvocationHandler
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteObjectInvocationHandler.metodos valor="invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object invoke(Object proxy, Method method, Object[] args) throws Throwable
~~~

## Parámetros
* **Object proxy**,  {% include w3api/param_description.html metodo=_dato parametro="Object proxy" %}
* **Method method**,  {% include w3api/param_description.html metodo=_dato parametro="Method method" %}
* **Object[] args**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] args" %}

## Excepciones
[UndeclaredThrowableException](/Java/UndeclaredThrowableException/)

## Clase Padre
[RemoteObjectInvocationHandler](/Java/RemoteObjectInvocationHandler/)

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
