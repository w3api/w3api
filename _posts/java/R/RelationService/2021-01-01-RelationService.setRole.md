---
title: RelationService.setRole()
permalink: Java/RelationService/setRole
date: 2021-01-11
key: Java.R.RelationService
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="setRole" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setRole(String relationId, Role role) throws RelationServiceNotRegisteredException, IllegalArgumentException, RelationNotFoundException, RoleNotFoundException, InvalidRoleValueException
~~~

## Parámetros
* **Role role**,  {% include w3api/param_description.html metodo=_dato parametro="Role role" %}
* **String relationId**,  {% include w3api/param_description.html metodo=_dato parametro="String relationId" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [RelationNotFoundException](/Java/RelationNotFoundException/), [RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [RoleNotFoundException](/Java/RoleNotFoundException/), [InvalidRoleValueException](/Java/InvalidRoleValueException/)

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
