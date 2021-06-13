---
title: RelationServiceMBean.updateRoleMap()
permalink: Java/RelationServiceMBean/updateRoleMap
date: 2021-01-11
key: Java.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="updateRoleMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void updateRoleMap(String relationId, Role newRole, List<ObjectName> oldRoleValue) throws IllegalArgumentException, RelationServiceNotRegisteredException, RelationNotFoundException
~~~

## Parámetros
* **List&lt;ObjectName&gt; oldRoleValue**,  {% include w3api/param_description.html metodo=_dato parametro="List<ObjectName> oldRoleValue" %}
* **String relationId**,  {% include w3api/param_description.html metodo=_dato parametro="String relationId" %}
* **Role newRole**,  {% include w3api/param_description.html metodo=_dato parametro="Role newRole" %}

## Excepciones
[RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RelationNotFoundException](/Java/RelationNotFoundException/)

## Clase Padre
[RelationServiceMBean](/Java/RelationServiceMBean/)

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
