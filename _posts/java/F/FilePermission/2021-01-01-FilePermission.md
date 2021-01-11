---
title: FilePermission
permalink: Java/FilePermission
date: 2021-01-11
key: JavaJava.F.FilePermission
category: java
tags: ['java se', 'java.io', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FilePermission.description }}

## Sintaxis
~~~java
public final class FilePermission extends Permission implements Serializable
~~~

## Constructores
* [FilePermission()](/Java/FilePermission/FilePermission/)

## Métodos
* [equals()](/Java/FilePermission/equals)
* [getActions()](/Java/FilePermission/getActions)
* [hashCode()](/Java/FilePermission/hashCode)
* [implies()](/Java/FilePermission/implies)
* [newPermissionCollection()](/Java/FilePermission/newPermissionCollection)

## Ejemplo
~~~java
{{ site.data.Java.F.FilePermission.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FilePermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
