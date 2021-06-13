---
title: UnresolvedPermission
permalink: /Java/UnresolvedPermission/
date: 2021-01-11
key: Java.U.UnresolvedPermission
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.U.UnresolvedPermission.description }}

## Sintaxis
~~~java
public final class UnresolvedPermission extends Permission implements Serializable
~~~

## Constructores
* [UnresolvedPermission()](/Java/UnresolvedPermission/UnresolvedPermission/)

## Métodos
* [equals()](/Java/UnresolvedPermission/equals)
* [getActions()](/Java/UnresolvedPermission/getActions)
* [getUnresolvedActions()](/Java/UnresolvedPermission/getUnresolvedActions)
* [getUnresolvedCerts()](/Java/UnresolvedPermission/getUnresolvedCerts)
* [getUnresolvedName()](/Java/UnresolvedPermission/getUnresolvedName)
* [getUnresolvedType()](/Java/UnresolvedPermission/getUnresolvedType)
* [hashCode()](/Java/UnresolvedPermission/hashCode)
* [implies()](/Java/UnresolvedPermission/implies)
* [newPermissionCollection()](/Java/UnresolvedPermission/newPermissionCollection)
* [toString()](/Java/UnresolvedPermission/toString)

## Ejemplo
~~~java
{{ site.data.Java.U.UnresolvedPermission.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UnresolvedPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
