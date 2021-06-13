---
title: RelationNotification
permalink: Java/RelationNotification
date: 2021-01-11
key: Java.R.RelationNotification
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RelationNotification.description }}

## Sintaxis
~~~java
public class RelationNotification extends Notification
~~~

## Constructores
* [RelationNotification()](/Java/RelationNotification/RelationNotification/)

## Campos
* [RELATION_BASIC_CREATION](/Java/RelationNotification/RELATION_BASIC_CREATION)
* [RELATION_BASIC_REMOVAL](/Java/RelationNotification/RELATION_BASIC_REMOVAL)
* [RELATION_BASIC_UPDATE](/Java/RelationNotification/RELATION_BASIC_UPDATE)
* [RELATION_MBEAN_CREATION](/Java/RelationNotification/RELATION_MBEAN_CREATION)
* [RELATION_MBEAN_REMOVAL](/Java/RelationNotification/RELATION_MBEAN_REMOVAL)
* [RELATION_MBEAN_UPDATE](/Java/RelationNotification/RELATION_MBEAN_UPDATE)

## Métodos
* [getMBeansToUnregister()](/Java/RelationNotification/getMBeansToUnregister)
* [getNewRoleValue()](/Java/RelationNotification/getNewRoleValue)
* [getObjectName()](/Java/RelationNotification/getObjectName)
* [getOldRoleValue()](/Java/RelationNotification/getOldRoleValue)
* [getRelationId()](/Java/RelationNotification/getRelationId)
* [getRelationTypeName()](/Java/RelationNotification/getRelationTypeName)
* [getRoleName()](/Java/RelationNotification/getRoleName)

## Ejemplo
~~~java
{{ site.data.Java.R.RelationNotification.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationNotification.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
