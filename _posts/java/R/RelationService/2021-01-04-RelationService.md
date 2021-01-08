---
title: RelationService
permalink: Java/RelationService
date: 2021-01-04
key: JavaJava.R.RelationService
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RelationService.description }}

## Sintaxis
~~~java
public class RelationService extends NotificationBroadcasterSupport implements RelationServiceMBean, MBeanRegistration, NotificationListener
~~~

## Constructores
* [RelationService()](/Java/RelationService/RelationService/)

## Métodos
* [addRelation()](/Java/RelationService/addRelation)
* [addRelationType()](/Java/RelationService/addRelationType)
* [checkRoleReading()](/Java/RelationService/checkRoleReading)
* [checkRoleWriting()](/Java/RelationService/checkRoleWriting)
* [createRelation()](/Java/RelationService/createRelation)
* [createRelationType()](/Java/RelationService/createRelationType)
* [findAssociatedMBeans()](/Java/RelationService/findAssociatedMBeans)
* [findReferencingRelations()](/Java/RelationService/findReferencingRelations)
* [findRelationsOfType()](/Java/RelationService/findRelationsOfType)
* [getAllRelationIds()](/Java/RelationService/getAllRelationIds)
* [getAllRelationTypeNames()](/Java/RelationService/getAllRelationTypeNames)
* [getAllRoles()](/Java/RelationService/getAllRoles)
* [getNotificationInfo()](/Java/RelationService/getNotificationInfo)
* [getPurgeFlag()](/Java/RelationService/getPurgeFlag)
* [getReferencedMBeans()](/Java/RelationService/getReferencedMBeans)
* [getRelationTypeName()](/Java/RelationService/getRelationTypeName)
* [getRole()](/Java/RelationService/getRole)
* [getRoleCardinality()](/Java/RelationService/getRoleCardinality)
* [getRoleInfo()](/Java/RelationService/getRoleInfo)
* [getRoleInfos()](/Java/RelationService/getRoleInfos)
* [getRoles()](/Java/RelationService/getRoles)
* [handleNotification()](/Java/RelationService/handleNotification)
* [hasRelation()](/Java/RelationService/hasRelation)
* [isActive()](/Java/RelationService/isActive)
* [isRelation()](/Java/RelationService/isRelation)
* [isRelationMBean()](/Java/RelationService/isRelationMBean)
* [purgeRelations()](/Java/RelationService/purgeRelations)
* [removeRelation()](/Java/RelationService/removeRelation)
* [removeRelationType()](/Java/RelationService/removeRelationType)
* [sendRelationCreationNotification()](/Java/RelationService/sendRelationCreationNotification)
* [sendRelationRemovalNotification()](/Java/RelationService/sendRelationRemovalNotification)
* [sendRoleUpdateNotification()](/Java/RelationService/sendRoleUpdateNotification)
* [setPurgeFlag()](/Java/RelationService/setPurgeFlag)
* [setRole()](/Java/RelationService/setRole)
* [setRoles()](/Java/RelationService/setRoles)
* [updateRoleMap()](/Java/RelationService/updateRoleMap)

## Ejemplo
~~~java
{{ site.data.Java.R.RelationService.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
