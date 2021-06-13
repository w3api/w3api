---
title: RelationService.createRelationType()
permalink: /Java/RelationService/createRelationType/
date: 2021-01-11
key: Java.R.RelationService
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="createRelationType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void createRelationType(String relationTypeName, RoleInfo[] roleInfoArray) throws IllegalArgumentException, InvalidRelationTypeException
~~~

## Parámetros
* **RoleInfo[] roleInfoArray**,  {% include w3api/param_description.html metodo=_dato parametro="RoleInfo[] roleInfoArray" %}
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_dato parametro="String relationTypeName" %}

## Excepciones
[InvalidRelationTypeException](/Java/InvalidRelationTypeException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationService](/Java/RelationService/)

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
