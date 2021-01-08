---
title: RelationService.updateRoleMap()
permalink: Java/RelationService/updateRoleMap
date: 2021-01-04
key: JavaJava.R.RelationService
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="updateRoleMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void updateRoleMap(String relationId, Role newRole, List<ObjectName> oldValue) throws IllegalArgumentException, RelationServiceNotRegisteredException, RelationNotFoundException
~~~

## Parámetros
* **String relationId**,  {% include w3api/param_description.html metodo=_data parametro="String relationId" %}
* **List&lt;ObjectName&gt; oldValue**,  {% include w3api/param_description.html metodo=_data parametro="List<ObjectName> oldValue" %}
* **Role newRole**,  {% include w3api/param_description.html metodo=_data parametro="Role newRole" %}

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
