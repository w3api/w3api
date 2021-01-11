---
title: RelationService.sendRoleUpdateNotification()
permalink: Java/RelationService/sendRoleUpdateNotification
date: 2021-01-11
key: JavaJava.R.RelationService
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="sendRoleUpdateNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void sendRoleUpdateNotification(String relationId, Role newRole, List<ObjectName> oldValue) throws IllegalArgumentException, RelationNotFoundException
~~~

## Parámetros
* **List&lt;ObjectName&gt; oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="List<ObjectName> oldValue" %}
* **String relationId**,  {% include w3api/param_description.html metodo=_dato parametro="String relationId" %}
* **Role newRole**,  {% include w3api/param_description.html metodo=_dato parametro="Role newRole" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [RelationNotFoundException](/Java/RelationNotFoundException/)

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
