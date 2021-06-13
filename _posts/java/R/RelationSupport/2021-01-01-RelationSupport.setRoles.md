---
title: RelationSupport.setRoles()
permalink: Java/RelationSupport/setRoles
date: 2021-01-11
key: Java.R.RelationSupport
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationSupport.metodos valor="setRoles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RoleResult setRoles(RoleList list) throws IllegalArgumentException, RelationServiceNotRegisteredException, RelationTypeNotFoundException, RelationNotFoundException
~~~

## Parámetros
* **RoleList list**,  {% include w3api/param_description.html metodo=_dato parametro="RoleList list" %}

## Excepciones
[RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RelationNotFoundException](/Java/RelationNotFoundException/), [RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/)

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
