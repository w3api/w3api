---
title: Permission.checkGuard()
permalink: /Java/Permission-java-security/checkGuard/
date: 2021-01-11
key: Java.P.Permission-java-security
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Permission-java-security.metodos valor="checkGuard" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void checkGuard(Object object) throws SecurityException
~~~

## Parámetros
* **Object object**,  {% include w3api/param_description.html metodo=_dato parametro="Object object" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[Permission](/Java/Permission-java-security/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
