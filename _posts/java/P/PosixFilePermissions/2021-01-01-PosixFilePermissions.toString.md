---
title: PosixFilePermissions.toString()
permalink: /Java/PosixFilePermissions/toString/
date: 2021-01-11
key: Java.P.PosixFilePermissions
category: Java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PosixFilePermissions.metodos valor="toString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String toString(Set<PosixFilePermission> perms)
~~~

## Parámetros
* **Set&lt;PosixFilePermission&gt; perms**,  {% include w3api/param_description.html metodo=_dato parametro="Set<PosixFilePermission> perms" %}

## Clase Padre
[PosixFilePermissions](/Java/PosixFilePermissions/)

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
