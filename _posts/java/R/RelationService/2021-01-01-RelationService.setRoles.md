---
title: RelationService.setRoles()
permalink: /Java/RelationService/setRoles/
date: 2021-01-11
key: Java.R.RelationService
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="setRoles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RoleResult setRoles(String relationId, RoleList roleList) throws RelationServiceNotRegisteredException, IllegalArgumentException, RelationNotFoundException
~~~

## Parámetros
* **RoleList roleList**,  {% include w3api/param_description.html metodo=_dato parametro="RoleList roleList" %}
* **String relationId**,  {% include w3api/param_description.html metodo=_dato parametro="String relationId" %}

## Excepciones
[RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RelationNotFoundException](/Java/RelationNotFoundException/)

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
