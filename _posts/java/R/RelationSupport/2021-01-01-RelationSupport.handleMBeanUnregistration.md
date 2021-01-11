---
title: RelationSupport.handleMBeanUnregistration()
permalink: Java/RelationSupport/handleMBeanUnregistration
date: 2021-01-11
key: JavaJava.R.RelationSupport
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationSupport.metodos valor="handleMBeanUnregistration" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void handleMBeanUnregistration(ObjectName objectName, String roleName) throws IllegalArgumentException, RoleNotFoundException, InvalidRoleValueException, RelationServiceNotRegisteredException, RelationTypeNotFoundException, RelationNotFoundException
~~~

## Parámetros
* **String roleName**,  {% include w3api/param_description.html metodo=_dato parametro="String roleName" %}
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName objectName" %}

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
