---
title: RelationServiceMBean
permalink: /Java/RelationServiceMBean/
date: 2021-01-11
key: Java.R.RelationServiceMBean
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RelationServiceMBean.description }}

## Sintaxis
~~~java
public interface RelationServiceMBean
~~~

## Métodos
* [addRelation()](/Java/RelationServiceMBean/addRelation)
* [addRelationType()](/Java/RelationServiceMBean/addRelationType)
* [checkRoleReading()](/Java/RelationServiceMBean/checkRoleReading)
* [checkRoleWriting()](/Java/RelationServiceMBean/checkRoleWriting)
* [createRelation()](/Java/RelationServiceMBean/createRelation)
* [createRelationType()](/Java/RelationServiceMBean/createRelationType)
* [findAssociatedMBeans()](/Java/RelationServiceMBean/findAssociatedMBeans)
* [findReferencingRelations()](/Java/RelationServiceMBean/findReferencingRelations)
* [findRelationsOfType()](/Java/RelationServiceMBean/findRelationsOfType)
* [getAllRelationIds()](/Java/RelationServiceMBean/getAllRelationIds)
* [getAllRelationTypeNames()](/Java/RelationServiceMBean/getAllRelationTypeNames)
* [getAllRoles()](/Java/RelationServiceMBean/getAllRoles)
* [getPurgeFlag()](/Java/RelationServiceMBean/getPurgeFlag)
* [getReferencedMBeans()](/Java/RelationServiceMBean/getReferencedMBeans)
* [getRelationTypeName()](/Java/RelationServiceMBean/getRelationTypeName)
* [getRole()](/Java/RelationServiceMBean/getRole)
* [getRoleCardinality()](/Java/RelationServiceMBean/getRoleCardinality)
* [getRoleInfo()](/Java/RelationServiceMBean/getRoleInfo)
* [getRoleInfos()](/Java/RelationServiceMBean/getRoleInfos)
* [getRoles()](/Java/RelationServiceMBean/getRoles)
* [hasRelation()](/Java/RelationServiceMBean/hasRelation)
* [isActive()](/Java/RelationServiceMBean/isActive)
* [isRelation()](/Java/RelationServiceMBean/isRelation)
* [isRelationMBean()](/Java/RelationServiceMBean/isRelationMBean)
* [purgeRelations()](/Java/RelationServiceMBean/purgeRelations)
* [removeRelation()](/Java/RelationServiceMBean/removeRelation)
* [removeRelationType()](/Java/RelationServiceMBean/removeRelationType)
* [sendRelationCreationNotification()](/Java/RelationServiceMBean/sendRelationCreationNotification)
* [sendRelationRemovalNotification()](/Java/RelationServiceMBean/sendRelationRemovalNotification)
* [sendRoleUpdateNotification()](/Java/RelationServiceMBean/sendRoleUpdateNotification)
* [setPurgeFlag()](/Java/RelationServiceMBean/setPurgeFlag)
* [setRole()](/Java/RelationServiceMBean/setRole)
* [setRoles()](/Java/RelationServiceMBean/setRoles)
* [updateRoleMap()](/Java/RelationServiceMBean/updateRoleMap)

## Ejemplo
~~~java
{{ site.data.Java.R.RelationServiceMBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationServiceMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
