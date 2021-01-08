---
title: Permission.checkGuard()
permalink: Java/Permission-java-security/checkGuard
date: 2021-01-04
key: JavaJava.P.Permission-java-security
category: java
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
* **Object object**,  {% include w3api/param_description.html metodo=_data parametro="Object object" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[Permission](/Java/Permission-java-security/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Permission-java-security.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
