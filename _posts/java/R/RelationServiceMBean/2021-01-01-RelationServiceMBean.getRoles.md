---
title: RelationServiceMBean.getRoles()
permalink: /Java/RelationServiceMBean/getRoles/
date: 2021-01-11
key: Java.R.RelationServiceMBean
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="getRoles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
RoleResult getRoles(String relationId, String[] roleNameArray) throws RelationServiceNotRegisteredException, IllegalArgumentException, RelationNotFoundException
~~~

## Parámetros
* **String[] roleNameArray**,  {% include w3api/param_description.html metodo=_dato parametro="String[] roleNameArray" %}
* **String relationId**,  {% include w3api/param_description.html metodo=_dato parametro="String relationId" %}

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
