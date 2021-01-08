---
title: RemoteObjectInvocationHandler.invoke()
permalink: Java/RemoteObjectInvocationHandler/invoke
date: 2021-01-04
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
* **Method method**,  {% include w3api/param_description.html metodo=_data parametro="Method method" %}
* **Object proxy**,  {% include w3api/param_description.html metodo=_data parametro="Object proxy" %}
* **Object[] args**,  {% include w3api/param_description.html metodo=_data parametro="Object[] args" %}

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
{%- for _ldc in site.data.Java.R.RemoteObjectInvocationHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
