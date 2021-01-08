---
title: AccessController.checkPermission()
permalink: Java/AccessController/checkPermission
date: 2021-01-04
key: JavaJava.A.AccessController
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AccessController.metodos valor="checkPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void checkPermission(Permission perm) throws AccessControlException
~~~

## Parámetros
* **Permission perm**,  {% include w3api/param_description.html metodo=_data parametro="Permission perm" %}

## Excepciones
[AccessControlException](/Java/AccessControlException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AccessController](/Java/AccessController/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AccessController.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
