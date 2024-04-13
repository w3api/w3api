---
title: AllPermission
permalink: /Java/AllPermission/
date: 2021-01-11
key: Java.A.AllPermission
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AllPermission.description }}

## Sintaxis
~~~java
public final class AllPermission extends Permission
~~~

## Constructores
* [AllPermission()](/Java/AllPermission/AllPermission/)

## Métodos
* [equals()](/Java/AllPermission/equals)
* [getActions()](/Java/AllPermission/getActions)
* [hashCode()](/Java/AllPermission/hashCode)
* [implies()](/Java/AllPermission/implies)
* [newPermissionCollection()](/Java/AllPermission/newPermissionCollection)

## Ejemplo
~~~java
{{ site.data.Java.A.AllPermission.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AllPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
