---
title: URLClassLoader.getPermissions()
permalink: Java/URLClassLoader/getPermissions
date: 2021-01-11
key: JavaJava.U.URLClassLoader
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLClassLoader.metodos valor="getPermissions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected PermissionCollection getPermissions(CodeSource codesource)
~~~

## Parámetros
* **CodeSource codesource**,  {% include w3api/param_description.html metodo=_dato parametro="CodeSource codesource" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[URLClassLoader](/Java/URLClassLoader/)

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
