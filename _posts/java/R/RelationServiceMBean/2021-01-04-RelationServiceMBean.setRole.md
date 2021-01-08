---
title: RelationServiceMBean.setRole()
permalink: Java/RelationServiceMBean/setRole
date: 2021-01-04
key: JavaJava.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="setRole" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setRole(String relationId, Role role) throws RelationServiceNotRegisteredException, IllegalArgumentException, RelationNotFoundException, RoleNotFoundException, InvalidRoleValueException, RelationTypeNotFoundException
~~~

## Parámetros
* **String relationId**,  {% include w3api/param_description.html metodo=_data parametro="String relationId" %}
* **Role role**,  {% include w3api/param_description.html metodo=_data parametro="Role role" %}

## Excepciones
[RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [InvalidRoleValueException](/Java/InvalidRoleValueException/), [RelationNotFoundException](/Java/RelationNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [RoleNotFoundException](/Java/RoleNotFoundException/)

## Clase Padre
[RelationServiceMBean](/Java/RelationServiceMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationServiceMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
