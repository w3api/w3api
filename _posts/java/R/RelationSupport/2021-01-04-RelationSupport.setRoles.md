---
title: RelationSupport.setRoles()
permalink: Java/RelationSupport/setRoles
date: 2021-01-04
key: JavaJava.R.RelationSupport
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
* **RoleList list**,  {% include w3api/param_description.html metodo=_data parametro="RoleList list" %}

## Excepciones
[RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [RelationNotFoundException](/Java/RelationNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationSupport](/Java/RelationSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
