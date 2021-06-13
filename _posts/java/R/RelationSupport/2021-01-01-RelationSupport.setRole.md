---
title: RelationSupport.setRole()
permalink: /Java/RelationSupport/setRole/
date: 2021-01-11
key: Java.R.RelationSupport
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationSupport.metodos valor="setRole" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setRole(Role role) throws IllegalArgumentException, RoleNotFoundException, RelationTypeNotFoundException, InvalidRoleValueException, RelationServiceNotRegisteredException, RelationNotFoundException
~~~

## Parámetros
* **Role role**,  {% include w3api/param_description.html metodo=_dato parametro="Role role" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [RelationNotFoundException](/Java/RelationNotFoundException/), [RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [RoleNotFoundException](/Java/RoleNotFoundException/), [RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [InvalidRoleValueException](/Java/InvalidRoleValueException/)

## Clase Padre
[RelationSupport](/Java/RelationSupport/)

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
