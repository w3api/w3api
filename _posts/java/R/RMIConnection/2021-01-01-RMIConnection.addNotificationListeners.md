---
title: RMIConnection.addNotificationListeners()
permalink: /Java/RMIConnection/addNotificationListeners/
date: 2021-01-11
key: Java.R.RMIConnection
category: Java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="addNotificationListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Integer[] addNotificationListeners(ObjectName[] names, MarshalledObject[] filters, Subject[] delegationSubjects) throws InstanceNotFoundException, IOException
~~~

## Parámetros
* **ObjectName[] names**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName[] names" %}
* **MarshalledObject[] filters**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject[] filters" %}
* **Subject[] delegationSubjects**,  {% include w3api/param_description.html metodo=_dato parametro="Subject[] delegationSubjects" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [ClassCastException](/Java/ClassCastException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/)

## Clase Padre
[RMIConnection](/Java/RMIConnection/)

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
