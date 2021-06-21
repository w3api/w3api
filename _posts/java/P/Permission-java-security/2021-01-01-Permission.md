---
title: Permission
permalink: /Java/Permission-java-security/
date: 2021-01-11
key: Java.P.Permission-java-security
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.Permission-java-security.description }}

## Sintaxis
~~~java
public abstract class Permission extends Object implements Guard, Serializable
~~~

## Constructores
* [Permission()](/Java/Permission-java-security/Permission/)

## Métodos
* [checkGuard()](/Java/Permission-java-security/checkGuard)
* [equals()](/Java/Permission-java-security/equals)
* [getActions()](/Java/Permission-java-security/getActions)
* [getName()](/Java/Permission-java-security/getName)
* [hashCode()](/Java/Permission-java-security/hashCode)
* [implies()](/Java/Permission-java-security/implies)
* [newPermissionCollection()](/Java/Permission-java-security/newPermissionCollection)
* [toString()](/Java/Permission-java-security/toString)

## Ejemplo
~~~java
{{ site.data.Java.P.Permission-java-security.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.Permission-java-security.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
