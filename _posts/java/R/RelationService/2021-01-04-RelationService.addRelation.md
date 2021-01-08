---
title: RelationService.addRelation()
permalink: Java/RelationService/addRelation
date: 2021-01-04
key: JavaJava.R.RelationService
category: java
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
* **ObjectName relationObjectName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName relationObjectName" %}

## Excepciones
[RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [InvalidRoleValueException](/Java/InvalidRoleValueException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [InvalidRelationIdException](/Java/InvalidRelationIdException/), [RoleNotFoundException](/Java/RoleNotFoundException/), [NoSuchMethodException](/Java/NoSuchMethodException/), [InvalidRelationServiceException](/Java/InvalidRelationServiceException/)

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
