---
title: RelationSupport.handleMBeanUnregistration()
permalink: Java/RelationSupport/handleMBeanUnregistration
date: 2021-01-04
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
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName objectName" %}
* **String roleName**,  {% include w3api/param_description.html metodo=_data parametro="String roleName" %}

## Excepciones
[RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [InvalidRoleValueException](/Java/InvalidRoleValueException/), [RelationNotFoundException](/Java/RelationNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [RoleNotFoundException](/Java/RoleNotFoundException/)

## Clase Padre
[RelationSupport](/Java/RelationSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
