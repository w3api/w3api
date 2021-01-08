---
title: SecureClassLoader.getPermissions()
permalink: Java/SecureClassLoader/getPermissions
date: 2021-01-04
key: JavaJava.S.SecureClassLoader
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureClassLoader.metodos valor="getPermissions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected PermissionCollection getPermissions(CodeSource codesource)
~~~

## Parámetros
* **CodeSource codesource**,  {% include w3api/param_description.html metodo=_data parametro="CodeSource codesource" %}

## Clase Padre
[SecureClassLoader](/Java/SecureClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
