---
title: RelationSupport.getRoles()
permalink: /Java/RelationSupport/getRoles/
date: 2021-01-11
key: Java.R.RelationSupport
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationSupport.metodos valor="getRoles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RoleResult getRoles(String[] roleNameArray) throws IllegalArgumentException, RelationServiceNotRegisteredException
~~~

## Parámetros
* **String[] roleNameArray**,  {% include w3api/param_description.html metodo=_dato parametro="String[] roleNameArray" %}

## Excepciones
[RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationSupport](/Java/RelationSupport/)

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
