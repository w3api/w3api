---
title: BasicPermission
permalink: Java/BasicPermission
date: 2021-01-11
key: JavaJava.B.BasicPermission
category: java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BasicPermission.description }}

## Sintaxis
~~~java
public abstract class BasicPermission extends Permission implements Serializable
~~~

## Constructores
* [BasicPermission()](/Java/BasicPermission/BasicPermission/)

## Métodos
* [equals()](/Java/BasicPermission/equals)
* [getActions()](/Java/BasicPermission/getActions)
* [hashCode()](/Java/BasicPermission/hashCode)
* [implies()](/Java/BasicPermission/implies)
* [newPermissionCollection()](/Java/BasicPermission/newPermissionCollection)

## Ejemplo
~~~java
{{ site.data.Java.B.BasicPermission.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
