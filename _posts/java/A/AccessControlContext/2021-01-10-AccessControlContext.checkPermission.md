---
title: AccessControlContext.checkPermission()
permalink: Java/AccessControlContext/checkPermission
date: 2021-01-10
key: JavaJava.A.AccessControlContext
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AccessControlContext.metodos valor="checkPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void checkPermission(Permission perm) throws AccessControlException
~~~

## Parámetros
* **Permission perm**,  {% include w3api/param_description.html metodo=_dato parametro="Permission perm" %}

## Excepciones
[AccessControlException](/Java/AccessControlException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AccessControlContext](/Java/AccessControlContext/)

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
