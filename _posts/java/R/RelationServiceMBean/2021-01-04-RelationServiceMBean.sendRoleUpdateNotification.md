---
title: RelationServiceMBean.sendRoleUpdateNotification()
permalink: Java/RelationServiceMBean/sendRoleUpdateNotification
date: 2021-01-04
key: JavaJava.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="sendRoleUpdateNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void sendRoleUpdateNotification(String relationId, Role newRole, List<ObjectName> oldRoleValue) throws IllegalArgumentException, RelationNotFoundException
~~~

## Parámetros
* **String relationId**,  {% include w3api/param_description.html metodo=_data parametro="String relationId" %}
* **Role newRole**,  {% include w3api/param_description.html metodo=_data parametro="Role newRole" %}
* **List&lt;ObjectName&gt; oldRoleValue**,  {% include w3api/param_description.html metodo=_data parametro="List<ObjectName> oldRoleValue" %}

## Excepciones
[RelationNotFoundException](/Java/RelationNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
