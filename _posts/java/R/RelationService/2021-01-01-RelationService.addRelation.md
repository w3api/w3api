---
title: RelationService.addRelation()
permalink: /Java/RelationService/addRelation/
date: 2021-01-11
key: Java.R.RelationService
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="addRelation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addRelation(ObjectName relationObjectName) throws IllegalArgumentException, RelationServiceNotRegisteredException, NoSuchMethodException, InvalidRelationIdException, InstanceNotFoundException, InvalidRelationServiceException, RelationTypeNotFoundException, RoleNotFoundException, InvalidRoleValueException
~~~

## Parámetros
* **ObjectName relationObjectName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName relationObjectName" %}

## Excepciones
[NoSuchMethodException](/Java/NoSuchMethodException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [InvalidRoleValueException](/Java/InvalidRoleValueException/), [InvalidRelationServiceException](/Java/InvalidRelationServiceException/), [RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [InvalidRelationIdException](/Java/InvalidRelationIdException/), [RoleNotFoundException](/Java/RoleNotFoundException/), [RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/)

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
