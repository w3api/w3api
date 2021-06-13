---
title: RelationService.createRelation()
permalink: Java/RelationService/createRelation
date: 2021-01-11
key: Java.R.RelationService
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="createRelation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void createRelation(String relationId, String relationTypeName, RoleList roleList) throws RelationServiceNotRegisteredException, IllegalArgumentException, RoleNotFoundException, InvalidRelationIdException, RelationTypeNotFoundException, InvalidRoleValueException
~~~

## Parámetros
* **RoleList roleList**,  {% include w3api/param_description.html metodo=_dato parametro="RoleList roleList" %}
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_dato parametro="String relationTypeName" %}
* **String relationId**,  {% include w3api/param_description.html metodo=_dato parametro="String relationId" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [InvalidRelationIdException](/Java/InvalidRelationIdException/), [RoleNotFoundException](/Java/RoleNotFoundException/), [RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [InvalidRoleValueException](/Java/InvalidRoleValueException/)

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
