---
title: PosixFilePermission
permalink: /Java/PosixFilePermission/
date: 2021-01-11
key: Java.P.PosixFilePermission
category: Java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PosixFilePermission.description }}

## Sintaxis
~~~java
public enum PosixFilePermission extends Enum<PosixFilePermission>
~~~

## Enumerados
* [GROUP_EXECUTE](/Java/PosixFilePermission/GROUP_EXECUTE/)
* [GROUP_READ](/Java/PosixFilePermission/GROUP_READ/)
* [GROUP_WRITE](/Java/PosixFilePermission/GROUP_WRITE/)
* [OTHERS_EXECUTE](/Java/PosixFilePermission/OTHERS_EXECUTE/)
* [OTHERS_READ](/Java/PosixFilePermission/OTHERS_READ/)
* [OTHERS_WRITE](/Java/PosixFilePermission/OTHERS_WRITE/)
* [OWNER_EXECUTE](/Java/PosixFilePermission/OWNER_EXECUTE/)
* [OWNER_READ](/Java/PosixFilePermission/OWNER_READ/)
* [OWNER_WRITE](/Java/PosixFilePermission/OWNER_WRITE/)

## Métodos
* [valueOf()](/Java/PosixFilePermission/valueOf/)
* [values()](/Java/PosixFilePermission/values/)

## Ejemplo
~~~java
{{ site.data.Java.P.PosixFilePermission.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PosixFilePermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
