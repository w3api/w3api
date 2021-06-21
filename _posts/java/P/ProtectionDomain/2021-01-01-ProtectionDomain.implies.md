---
title: ProtectionDomain.implies()
permalink: /Java/ProtectionDomain/implies/
date: 2021-01-11
key: Java.P.ProtectionDomain
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProtectionDomain.metodos valor="implies" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean implies(Permission perm)
~~~

## Parámetros
* **Permission perm**,  {% include w3api/param_description.html metodo=_dato parametro="Permission perm" %}

## Clase Padre
[ProtectionDomain](/Java/ProtectionDomain/)

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
