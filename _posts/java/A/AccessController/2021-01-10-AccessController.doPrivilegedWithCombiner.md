---
title: AccessController.doPrivilegedWithCombiner()
permalink: Java/AccessController/doPrivilegedWithCombiner
date: 2021-01-10
key: JavaJava.A.AccessController
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AccessController.metodos valor="doPrivilegedWithCombiner" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> T doPrivilegedWithCombiner(PrivilegedAction<T> action)
static <T> T doPrivilegedWithCombiner(PrivilegedAction<T> action, AccessControlContext context, Permission... perms)
static <T> T doPrivilegedWithCombiner(PrivilegedExceptionAction<T> action)
static <T> T doPrivilegedWithCombiner(PrivilegedExceptionAction<T> action, AccessControlContext context, Permission... perms)
~~~

## Parámetros
* **Permission... perms**,  {% include w3api/param_description.html metodo=_dato parametro="Permission... perms" %}
* **PrivilegedAction&lt;T&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="PrivilegedAction<T> action" %}
* **PrivilegedExceptionAction&lt;T&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="PrivilegedExceptionAction<T> action" %}
* **AccessControlContext context**,  {% include w3api/param_description.html metodo=_dato parametro="AccessControlContext context" %}

## Clase Padre
[AccessController](/Java/AccessController/)

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
