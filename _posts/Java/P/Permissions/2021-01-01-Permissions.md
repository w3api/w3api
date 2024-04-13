---
title: Permissions
permalink: /Java/Permissions/
date: 2021-01-11
key: Java.P.Permissions
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.Permissions.description }}

## Sintaxis
~~~java
public final class Permissions extends PermissionCollection implements Serializable
~~~

## Constructores
* [Permissions()](/Java/Permissions/Permissions/)

## Métodos
* [add()](/Java/Permissions/add/)
* [elements()](/Java/Permissions/elements/)
* [implies()](/Java/Permissions/implies/)

## Ejemplo
~~~java
{{ site.data.Java.P.Permissions.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.Permissions.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
