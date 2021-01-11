---
title: RelationServiceMBean.setRoles()
permalink: Java/RelationServiceMBean/setRoles
date: 2021-01-11
key: JavaJava.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="setRoles" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
RoleResult setRoles(String relationId, RoleList roleList) throws RelationServiceNotRegisteredException, IllegalArgumentException, RelationNotFoundException
~~~

## Parámetros
* **RoleList roleList**,  {% include w3api/param_description.html metodo=_dato parametro="RoleList roleList" %}
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
