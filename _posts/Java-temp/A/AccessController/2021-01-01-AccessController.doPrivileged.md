---
title: AccessController.doPrivileged()
permalink: /Java/AccessController/doPrivileged/
date: 2021-01-11
key: Java.A.AccessController
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AccessController.metodos valor="doPrivileged" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> T doPrivileged(PrivilegedAction<T> action)
static <T> T doPrivileged(PrivilegedAction<T> action, AccessControlContext context)
static <T> T doPrivileged(PrivilegedAction<T> action, AccessControlContext context, Permission... perms)
static <T> T doPrivileged(PrivilegedExceptionAction<T> action)
static <T> T doPrivileged(PrivilegedExceptionAction<T> action, AccessControlContext context)
static <T> T doPrivileged(PrivilegedExceptionAction<T> action, AccessControlContext context, Permission... perms)
~~~

## Parámetros
* **PrivilegedAction&lt;T&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="PrivilegedAction<T> action" %}
* **PrivilegedExceptionAction&lt;T&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="PrivilegedExceptionAction<T> action" %}
* **Permission... perms**,  {% include w3api/param_description.html metodo=_dato parametro="Permission... perms" %}
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
