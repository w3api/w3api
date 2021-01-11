---
title: RelationType.getRoleInfo()
permalink: Java/RelationType/getRoleInfo
date: 2021-01-11
key: JavaJava.R.RelationType
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationType.metodos valor="getRoleInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
RoleInfo getRoleInfo(String roleInfoName) throws IllegalArgumentException, RoleInfoNotFoundException
~~~

## Parámetros
* **String roleInfoName**,  {% include w3api/param_description.html metodo=_dato parametro="String roleInfoName" %}

## Excepciones
[RoleInfoNotFoundException](/Java/RoleInfoNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationType](/Java/RelationType/)

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
