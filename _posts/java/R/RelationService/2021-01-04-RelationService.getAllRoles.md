---
title: RelationService.getAllRoles()
permalink: Java/RelationService/getAllRoles
date: 2021-01-04
key: JavaJava.R.RelationService
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="getAllRoles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RoleResult getAllRoles(String relationId) throws IllegalArgumentException, RelationNotFoundException, RelationServiceNotRegisteredException
~~~

## Parámetros
* **String relationId**,  {% include w3api/param_description.html metodo=_data parametro="String relationId" %}

## Excepciones
[RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [RelationNotFoundException](/Java/RelationNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationService](/Java/RelationService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
