---
title: ProtectionDomain
permalink: Java/ProtectionDomain
date: 2021-01-11
key: JavaJava.P.ProtectionDomain
category: java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.ProtectionDomain.description }}

## Sintaxis
~~~java
public class ProtectionDomain extends Object
~~~

## Constructores
* [ProtectionDomain()](/Java/ProtectionDomain/ProtectionDomain/)

## Métodos
* [getClassLoader()](/Java/ProtectionDomain/getClassLoader)
* [getCodeSource()](/Java/ProtectionDomain/getCodeSource)
* [getPermissions()](/Java/ProtectionDomain/getPermissions)
* [getPrincipals()](/Java/ProtectionDomain/getPrincipals)
* [implies()](/Java/ProtectionDomain/implies)
* [staticPermissionsOnly()](/Java/ProtectionDomain/staticPermissionsOnly)
* [toString()](/Java/ProtectionDomain/toString)

## Ejemplo
~~~java
{{ site.data.Java.P.ProtectionDomain.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ProtectionDomain.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
